# Dockerfile, Image, Container

FROM python:3.8

WORKDIR /app

ADD factorial_digits.py .

RUN pip install --no-cache-dir numpy argparse

ENTRYPOINT ["python", "./factorial_digits.py"]
