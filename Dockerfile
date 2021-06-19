FROM python:3.7-alpine

COPY dracula.txt /bot/
COPY config.py /bot/
COPY dracula_account_api.py /bot/
COPY tweet_out_dracula.py /bot/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bot
CMD ["python3", "tweet_out_dracula.py"]