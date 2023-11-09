# import packages
import os
import psycopg2
import pandas as pd
from sqlalchemy import create_engine


# create database
CREATE_DB = 'stack/create_database.psql'
CREATE_TABLES = 'stack/create_tables.psql'

DATABASE_NAME = 'A01'

def run_psql_script(PSQL_FILE, db_name):
    print(f'creating {PSQL_FILE.split("_")[1].split(".")[0]}')
    connection_data = {'database': db_name,
        'user': 'postgres',
        'password': 'postgres',
        'host': 'localhost',
        'port': 5432}

    connection = psycopg2.connect(**connection_data)

    with open(PSQL_FILE, 'r') as infile:
        psql_script = infile.read()

    connection.autocommit = True
    cursor = connection.cursor()

    # create tables
    cursor.execute(psql_script)
    connection.commit()
    connection.close()
    return 'database created succesfully'



def populate_tables(db_name):
    print('ingesting...')
    connection_string = f'postgresql://postgres:postgres@localhost:5432/{db_name}'
    db = create_engine(connection_string)
    connection_sqlalchemy = db.connect()

    # insert metadata
    # metadata = ["author",
    #                 "madhhab_altafsir",
    #                 "region",
    #                 "period",
    #                 "exegetical_interest_method",
    #                 "school_of_theology",
    #                 "school_of_law",
    #                 "tafsir",
    #                 "author_school_of_law",
    #                 "author_exegetical_interest_method",
    #                 "author_period",
    #                 "author_region",
    #                 "author_school_of_theology",
    #                 "author_tafsir",
    #                 "region_period"]
    #
    # print('INGESTING METADATA ...')
    # for table in metadata:
    #     print(f'>>> {table}')
    #     data = pd.read_excel('/mnt/sciebo/A01 Corpora/db_preparation.ods', table)
    #     data.to_sql(table, connection_sqlalchemy, schema='metadata', if_exists='append', index=False)
    #
    # print('INGESTING QURAN ...')
    # quran = ['sura', 'aya']
    # for table in quran:
    #     print(f'>>> {table}')
    #     data = pd.read_csv(f'/home/dertrudi/Masterarbeit/Datenbank/Inputfiles/quran/{table}.csv')
    #     data.to_sql(table, connection_sqlalchemy, schema='quran', if_exists='append', index=False)
    #
    # print('INGESTING RELATIONS ...')
    # relations = ['chapter', 'subchapter', 'sentence', 'quote', 'punctuation', 'subchapter_aya']
    # for relation in relations:
    #     print(f'>>> {relation}')
    #     data = pd.read_csv(f'/home/dertrudi/Masterarbeit/Datenbank/Inputfiles/relations/{relation}.csv')
    #     data.to_sql(relation, connection_sqlalchemy, schema='tafsir', if_exists='append', index=False)

    os.chdir('/home/dertrudi/Masterarbeit/Datenbank/Inputfiles/nlp_data')
    files = os.listdir()
    files.sort()


    for file in files:
        print(f'ingesting {file}')
        data = pd.read_csv(file, delimiter=',')
        data.to_sql('word', connection_sqlalchemy, schema='tafsir', if_exists='append', index=False)
if __name__ == "__main__":
    # run_psql_script(CREATE_DB, 'postgres')
    # run_psql_script(CREATE_TABLES, 'a02')
    populate_tables(db_name='a02')