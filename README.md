# lerning-city

# 🏙️ Learning City - Django REST API

A modern e-learning backend built with **Django REST Framework** and **PostgreSQL**.  
It allows teachers to upload lessons, students to buy and access them, with secure authentication & role-based permissions.

---

## 🚀 Features

- 👨‍🏫 Teachers can create, update and delete lessons  
- 🎓 Students can buy lessons and view only their own  
- 💾 File upload support (PDF, Video, etc.)  
- 💰 Lesson pricing system  
- 🔐 JWT Authentication  
- 🧩 Role-based permissions (`IsOwner`, `IsStudent`)  
- 📘 Swagger API Documentation  
- 🐘 PostgreSQL Database  
- 🎨 Custom Swagger UI (branding ready)

---

## 🧠 Tech Stack

- **Backend:** Django, Django REST Framework  
- **Database:** PostgreSQL  
- **Auth:** Simple JWT  
- **Docs:** drf-spectacular  
- **Language:** Python 3.13+

---

## ⚙️ Installation

```bash
# 1️⃣ Clone the repository
git clone https://github.com/yourusername/learningcity.git
cd learningcity

# 2️⃣ Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# 3️⃣ Install dependencies


# 4️⃣ Setup PostgreSQL (example)
CREATE DATABASE lcity OWNER lcity;

# 5️⃣ Configure settings
# In lcity/settings.py update DATABASES section with your credentials

# 6️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

# 7️⃣ Create superuser
python manage.py createsuperuser

# 8️⃣ Run the server
python manage.py runserver
