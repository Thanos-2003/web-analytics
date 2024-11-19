from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

conversion_count = 0
total_visits = 0

@app.route('/')
def index():
    global total_visits
    total_visits += 1
    return render_template('index.html')

@app.route('/conversion', methods=['POST'])
def conversion():
    global conversion_count
    conversion_count += 1
    return render_template('index.html')

@app.route('/index')
def goBack():
    return render_template('index.html')
@app.route('/stats')
def stats():
    global conversion_count, total_visits
    conversion_rate = (conversion_count / total_visits) * 100 if total_visits > 0 else 0
    return render_template('stats.html', conversion_count=conversion_count, total_visits=total_visits,conversion_rate=conversion_rate)

if __name__ == '__main__':
    app.run(debug=True)