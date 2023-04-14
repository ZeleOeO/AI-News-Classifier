from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html', prediction={})

@app.route('/predict', methods=['POST'])
def predict():
    my_list = request.form.values()
    ans = model.predict(my_list)
    prediction = {}
    diction={}
    for index, i in enumerate(ans):
        if i == 0:
           diction[index] = "BUSINESS NEWS"
        elif i == 1:
           diction[index] = "SPORTS NEWS"
        elif i == 2:
            diction[index] = "CRIME NEWS"
        elif i == 3:
            diction[index]="SCIENCE NEWS"


    return render_template('index.html',prediction = diction)


if __name__ == '__main__':
    app.run(debug=True)
