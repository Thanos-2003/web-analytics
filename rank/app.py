from flask import Flask, render_template

app = Flask(__name__)

# Sample data for your website and competitors
data = {
    "your_website": {
        "name": "Your Website",
        "global_rank": 12000,
        "country_rank": 800,
        "total_visitors": "1.2M"
    },
    "competitors": [
        {
            "name": "Competitor 1",
            "global_rank": 10000,
            "country_rank": 700,
            "total_visitors": "1.5M"
        },
        {
            "name": "Competitor 2",
            "global_rank": 15000,
            "country_rank": 900,
            "total_visitors": "900K"
        },
        {
            "name": "Competitor 3",
            "global_rank": 20000,
            "country_rank": 1100,
            "total_visitors": "600K"
        }
    ]
}

@app.route('/')
def home():
    return render_template('index.html', data=data)

@app.route('/compare')
def compare():
    return render_template('compare.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
