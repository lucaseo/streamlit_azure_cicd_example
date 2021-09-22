FROM python:3.8-slim-buster

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         build-essential libopenmpi-dev freetds-dev \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY . /app
WORKDIR /app

# RUN pip install -r requirements.txt --no-cache-dir
RUN pip install -r requirements.txt

EXPOSE 80
# EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]