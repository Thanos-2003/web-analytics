from flask import Flask, session, render_template, request
from collections import defaultdict

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-memory data structures to store visit data
all_visits = []
unique_visits = set()

@app.route('/')
def index():
    user_ip = request.remote_addr
    all_visits.append(user_ip)
    unique_visits.add(user_ip)
    session['user_ip'] = user_ip
    
    return render_template('index.html', user_ip=user_ip)

@app.route('/analytics')
def analytics():
    total_visits = len(all_visits)
    total_unique_visits = len(unique_visits)
    
    return render_template('result.html', total_visits=total_visits, total_unique_visits=total_unique_visits, all_visits=all_visits)

if __name__ == '__main__':
    app.run(debug=True)