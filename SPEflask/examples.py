import matplotlib
matplotlib.use('Agg')
import sys
import argparse
import matplotlib.pyplot as plt
from ast import literal_eval as make_tuple
import time


def myfunc1():
    data = open("uber_economics_processed_combined", "r")
    results = []
    for row in data:
        results.append(make_tuple(row))
    plt.bar(range(len(results)), [val[1] for val in results], align='center')
    plt.xticks(range(len(results)), [val[0] for val in results])
    plt.xticks(rotation=20,fontsize=8)
    #plt.show()
    plt.savefig('static/borough.png')
    plt.clf()
    data.flush()
    data.close()

def myfunc2():
    data = open("taxi_bussiness_processed_combined", "r")
    results = []
    for row in data:
        results.append(make_tuple(row))
    plt.bar(range(len(results)), [val[1] for val in results], align='center')
    plt.xticks(range(len(results)), [val[0] for val in results])
    plt.xticks(rotation=20,fontsize=8)
    #plt.show()
    plt.savefig('static/taxi_buisness.png')
    plt.clf()
    data.flush()
    data.close()

def myfunc3():
    data = open("taxi_economics_processed_combined", "r")
    results = []
    for row in data:
        results.append(make_tuple(row))
    plt.bar(range(len(results)), [val[1] for val in results], align='center')
    plt.xticks(range(len(results)), [val[0] for val in results])
    plt.xticks(rotation=20,fontsize=8)
    #plt.show()
    plt.savefig('static/taxi_economics.png')
    plt.clf()
    data.flush()
    data.close()

def myfunc4():
    data = open("uber_wethear_processed_combined", "r")
    results = []
    for row in data:
        results.append(make_tuple(row))
    plt.bar(range(len(results)), [val[1] for val in results], align='center')
    plt.xticks(range(len(results)), [val[0] for val in results])
    plt.xticks(rotation=20,fontsize=8)
    #plt.show()
    plt.savefig('static/uber_weather.png')
    plt.clf()
    data.flush()
    data.close()

def myfunc5():
    data = open("taxi_wethear_processed_combined", "r")
    results = []
    for row in data:
        results.append(make_tuple(row))
    plt.bar(range(len(results)), [val[1] for val in results], align='center')
    plt.xticks(range(len(results)), [val[0] for val in results])
    plt.xticks(rotation=20,fontsize=8)
    #plt.show()
    plt.savefig('static/taxi_weather.png')
    plt.clf()
    data.flush()
    data.close()

def myfunc6():
    data = open("weekdays_weekends_uber", "r")
    results = []
    for row in data:
        results.append(make_tuple(row))
    plt.bar(range(len(results)), [val[1] for val in results], align='center')
    plt.xticks(range(len(results)), [val[0] for val in results])
    plt.xticks(rotation=20,fontsize=8)
    #plt.show()
    plt.savefig('static/uber_week.png')
    plt.clf()
    data.flush()
    data.close()

def myfunc7():
    data = open("weekdays_weekends_taxi", "r")
    results = []
    for row in data:
        results.append(make_tuple(row))
    plt.bar(range(len(results)), [val[1] for val in results], align='center')
    plt.xticks(range(len(results)), [val[0] for val in results])
    plt.xticks(rotation=20,fontsize=8)
    #plt.show()
    plt.savefig('static/taxi_week.png')
    plt.clf()
    data.flush()
    data.close()


def myfunc8():
    data = open("uber_bussiness_processed_combined", "r")
    results = []
    for row in data:
        results.append(make_tuple(row))
    plt.bar(range(len(results)), [val[1] for val in results], align='center')
    plt.xticks(range(len(results)), [val[0] for val in results])
    plt.xticks(rotation=20,fontsize=8)
    #plt.show()
    plt.savefig('static/uber_business.png')
    plt.clf()
    data.flush()
    data.close()

#myfunc1()
#myfunc2()
#myfunc3()
#myfunc4()
#myfunc5()
#myfunc6()
#myfunc7()
#myfunc8()
