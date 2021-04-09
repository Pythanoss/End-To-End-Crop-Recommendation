from flask import Flask,render_template,request
import pickle

model_file=open('model.pkl','rb')
model=pickle.load(model_file)
model_file.close()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods=['POST', 'GET'])
def predict():
    n=request.form['n']
    p=request.form['p']
    k=request.form['k']
    temp=request.form['temp']
    humidity=request.form['humidity']
    ph=request.form['ph']
    rain=request.form['rainfall']
    output=model.predict([[n,p,k,temp,humidity,ph,rain]])

    return "<h1>You should plant {}</h1>".format(output[0])
    
    






if __name__ == '__main__':
    app.run()