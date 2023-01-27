import pandas as pd
import argparse
import os
import wget
from time import time
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name 
    url = params.url
    csv_name = 'output.csv'

    wget.download(url=url, out=csv_name)

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000, compression='gzip')
    df = next(df_iter)
    df.tpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    # head with n=0 returns headers; so running the below creates a empty database with given schema
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    df.to_sql(name=table_name, con=engine, if_exists='append')

    while True:
        t_start = time()

        df = next(df_iter)
        
        df.tpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
        
        df.to_sql(name=table_name, con=engine, if_exists='append')
        t_end = time()
        
        print('inserted another chunk..., took %.3f second' % (t_end - t_start))    


if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres.')

    # user, password, host, port, DB name, Table name, URL of the csv

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database for postgres')
    parser.add_argument('--table_name', help='name of the write table')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()
    
    main(args)