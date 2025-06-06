FROM python:3.12

WORKDIR /code
RUN pip install flask
COPY word_picker.py /code/word_picker.py
ENV FLASK_APP=/code/word_picker.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
