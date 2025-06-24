# 🔗 URL Shortener API

A high-performance and lightweight URL Shortener built using **FastAPI**, **SQLAlchemy**, and **SQLite/PostgreSQL**. It allows you to shorten long URLs into tiny, easy-to-share links and redirect users to the original URLs with blazing-fast speed.

---

## 🚀 Features

- 🔒 Validates URLs before shortening
- 📦 SQLite/PostgreSQL-compatible ORM using SQLAlchemy
- ⚡ FastAPI-powered RESTful API
- 📆 Automatic timestamping
- 🔁 URL redirection
- 📜 Environment variable configuration using `.env`
- ✅ URL format validation with `validators`
- 🌐 Asynchronous and production-ready

---

## 📦 Tech Stack

| Tech | Version |
|------|---------|
| Python | 3.x |
| FastAPI | 0.75.0 |
| SQLAlchemy | 1.4.32 |
| Uvicorn | 0.17.6 |
| Pydantic | 1.10.22 |
| validators | 0.35.0 |
| dotenv | 0.19.2 |

---

## 🛠 Installation

```bash
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```
## ⚙️ Environment Setup
Create a .env file in the root directory:

```bash
DATABASE_URL=sqlite:///./shortener.db  # or use PostgreSQL URL
BASE_URL=http://localhost:8000
```
## 📁 Project Structure
```
url_shortener/
├── app/
│ ├── main.py # FastAPI app entry point
│ ├── models.py # SQLAlchemy models (URL model)
│ ├── schemas.py # Pydantic schemas for request/response
│ ├── database.py # Database engine and session management
│ ├── utils.py # Utility functions (e.g., token generation, validation)
│ └── routers/
│ └── shortener.py # API routes for URL shortening and redirection
├── .env # Environment variables (DB URL, base URL, etc.)
├── requirements.txt # Python dependencies
└── README.md # Project documentation

````




