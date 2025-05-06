FROM python:3

ADD Poker.py .

RUN pip install requests beautifulsoup4

CMD ["python", "./Poker.py"]