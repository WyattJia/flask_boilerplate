FROM python:2.7

MAINTAINER Wells Jia <wellschuan@gmail.com>

RUN apt-get update \
    && apt-get install -y apt-transport-https 

ADD . /app

WORKDIR /app


RUN apt-get update \ 
    && apt-get install -y curl \ 
                          python \ 
                          python-dev \ 
                          python-pip \ 
                          build-essential \ 
    && apt-get clean \ 
    && apt-get autoclean \ 
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \ 
    && pip install -r requirements.txt

RUN cd /app

