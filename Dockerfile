FROM python:3.10-slim

WORKDIR /code/
ADD . /code/

RUN pip install -r requirements.txt

ENV SECRET_KEY="0)kng*$i=qd)$x(nv!($%e%8&_x*(b8ud0l3r&rsss&3d3wfbf"
ENV DEBUG="FALSE"

EXPOSE 8000

