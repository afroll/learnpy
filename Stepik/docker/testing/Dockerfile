FROM python:3.6

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY ../../pythonProject/test /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 6080

ENV TZ Europe/Moscow

CMD ["python", "app.py"]