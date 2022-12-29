from flask import Flask,request,render_template,url_for
import joblib
import sklearn


app=Flask(__name__)
model=joblib.load(r"C:\Users\koush\OneDrive\Desktop\Moses k\Innomatics\Data\fish_model.joblib")

@app.route("/")
def f():
    return render_template("index.html")

@app.route("/home",methods=["GET","POST"])
def home():
    var1=int(request.form["species"])
    var2=float(request.form["Length1"])
    var3=float(request.form["Length2"])
    var4=float(request.form["Length3"])
    var5=float(request.form["Height"])
    var6=float(request.form["Width"])
    predict=model.predict([[var1,var2,var3,var4,var5,var6]])
    return "your Expected weight is : "+str(predict)

if __name__=="__main__":
    app.run(debug=True)
