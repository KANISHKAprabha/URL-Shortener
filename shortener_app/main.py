import validators
from fastapi import Depends, FastAPI, HTTPException,Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse, RedirectResponse
from . import models, schemas,crud
from .database import Sessionlocal, engine
from starlette.datastructures import URL
from .config import get_settings
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app=FastAPI()
models.Base.metadata.create_all(bind=engine)
db=Sessionlocal()


# Mount folders (non-intrusive)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()



def raise_bad_request(message):
    raise HTTPException(status_code=400,detail=message)

def get_admin_info(db_url:models.URL)->schemas.URLInfo:
    base_url = URL(get_settings().base_url)
    admin_endpoint = app.url_path_for(
         "administration info", secret_key=db_url.secret_key
    )
    db_url.url = str(base_url.replace(path=db_url.key))
    db_url.admin_url = str(base_url.replace(path=admin_endpoint))
    return db_url


@app.get("/", response_class=HTMLResponse)
def serve_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})




@app.post("/url", response_model = schemas.URLInfo)
def create_url(url:schemas.URLBase,Session =Depends(get_db)):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")
    db_url = crud.create_db_url(db=db,url=url)
    return get_admin_info(db_url)

    
@app.get("/{url_key}")
def forward_to_target_url(
    url_key : str,
    request :Request,
    db : Session = Depends(get_db)

):
    if db_url:=crud.get_db_url_by_key(db=db,url_key=url_key):
        crud.update_db_clicks(db=db,db_url=db_url)
        return RedirectResponse(url=db_url.target_url)
    else:
         return crud.raise_not_found(request)



@app.get(
    "/admin/{secret_key}",
    name = "administration info",
    response_model = schemas.URLInfo,
)
def get_url_info(
    secret_key:str, request :Request,db:Session = Depends(get_db)
):
    if db_url:=crud.get_db_url_by_secret_key(db, secret_key=secret_key):
        db_url.url = db_url.key
        db_url.admin_url = db_url.secret_key
        return db_url
    else:
        return crud.raise_not_found(request)


@app.delete("/admin/{secret_key}")
def delete_url(
    secret_key: str, request: Request, db: Session = Depends(get_db)
):
    print(secret_key,"line 97")
    if db_url := crud.deactivate_db_url_by_secret_key(db, secret_key=secret_key):
        message = f"Successfully deleted shortened URL for '{db_url.target_url}'"
        return {"detail": message}
    else:
        return crud.raise_not_found(request)