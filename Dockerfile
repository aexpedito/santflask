FROM python:3.9-bullseye

RUN cd /usr/src/ && mkdir app

ENV APP_HOME /usr/src/app
WORKDIR /$APP_HOME

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8082

CMD ["python", "main.py", "8082"]

