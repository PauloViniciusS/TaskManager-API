FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Used for .db file
RUN mkdir -p /app/data 

# For prod 
CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]