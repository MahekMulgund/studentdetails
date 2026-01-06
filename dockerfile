FROM python:3.10

WORKDIR /studentdetails

COPY . .

CMD ["python", "studentdetails.py"]
