from flask import Flask,render_template,request, flash
import pickle
import numpy as np

# @app.route('/')
# def hello_world():
#     return 'Hello, This is Anitha...Trying out Render!'
# -*- coding: utf-8 -*-




app=Flask(__name__) #instantiating flask object
app.secret_key = 'super secret'

model=pickle.load(open('model.pickle','rb'))

#prediction function
def ValuePredictor(to_predict_list):
    to_predict = [np.array(to_predict_list)]
    print(type(model))
    result = model.predict(to_predict)
    return result[0]


@app.route('/')
@app.route('/home')
def home():
    return render_template('predictform.html')
 
@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == 'GET':
        to_predict_list = request.args.to_dict()
        to_predict_list = to_predict_list.values()
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)       
        if int(result)== 1:
           #prediction ='Income more than 50K'
           flash('Income more than 50K')
        else:
           #prediction ='Income less that 50K'
           flash('Income more than 50K')
        return render_template("result.html")
       #return redirect(url_for('home'))
       #return render_template("result.html", prediction = prediction)
        
    
@app.errorhandler(500)
def internal_error(error):
    return "500 error"

    
if __name__=='__main__':
    app.run(port=8000)
