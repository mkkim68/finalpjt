import os
import pandas as pd
import numpy as np
import sqlite3
from django.conf import settings

db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')

def deposit_recommend_age(target_age):
    con = sqlite3.connect(db_path)
    Query_String = f"SELECT * FROM accounts_user a INNER JOIN accounts_user_deposit b ON a.id = b.user_id WHERE a.age BETWEEN {target_age - 5} AND {target_age + 5}"
    df = pd.read_sql_query(Query_String, con)
    answer = df['deposit_id'].value_counts().head(3)
    con.close()
    return answer.index

# deposit_recommend_age(30)

def deposit_recommend_bank(target):
    con = sqlite3.connect(db_path)
    Query_String = f"SELECT * FROM banks_deposit WHERE fin_co_no = '{target}';"
    df = pd.read_sql_query(Query_String, con)
    print(df)
    con.close()

# deposit_recommend_bank('0010001')
    
def deposit_recommend_balance(target):
    con = sqlite3.connect(db_path)
    Query_String = f"SELECT * FROM accounts_user WHERE balance BETWEEN {target - 500000} AND {target + 500000}"
    df = pd.read_sql_query(Query_String, con)
    print(df)
    con.close()

# deposit_recommend_balance(100000)
    
def deposit_recommend_income(target):
    con = sqlite3.connect(db_path)
    Query_String = f"SELECT * FROM accounts_user WHERE income BETWEEN {target - 5000000} AND {target + 5000000}"
    df = pd.read_sql_query(Query_String, con)
    print(df)
    con.close()

# deposit_recommend_income(50000000)
    
def deposit_recommend_type(target):
    con = sqlite3.connect(db_path)
    Query_String = f"SELECT * FROM accounts_user WHERE invest_type='{target}'"
    df = pd.read_sql_query(Query_String, con)
    print(df)
    con.close()

# deposit_recommend_type('성실')