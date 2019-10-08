FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install click
CMD ["python", "main.py", "--dictionary", "dict.txt", "--input", "input.txt", "--debug"]