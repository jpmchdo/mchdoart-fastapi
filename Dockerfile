FROM python:3.9.19-bullseye

WORKDIR /usr/src/app

COPY Requirements.txt ./

RUN pip install -r Requirements.txt

COPY . .

CMD ["uvicorn", "app.Main:app", "--host", "0.0.0.0", "--port", "8000"]