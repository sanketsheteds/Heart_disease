from flask import Flask, render_template, request, jsonify
from utils import HeartPrediction
import CONFIG

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def load_raw():
    if request.method == 'GET':
        data = request.args
    elif request.method == 'POST':
        data = request.form
        return jsonify({"message": "successful"})
    
    else:
        return jsonify({"message": "Unsuccessful"})

    pred_obj = HeartPrediction()
    predict_disease = pred_obj.predict_result(data)
    print(predict_disease)

    return render_template("index.html", result=predict_disease)


if __name__ == "__main__":
    app.run(host=CONFIG.HOST, port=CONFIG.PORT)
