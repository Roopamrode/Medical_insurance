# from flask import Flask, render_template,jsonify,request,redirect,url_for
# from Project_app.utils import MedicalInsurance
# import config

# app  = Flask(__name__)

# app = Flask(__name__, template_folder='./templates', static_folder='./static')
# @app.route('/')

# def hello_world():
#     return render_template('home.html')

# # @app.route("/")  
# # def hello_flask():
# #     print("Welcome to flask")
# #     return render_template("home.html")

# # @app.route("/result/<name>")  
# # def result(name):
# #     return f"Hello {name}"

# # @app.route("/login",methods = ["POST","GET"])  
# # def login():
# #     if request.method == "POST":
# #         data = request.form 
# #         name = data["name"]
# #         print("Name:",name)
# #         return redirect(url_for('result',name = name))

# #     if request.method == "GET":
# #         name = request.args.get("name")
# #         print("Name:",name)
# #         return redirect(url_for('result',name = name))

    


# # ###############################################################################################

# # @app.route("/predict_charges",methods = ["POST","GET"])
# # def get_insurance_charges():
# #     if request.method == "POST":

# #         print("Using POST Method")

# #         data = request.form 
# #         age = eval(data["age"])
# #         sex = data['sex']
# #         bmi = eval(data["bmi"])
# #         children = eval(data["children"])
# #         smoker = data["smoker"]
# #         region = data["region"]

# #         print("age,sex,bmi,children,smoker,region",age,sex,bmi,children,smoker,region)

# #         med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
# #         charges = med_ins.get_predicted_charges()

# #         return jsonify({"Result":f"Predicted Medical Insurance Charges are :{charges}"})






# app.run() #server start



from flask import Flask, request, url_for, redirect, render_template
import pickle
import json
import config
from Project_app import utils
import numpy as np


app = Flask(__name__, template_folder='./templates', static_folder='./static')

with open(config.MODEL_FILE_PATH,"rb") as f:
            model=pickle.load(f)
@app.route('/')

def hello_world():
    return render_template('login.html')



@app.route('/predict', methods=['POST','GET'])
def predict():
    print([x for x in request.form.values()])
    features = [x for x in request.form.values()]
    age=features[0]
    sex=features[1]
    bmi=features[2]
    children=features[3]
    smoker=features[4]
    region=features[5]
    print(features)
    md=utils.MedicalInsurance(age,sex,bmi,children,smoker,region)
    # final = np.array(features).reshape((1,6))
    # print(final)
    # pred = model.predict(final)[0]
    # print(pred)
    pred=md.get_predicted_charges()
    
    return render_template('op.html', pred='Expected amount is {}'.format(pred))

if __name__ == '__main__':
    app.run(debug=True)
       


app.run()