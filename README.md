# Learning Log (Django Project)

This project is a web application built using Django that allows users to keep track of topics they are learning and create journal entries for each topic.

It is based on the project from the book:

*Python Crash Course (3rd Edition)* by Eric Matthes

---

## Features

- Create, read, update, and delete learning topics  
- Add entries under each topic  
- Track your personal learning progress  
- User authentication (login/logout)  
- Clean and simple UI powered by Django templates  

---

## Purpose

This project is part of my journey to:

- Learn Python and Django fundamentals  
- Understand how web applications work (CRUD, authentication, routing)  
- Build a strong foundation before moving into AI / Machine Learning  

---

## Project Structure

```
learning-log/
│
├── learning_logs/     # Main app for topics and entries
├── users/             # User authentication system
├── ll_env/            # Virtual environment (optional)
├── db.sqlite3         # Database
├── manage.py          # Django CLI entry point
├── requirements.txt   # Dependencies
└── README.md
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/benidict1995/learning-log.git
cd learning-log
```

2. Create a virtual environment:

```bash
python -m venv ll_env
source ll_env/bin/activate   # macOS/Linux
ll_env\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Open in your browser:

```
http://127.0.0.1:8000/
```

---

## Admin Access (Optional)

Create a superuser:

```bash
python manage.py createsuperuser
```

---

## Learning Source

This project is based on:

- *Python Crash Course (3rd Edition)* — Eric Matthes  

Huge credit to Eric Matthes for providing an excellent beginner-friendly Python course.

---

## What I Learned

- Django project structure  
- Models, Views, Templates (MVT)  
- User authentication  
- Database migrations  
- Building a CRUD web application  

---

## Future Improvements

- Improve UI/UX design  
- Add REST API (Django REST Framework)  
- Deploy to production (Render / Railway / AWS)  
- Add automated tests  

---

## Contributions

This is a personal learning project, but feedback is welcome!

---

## Final Note

> "The best way to learn is by building."

This project is one of my first steps toward becoming an AI Engineer.
