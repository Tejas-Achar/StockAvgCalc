from flask import Flask, request
import math


app = Flask(__name__)

# X = [(A*B)-(A*D)]/(D-C)


@app.route("/calculate",methods=["POST"])
def calcReqUnits():

    reqobj = request.get_json()
    NOS = int(reqobj["NOS"])
    AVS = int(reqobj["AVS"])
    CMV = int(reqobj["CMV"])
    TA = int(reqobj["TA"])
    Req_Units = math.ceil(((NOS*AVS) - (NOS*TA))/(TA-CMV))
    money = Req_Units*CMV
    result = {"url":"You will have to buy "+str(Req_Units)+ " units, which will cost you : "+str(money)}
    
    if result == {"url":"You will have to buy 0 units, which will cost you : 0"}:
        result = {"url":"Please Provide Valid Input"}
    
    
    return result


if __name__ == '_main_':
    app.run()
