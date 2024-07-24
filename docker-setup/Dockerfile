FROM python:3.9.1


RUN pip install pandas sqlalchemy psycopg2-binary
RUN pip install pyarrow

WORKDIR /app

COPY ingest_ny_taxi_data.py ingest_ny_taxi_data.py

ENTRYPOINT [ "python","ingest_ny_taxi_data.py" ]

