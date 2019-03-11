FROM python:2

WORKDIR /Users/yehuda/PycharmProjects/kin/

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "./sms_sender/app.py" ]
