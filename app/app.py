import pickle
from flask import Flask, render_template, request
from utils import convert_sentiment, page_not_found


# load model
with open("model.pkl", "rb") as f:
    global model
    model = pickle.load(f)

app = Flask(__name__)
app.register_error_handler(404, page_not_found)

@app.route('/')
def my_form():
    return render_template('form.html')


@app.route("/", methods=["POST"])
def sentiment():

    text = request.form['sentiment'].lower()
    input_text = [text]
    predict = model.predict(input_text)[0]
    sentiment = convert_sentiment(predict)
    
    return render_template('form.html', sentiment=sentiment, text=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='1000', debug=True)