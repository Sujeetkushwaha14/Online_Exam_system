# 📝 Online Exam System (Flask-based)

This is a web-based exam platform built using Flask (Python). It supports:

* User signup and login (with session management)
* One-time exam attempt enforcement
* Auto-submission with timer
* Cheating detection and blocking
* Result and review page after submission
* Optional database support (fallback to in-memory mode)

---

## 🔧 Features

* 🛡️ Secure login & signup with hashed passwords (SHA256)
* 🧠 25+ Hard DevOps questions (Kubernetes, Docker, Terraform, Jenkins, Ansible etc.)
* ⏱️ Timer-based auto-submit to prevent cheating
* 🛑 Re-entry detection & user blocking
* 📊 Exam score and answer review system
* 🧩 Modular code structure using `questions_module.py`

---

## 🗃️ Project Structure

```
.
├── app.py
├── questions_module.py
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── exam.html
│   ├── result.html
│   ├── review.html
│   └── already_attempted.html
├── static/
│   └── (your CSS/JS files if needed)
└── README.md
```

---

## 🚀 How to Run

### ✅ Prerequisites

* Python 3.8+
* Flask

### 🔌 Setup Instructions

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install flask

# Run the app
python app.py
```

Then go to [http://localhost:5000](http://localhost:5000)

---

## ⚙️ Configuration

* If you want to use a database, create a `database.py` file that provides a `get_connection()` method.
* Otherwise, the system will fall back to in-memory mode.

---

## ✏️ Adding Questions

You can add/edit questions in:

```
questions_module.py
```

Each question is a dictionary with:

```python
{
    "id": 1,
    "question": "Your question?",
    "options": ["A", "B", "C", "D"],
    "answer": "Correct Answer"
}
```

---

## 👨‍💻 Author

Sujeet Kushwaha
🔗 [LinkedIn Profile](https://www.linkedin.com/in/sujeet-kushwaha-915619245)
