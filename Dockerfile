FROM python:3.8

COPY . /app

WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENV PORT 8080
EXPOSE 8080
CMD python -m uvicorn main:app --host 0.0.0.0 --port 8080