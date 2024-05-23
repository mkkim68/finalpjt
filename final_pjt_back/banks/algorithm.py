import os
import sys
import pandas as pd
import sqlite3
import django
from django.conf import settings

# 프로젝트 루트 디렉토리를 PYTHONPATH에 추가
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Django settings 초기화
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_pjt_back.settings')
django.setup()

# settings에서 BASE_DIR 가져오기
db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')

# 데이터베이스 연결 설정
con = sqlite3.connect(db_path)

# 비슷한 나이(+5살)의 사람들이 가장 많이 가입한 3개
def deposit_recommend_age(target_age):
    Query_String = f"""
    SELECT b.deposit_id FROM accounts_user a 
    INNER JOIN accounts_user_deposit b ON a.id = b.user_id 
    WHERE a.age BETWEEN {target_age - 5} AND {target_age + 5}
    """
    df = pd.read_sql_query(Query_String, con)
    top_deposits = df['deposit_id'].value_counts().nlargest(3).index.values.tolist()

    if not top_deposits:
        return []
    deposits_str = ','.join(map(str, top_deposits))
    Query_String = f"""
    SELECT fin_prdt_cd, fin_prdt_nm FROM banks_deposit 
    WHERE id IN ({deposits_str})
    """
    result_df = pd.read_sql_query(Query_String, con)
    result_list = result_df.to_dict(orient='records')
    return result_list

# 같은 은행에 있는 상품들 전체
def deposit_recommend_bank(target):
    Query_String = f"SELECT fin_prdt_cd, fin_prdt_nm FROM banks_deposit WHERE fin_co_no = '{target}';"
    df = pd.read_sql_query(Query_String, con)
    result_list = df.to_dict(orient='records')
    return result_list

# 비슷한 자산 규모의 사람들이 가장 많이 가입한 3개
def deposit_recommend_balance(target):
    Query_String = f"""
    SELECT b.deposit_id FROM accounts_user a 
    INNER JOIN accounts_user_deposit b ON a.id = b.user_id 
    WHERE a.balance BETWEEN {target - 500000} AND {target + 500000}
    """
    df = pd.read_sql_query(Query_String, con)
    top_deposits = df['deposit_id'].value_counts().nlargest(3).index.values.tolist()

    if not top_deposits:
        return []
    deposits_str = ','.join(map(str, top_deposits))
    Query_String = f"""
    SELECT fin_prdt_cd, fin_prdt_nm FROM banks_deposit 
    WHERE id IN ({deposits_str})
    """
    result_df = pd.read_sql_query(Query_String, con)
    result_list = result_df.to_dict(orient='records')
    return result_list

# 비슷한 연봉의 사람들이 가장 많이 가입한 3개
def deposit_recommend_income(target):
    Query_String = f"""
    SELECT b.deposit_id FROM accounts_user a 
    INNER JOIN accounts_user_deposit b ON a.id = b.user_id 
    WHERE a.income BETWEEN {target - 5000000} AND {target + 5000000}
    """
    df = pd.read_sql_query(Query_String, con)
    top_deposits = df['deposit_id'].value_counts().nlargest(3).index.values.tolist()

    if not top_deposits:
        return []
    deposits_str = ','.join(map(str, top_deposits))
    Query_String = f"""
    SELECT fin_prdt_cd, fin_prdt_nm FROM banks_deposit 
    WHERE id IN ({deposits_str})
    """
    result_df = pd.read_sql_query(Query_String, con)
    result_list = result_df.to_dict(orient='records')
    return result_list

# 같은 타입인 사람들이 가장 많이 가입한 3개
def deposit_recommend_type(target):
    Query_String = f"""
    SELECT b.deposit_id FROM accounts_user a 
    INNER JOIN accounts_user_deposit b ON a.id = b.user_id 
    WHERE a.invest_type='{target}'
    """
    df = pd.read_sql_query(Query_String, con)
    top_deposits = df['deposit_id'].value_counts().nlargest(3).index.values.tolist()

    if not top_deposits:
        return []
    deposits_str = ','.join(map(str, top_deposits))
    Query_String = f"""
    SELECT fin_prdt_cd, fin_prdt_nm FROM banks_deposit 
    WHERE id IN ({deposits_str})
    """
    result_df = pd.read_sql_query(Query_String, con)
    result_list = result_df.to_dict(orient='records')
    return result_list

# Example usage
print(deposit_recommend_age(30))
print(deposit_recommend_bank('0010016'))
print(deposit_recommend_balance(100000))
print(deposit_recommend_income(50000000))
print(deposit_recommend_type('성실'))

# 데이터베이스 연결 닫기
con.close()
