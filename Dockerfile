FROM ubuntu:latest
LABEL authors="Vlepic"


FROM python:3.11
ADD main.py .
ADD bot.py .
ADD Timer.py .
RUN pip install discord.py
RUN pip install pynacl
ENTRYPOINT ["python", "./main.py"]