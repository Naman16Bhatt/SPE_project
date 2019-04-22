from flask import Flask, render_template 
import flask
from examples import myfunc1,myfunc2,myfunc3,myfunc4,myfunc5,myfunc6,myfunc7,myfunc8
#from flask_ngrok import run_with_ngrok

import logging
from logging.handlers import RotatingFileHandler
from flask import request

app = Flask(__name__)
#run_with_ngrok(app)
@app.route("/")
def home():
    print(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    return render_template("index.html")


@app.route("/data1")
def home1():
    return render_template("home.html")

@app.route("/data2")
def home2():
    return render_template("new.html")

@app.route("/ubereco")
def data1():
    myfunc1()
    return render_template("borough.html")

@app.route("/taxibusiness")
def data2():
    myfunc2()
    return render_template("taxi_buisness.html")

@app.route("/taxieco")
def data3():
    myfunc3()
    return render_template("taxi_economics.html")

@app.route("/uberweather")
def data4():
    myfunc4()
    return render_template("uber_weather.html")

@app.route("/taxiweather")
def data5():
    myfunc5()
    return render_template("taxi_weather.html")

@app.route("/uberweek")
def data6():
    myfunc6()
    return render_template("uber_week.html")


@app.route("/taxiweek")
def data7():
    myfunc7()
    return render_template("taxi_week.html")

@app.route("/uberbusiness")
def data8():
    myfunc8()
    return render_template("uber_business.html")

@app.route("/ubermonthly")
def data9():
    return render_template("Monthly count per borough for uber.html")

@app.route("/taximonthly")
def data10():
    return render_template("Monthly count per borough for taxi.html")

@app.route("/salvador")
def salvador():
    return "Hello, Salvador"

if __name__ == "__main__":
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    formatter = logging.Formatter( "%(asctime)s | %(pathname)s:%(lineno)d | %(funcName)s | %(levelname)s | %(message)s ")
    #handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    log.addHandler(handler)
    app.run(debug=True)
