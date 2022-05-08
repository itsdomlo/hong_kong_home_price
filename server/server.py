from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_district_names')
def get_district_names():
    response = jsonify({
        'districts': util.get_district_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    area = float(request.form['area'])
    market = request.form['market']
    district = request.form['district']
    util.predict_price(area, market, district)
    response = jsonify({
        'predicted_price': util.predict_price(area, market, district)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server for Hong Kong home price prediction...")
    util.load_save_artifacts()
    app.run()
