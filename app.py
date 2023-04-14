from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    my_list = request.form.values()
    ans = model.predict(my_list)
    diction={}
    for index, i in enumerate(ans):
        if i == 0:
           ans = "BUSINESS NEWS"
        elif i == 1:
           ans = "SPORTS NEWS"
        elif i == 2:
            ans = "CRIME NEWS"
        elif i == 3:
            ans="SCIENCE NEWS"
        diction[index]=ans


    return render_template('index.html',prediction = diction)


if __name__ == '__main__':
    app.run()
