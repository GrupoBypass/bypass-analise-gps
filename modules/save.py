import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


def get_connection():
    load_dotenv()
    try:
        username = os.getenv("DB_USER")
        password = os.getenv("DB_PASS")
        host = os.getenv("DB_HOST")
        database = os.getenv("DB_NAME")
    except KeyError:
        print("Variáveis de ambiente não definidas")

    return f"mysql+pymysql://{username}:{password}@{host}/{database}"


def get_engine(connection_string):
    return create_engine(connection_string)


def save_results(n, memory_result, time_result):
    df = pd.DataFrame({"memory_result": memory_result,
                      "time_result": time_result})

    df.to_csv("results.csv", index=False)

    # SQL part
    table_name = "results"
    df.to_sql(
        name=table_name,
        con=get_engine(get_connection()),
        if_exists="append",
        index=False,
    )
