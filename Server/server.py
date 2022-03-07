from flask import Flask,request,jsonify
import util

app = Flask(__name__)

@app.route('/get_loc_names')
def get_loc_names():
  response = jsonify({
      'locations': util.get_loc_names()
  })
  response.headers.add('Access-Control-Allow-Origin','*')
  return response

@app.route('/predict_home_price',methods = ['POST'])
def predict_home_price():
    sqft = float(request.form['sqft'])
    loc = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.predict_home_price(loc,sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print('Starting Python Flask Server...')
    util.load_saved_artifacts()
    app.run()