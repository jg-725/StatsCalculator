FROM python:3.7

ADD src /src

CMD [ "python", "./src/Calculator_Tests.py" ]