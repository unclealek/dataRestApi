import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

def load_sensor_data():
    data = pd.read_excel('data.xls', usecols=['Temperature', 'Time', 'Moisture'], engine='xlrd')
    data['Time'] = pd.to_datetime(data['Time'])
    return data

sensor_data = load_sensor_data()

@app.route('/data', methods=['GET'])
def get_all_data():
    data_dict = sensor_data.to_dict(orient='records')
    return jsonify(data_dict)

if __name__ == '__main__':
    app.run(debug=True)
