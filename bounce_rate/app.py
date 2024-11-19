from flask import Flask, render_template, request

app = Flask(__name__)

# Metrics
total_visits = 0
single_page_visits = 0
page_visits = {}
exit_visits = {}


@app.route('/')
def index():
    global total_visits, single_page_visits
    total_visits += 1
    
    page_visits['index'] = page_visits.get('index', 0) + 1
    
    if 'from_page' in request.args:
        from_page = request.args['from_page']
        exit_visits[from_page] = exit_visits.get(from_page, 0) + 1
    else:
        single_page_visits += 1

    return render_template('index.html')

@app.route('/about')
def about():
    global total_visits, single_page_visits
    total_visits += 1
    
    page_visits['about'] = page_visits.get('about', 0) + 1
    
    if 'from_page' in request.args:
        from_page = request.args['from_page']
        exit_visits[from_page] = exit_visits.get(from_page, 0) + 1
    else:
        single_page_visits += 1

    return render_template('about.html')

@app.route('/contact')
def contact():
    global total_visits, single_page_visits
    total_visits += 1
    
    page_visits['contact'] = page_visits.get('contact', 0) + 1
    
    if 'from_page' in request.args:
        from_page = request.args['from_page']
        exit_visits[from_page] = exit_visits.get(from_page, 0) + 1
    else:
        single_page_visits += 1

    return render_template('contact.html')

@app.route('/stats')
def stats():
    global total_visits, single_page_visits
    
    bounce_rate = (single_page_visits / total_visits) * 100 if total_visits > 0 else 0
    
    exit_rates = {}
    for page, visits in page_visits.items():
        exits = exit_visits.get(page, 0)
        exit_rate = (exits / visits) * 100 if visits > 0 else 0
        exit_rates[page] = exit_rate
    
    return render_template('stats.html', total_visits=total_visits,single_page_visits=single_page_visits, bounce_rate=bounce_rate, exit_rates=exit_rates)

if __name__ == '__main__':
    app.run(debug=True)