from flask import Flask,request,render_template

from src.pipeline.prediction_pipeline import PredictPipeline,CustomData

app=Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
def predict_datapoint():
    if request.method=="GET":
        return render_template("form.html")
    else:
        data = CustomData(
    Time=float(request.form.get("Time")),
    Amount=float(request.form.get("Amount")),

    V1=float(request.form.get("V1")),
    V2=float(request.form.get("V2")),
    V3=float(request.form.get("V3")),
    V4=float(request.form.get("V4")),
    V5=float(request.form.get("V5")),
    V6=float(request.form.get("V6")),
    V7=float(request.form.get("V7")),
    V8=float(request.form.get("V8")),
    V9=float(request.form.get("V9")),
    V10=float(request.form.get("V10")),

    V11=float(request.form.get("V11")),
    V12=float(request.form.get("V12")),
    V13=float(request.form.get("V13")),
    V14=float(request.form.get("V14")),
    V15=float(request.form.get("V15")),
    V16=float(request.form.get("V16")),
    V17=float(request.form.get("V17")),
    V18=float(request.form.get("V18")),
    V19=float(request.form.get("V19")),
    V20=float(request.form.get("V20")),

    V21=float(request.form.get("V21")),
    V22=float(request.form.get("V22")),
    V23=float(request.form.get("V23")),
    V24=float(request.form.get("V24")),
    V25=float(request.form.get("V25")),
    V26=float(request.form.get("V26")),
    V27=float(request.form.get("V27")),
    V28=float(request.form.get("V28"))
)

        final_data=data.get_data_as_dataframe()

        predict_pipeline=PredictPipeline()

        pred=predict_pipeline.predict(final_data)

        prediction = pred[0]

        if prediction == 1:
            result = "Fraudulent Transaction Detected"
        else:
            result = "Normal Transaction"

        return render_template("result.html",final_result=result)



if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000)