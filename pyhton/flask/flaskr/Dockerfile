FROM alpine:3.21
RUN apk add --no-cache python3 py3-pip
COPY . /app
WORKDIR /app
RUN python -m venv venv
RUN source venv/bin/activate && pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
# ENTRYPOINT ["echo", "hello,world!"]