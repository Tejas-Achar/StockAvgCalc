from flask import Flask, request
import math


app = Flask(__name__)

# X = [(A*B)-(A*D)]/(D-C)


@app.route("/calculate",methods=["POST"])
def calcReqUnits():

    reqobj = request.get_json()
    NOS = reqobj["NOS"]
    AVS = reqobj["AVS"]
    CMV = reqobj["CMV"]
    TA = reqobj["TA"]
    Req_Units = ((NOS*AVS) - (NOS*TA))/(TA-CMV)
    result = {"url":str(Req_Unit)}
    return result


if __name__ == '_main_':
    app.run()
