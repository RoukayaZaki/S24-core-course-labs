from flask import Flask, render_template
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)

@app.route('/')
def current_time_moscow():
    # Get the current time in UTC
    utc_now = datetime.utcnow()

    # Get the timezone for Moscow
    moscow_tz = pytz.timezone('Europe/Moscow')

    # Convert UTC time to Moscow time
    moscow_time = utc_now + timedelta(seconds=moscow_tz.utcoffset(utc_now).seconds)

    # Render the template with the current time
    return render_template('index.html', current_time=moscow_time.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    app.run(debug=True)