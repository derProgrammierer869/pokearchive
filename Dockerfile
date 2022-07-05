FROM python:3.10.2-alpine
WORKDIR /Users/nicholascrosbie/desktop/coding/flaskproject
ADD . /Users/nicholascrosbie/desktop/coding/flaskproject
RUN pip install -r requirements.txt
CMD ["python3","flasktest.py"]
