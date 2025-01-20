from flask import Flask, request
import pickle

first_app = Flask(__name__) # create an app instance

with open("rfclf.pkl", "rb") as f:
    model = pickle.load(f)

@first_app.route("/ping", methods=["GET"])
def ping():
    return "pong"

@first_app.route("/home", methods=["GET"])
def home_ping():
    return "home-pong"

@first_app.route("/predict", methods=["POST"])
def predict():
    input_params = request.get_json()
    Pclass = input_params['Pclass']

    if Pclass not in [1,2,3]:
        return "Invalid data input in Pclass"
    
    if input_params['Sex'] == 'Male':
        Sex = 0
    elif input_params['Sex'] == 'Female':
        Sex = 1
    else:
        return "Invalid data input in Sex"
    
    Age = input_params['Age']

    data = [[Pclass, Sex, Age, 1,0,0,1,0]]
    result = model.predict(data)

    if result == 1:
        return "Survived"
    else:
        return "Not survived"
    

if __name__ == "__main__":        # on running python app.py
    first_app.run(host="0.0.0.0", port=5000)
