FROM python:latest

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python", "-m", "twitterbot"]