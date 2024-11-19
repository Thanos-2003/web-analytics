from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# In-memory storage for demonstration purposes
referrals = {}
destinations = {}

@app.route('/')
def home():
    # Capture the referral source
    referrer = request.referrer
    
    if referrer:
        if referrer in referrals:
            referrals[referrer] += 1
        else:
            referrals[referrer] = 1

    return render_template('index.html')

@app.route('/go/<destination>')
def go_to_destination(destination):
    # Capture outgoing visits to destinations
    url = request.url
    
    if destination in destinations:
        destinations[destination] += 1
    else:
        destinations[destination] = 1

    # Simulate a redirect to the destination URL
    return redirect(f"http://{destination}")

@app.route('/analysis')
def analysis():
    return render_template('analysis.html', referrals=referrals, destinations=destinations)

if __name__ == '__main__':
    app.run(debug=True)
