import pandas as pd
import numpy as np
import sqlite3

con = sqlite3.connect(r"C:\Users\SSAFY\Documents\mk\PJT\final-pjt\final_pjt_back\db.sqlite3")
def deposit_recommend_age(target_age):
    Query_String = f"SELECT * FROM accounts_user a INNER JOIN accounts_user_deposit b ON a.id = b.user_id WHERE a.age BETWEEN {target_age - 5} AND {target_age + 5}"
    df = pd.read_sql_query(Query_String, con)
    answer = df['deposit_id'].value_counts().head(3)
    con.close()
    return 'hi'

# deposit_recommend_age(30)

def deposit_recommend_bank(target):
    Query_String = f"SELECT * FROM banks_deposit WHERE fin_co_no = '{target}';"
    df = pd.read_sql_query(Query_String, con)
    print(df)
    con.close()

# deposit_recommend_bank('0010001')
    
def deposit_recommend_balance(target):
    Query_String = f"SELECT * FROM accounts_user WHERE balance BETWEEN {target - 500000} AND {target + 500000}"
    df = pd.read_sql_query(Query_String, con)
    print(df)
    con.close()

# deposit_recommend_balance(100000)
    
def deposit_recommend_income(target):
    Query_String = f"SELECT * FROM accounts_user WHERE income BETWEEN {target - 5000000} AND {target + 5000000}"
    df = pd.read_sql_query(Query_String, con)
    print(df)
    con.close()

# deposit_recommend_income(50000000)
    
def deposit_recommend_type(target):
    Query_String = f"SELECT * FROM accounts_user WHERE invest_type='{target}'"
    df = pd.read_sql_query(Query_String, con)
    print(df)
    con.close()

# deposit_recommend_type('성실')