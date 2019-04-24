FROM ubuntu:16.04

#MAINTANER Your Name "youremail@domain.tld"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
RUN pip install --upgrade pip
RUN apt-get install -y python-tk
# We copy just the requirements.txt first to leverage Docker cache
#COPY ./examples.py ./examples.py
#COPY ./templates ./templates
#COPY ./taxi_2014_weather ./taxi_2014_weather
#COPY ./taxi_2015_weather ./taxi_2015_weather
#COPY ./taxi_processed_combined ./taxi_processed_combined
#COPY ./taxi_bussiness_processed_combined ./taxi_bussiness_processed_combined
#COPY ./taxi_economics_processed_combined ./taxi_economics_processed_combined
#COPY ./taxi_wethear_processed_combined ./taxi_wethear_processed_combined
#COPY ./taxi_income_processed_combined ./taxi_income_processed_combined
#COPY ./weekdays_weekends_taxi ./weekdays_weekends_taxi
#COPY ./weekdays_weekends_uber ./weekdays_weekends_uber



#COPY ./Uber_2014_weather ./Uber_2014_weather
#COPY ./Uber_2015_weather ./Uber_2015_weather
##COPY ./uber_processed_combined ./uber_processed_combined
#COPY ./uber_bussiness_processed_combined ./uber_bussiness_processed_combined
#COPY ./uber_economics_processed_combined ./uber_economics_processed_combined
#COPY ./uber_wethear_processed_combined ./uber_wethear_processed_combined
#COPY ./uber_income_processed_combined ./uber_income_processed_combined


WORKDIR /app

RUN pip install flask
RUN pip install matplotlib


COPY . /app
RUN export FLASK_APP=app.py
#ENTRYPOINT [ "python" ]
WORKDIR /app
CMD [ "flask","run","--host","0.0.0.0" ]


