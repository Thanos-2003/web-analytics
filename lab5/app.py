from flask import Flask, session, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Secret key for session management

# Variable to store the total time spent on the page in seconds
total_time_spent_seconds = 0

@app.route('/')
def home():
    record_entry_time()
    return render_template('home.html')

@app.route('/exitt')
def exit_page():
    record_exit_time()
    return render_template('exitt.html', total_time_spent_seconds=total_time_spent_seconds)


def record_entry_time():
    session['entry_time'] = datetime.now().replace(tzinfo=None)

def record_exit_time():
    global total_time_spent_seconds
    exit_time = datetime.now().replace(tzinfo=None)
    entry_time = session.get('entry_time', exit_time).replace(tzinfo=None)  # Default to exit_time if entry_time is not set
    time_spent = (exit_time - entry_time).total_seconds()
    total_time_spent_seconds += time_spent
    session.pop('entry_time', None)  # Clear the session entry time

@app.route('/reset')
def reset_time():
    global total_time_spent_seconds
    total_time_spent_seconds = 0
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)