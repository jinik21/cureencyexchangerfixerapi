from flask import Flask,render_template,request
import requests
access_key="*use fixer api keys*" #requires fixer.io keys
app = Flask(__name__)
res = requests.get(("http://data.fixer.io/api/symbols?access_key=2997831793c17c299ea3b4825e9637b9"+access_key))
if res.status_code != 200:
    raise Exception("ERROR: API request unsuccessful.")
data = res.json()
k=data["symbols"]
    

@app.route("/",methods=["POST","GET"])
def index():
    return render_template('curency.html',lst=k)
    
@app.route("/thankU",methods=["POST"])
def conversion():
    base=request.form.get("bform")
    toc=request.form.get("tform")
    amount=int(request.form.get("amount"))
    urlg="http://data.fixer.io/api/latest?access_key="+access_key+"&base="+base+"&symbols="+toc

    rpc=requests.get(urlg)

    if rpc.status_code != 200:
        return {{"ERROR: API request unsuccessful."}}
    conv=rpc.json()
    covrt=conv["rates"][toc]
    convamt=covrt*amount
    
    return render_template('converted.html',lst=k,bas=base,toc=toc,amount=amount,convamt=convamt)
