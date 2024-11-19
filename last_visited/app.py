from flask import Flask, request, render_template, session
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
# Retrieve and update the last visited time
    last_visited = session.get('last_visited')
    session['last_visited'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Retrieve and update the page visit count
    page_count = session.get('page_count', 0) + 1
    session['page_count'] = page_count

    return render_template('index.html', last_visited=last_visited,
page_count=page_count)

if __name__ == '__main__':
    app.run(debug=True)