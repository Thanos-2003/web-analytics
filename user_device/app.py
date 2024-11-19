from flask import Flask, request, render_template
from user_agents import parse

app = Flask(__name__)

# Function to determine the device type
def get_device_type(user_agent):
    ua = parse(user_agent)
    if ua.is_mobile:
        return "Mobile"
    elif ua.is_tablet:
        return "Tablet"
    elif ua.is_pc:
        return "PC"
    elif ua.is_bot:
        return "Bot"
    else:
        return "Unknown"

# Sample data
device_data = []

@app.route('/')
def home():
    user_agent = request.headers.get('User-Agent')
    url = request.url
    device_type = get_device_type(user_agent)

    # Store the data
    device_data.append({
        'url': url,
        'user_agent': user_agent,
        'device_type': device_type
    })

    return render_template('index.html', device_data=device_data)

if __name__ == '__main__':
    app.run(debug=True)
