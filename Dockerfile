FROM python:3.7

ADD . .

CMD [ "python", "-m", "unittest", "disciver", "-s", "tests" ]