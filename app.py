try:
    from database import get_connection
    db_enabled = True
except ImportError as e:
    print("⚠️ Database module not available. Running in fallback mode.")
    get_connection = None
    db_enabled = False

from flask import Flask, render_template, request, redirect, session
import hashlib, threading, time
from questions_module import get_questions
from waitress import serve 

app = Flask(__name__)
app.secret_key = "secret"

# Simulated user database (in-memory fallback)
users = {}
# Store exam attempt status
attempted_users = {}
# Store user answers for review
user_answers = {}
# Blocked users due to cheating
blocked_users = set()
# Store users who opened exam page but didn't submit
entered_exam_page = set()
# Store exam start times
exam_start_times = {}

# Sample questions
questions = get_questions()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def home():
    return redirect('/login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = hash_password(request.form['password'])

        db_success = False
        if db_enabled:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
                conn.close()
                db_success = True
            except Exception as e:
                print("⚠️ DB Error:", e)

        if not db_success:
            if username in users:
                return "User already exists. <a href='/signup'>Try again</a>"
            users[username] = password
            attempted_users[username] = False

        return redirect('/login')

    return render_template('signup.html', db_enabled=db_enabled)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hash_password(request.form['password'])

        if username in blocked_users:
            return "You have been blocked from taking the exam due to a rule violation."

        if db_enabled:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT password FROM users WHERE username=?", (username,))
                row = cursor.fetchone()
                conn.close()
                if row and row[0] == password:
                    session['user'] = username
                    return redirect('/exam')
                else:
                    return "Invalid credentials. <a href='/login'>Try again</a>"
            except Exception as e:
                print("⚠️ DB Error:", e)

        if username in users and users[username] == password:
            session['user'] = username
            return redirect('/exam')
        else:
            return "Invalid credentials. <a href='/login'>Try again</a>"

    return render_template('login.html')

@app.route('/exam')
def exam():
    if 'user' not in session:
        return redirect('/login')
    username = session['user']
    if username in blocked_users:
        session.clear()
        return "Access denied. You have been blocked."
    if attempted_users.get(username):
        return render_template('already_attempted.html', username=username)
    if username in entered_exam_page:
        return "You have already accessed the exam. Re-entry is not allowed."

    entered_exam_page.add(username)
    exam_start_times[username] = time.time()
    threading.Thread(target=auto_submit_timer, args=(username,)).start()
    return render_template('exam.html', questions=questions, username=username)

def auto_submit_timer(username):
    total_seconds = len(questions) * 60
    time.sleep(total_seconds)
    if username in entered_exam_page and not attempted_users.get(username):
        with app.app_context():
            blocked_users.add(username)
            entered_exam_page.discard(username)
            attempted_users[username] = True
            user_answers[username] = {}

@app.route('/submit', methods=['POST'])
def submit():
    if 'user' not in session:
        return redirect('/login')
    username = session['user']
    if username in blocked_users:
        session.clear()
        return "Access denied. You have been blocked."
    if attempted_users.get(username):
        return redirect('/exam')

    score = 0
    answers = {}

    for q in questions:
        user_ans = request.form.get(str(q['id']))
        answers[q['id']] = {
            "question": q['question'],
            "selected": user_ans,
            "correct": q['answer'],
            "status": "Correct" if user_ans == q['answer'] else "Wrong"
        }
        if user_ans == q['answer']:
            score += 1

    attempted_users[username] = True
    user_answers[username] = answers
    entered_exam_page.discard(username)

    return render_template('result.html', score=score, total=len(questions), username=username, answers=answers)

@app.route('/review')
def review():
    if 'user' not in session:
        return redirect('/login')
    username = session['user']
    if not attempted_users.get(username):
        return redirect('/exam')
    answers = user_answers.get(username, {})
    return render_template('review.html', username=username, answers=answers)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/block_user')
def block_user():
    username = session.get('user')
    if username:
        blocked_users.add(username)
        session.clear()
    return redirect('/login')

if __name__ == '__main__':
    serve(app,host='0.0.0.0',port='5000')
