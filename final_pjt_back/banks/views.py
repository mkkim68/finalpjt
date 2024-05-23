import os
import sys
import pandas as pd
from django.db import connection
import django
from django.conf import settings

# 프로젝트 루트 디렉토리를 PYTHONPATH에 추가
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Django settings 초기화
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_pjt_back.settings')
django.setup()

# 예금
# 비슷한 나이(+5살)의 사람들이 가장 많이 가입한 3개
def deposit_recommend_age(target_age):
    Query_String = f"""
    SELECT b.deposit_id FROM accounts_user a 
    INNER JOIN accounts_user_deposit b ON a.id = b.user_id 
    WHERE a.age BETWEEN {target_age - 5} AND {target_age + 5}
    """
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(rows, columns=columns)

    top_deposits = df['deposit_id'].value_counts().nlargest(3).index.values.tolist()
    if not top_deposits:
        return []

    deposits_str = ','.join(map(str, top_deposits))
    Query_String = f"""
    SELECT fin_prdt_cd, fin_prdt_nm FROM banks_deposit 
    WHERE id IN ({deposits_str})
    """
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        result_df = pd.DataFrame(rows, columns=columns)

    result_list = result_df.to_dict(orient='records')
    return result_list

# 같은 은행에 있는 상품들 전체
def deposit_recommend_bank(target):
    Query_String = f"SELECT fin_prdt_cd, fin_prdt_nm FROM banks_deposit WHERE fin_co_no = '{target}';"
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(rows, columns=columns)

    result_list = df.to_dict(orient='records')
    return result_list

# 비슷한 자산 규모의 사람들이 가장 많이 가입한 3개
def deposit_recommend_balance(target):
    Query_String = f"""
    SELECT b.deposit_id FROM accounts_user a 
    INNER JOIN accounts_user_deposit b ON a.id = b.user_id 
    WHERE a.balance BETWEEN {target - 500000} AND {target + 500000}
    """
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(rows, columns=columns)

    top_deposits = df['deposit_id'].value_counts().nlargest(3).index.values.tolist()
    if not top_deposits:
        return []

    deposits_str = ','.join(map(str, top_deposits))
    Query_String = f"""
    SELECT fin_prdt_cd, fin_prdt_nm FROM banks_deposit 
    WHERE id IN ({deposits_str})
    """
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        result_df = pd.DataFrame(rows, columns=columns)

    result_list = result_df.to_dict(orient='records')
    return result_list

# 비슷한 연봉의 사람들이 가장 많이 가입한 3개
def deposit_recommend_income(target):
    Query_String = f"""
    SELECT b.deposit_id FROM accounts_user a 
    INNER JOIN accounts_user_deposit b ON a.id = b.user_id 
    WHERE a.income BETWEEN {target - 5000000} AND {target + 5000000}
    """
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(rows, columns=columns)

    top_deposits = df['deposit_id'].value_counts().nlargest(3).index.values.tolist()
    if not top_deposits:
        return []

    deposits_str = ','.join(map(str, top_deposits))
    Query_String = f"""
    SELECT fin_prdt_cd, fin_prdt_nm FROM banks_deposit 
    WHERE id IN ({deposits_str})
    """
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        result_df = pd.DataFrame(rows, columns=columns)

    result_list = result_df.to_dict(orient='records')
    return result_list

# 같은 타입인 사람들이 가장 많이 가입한 3개
def deposit_recommend_type(target):
    Query_String = f"""
    SELECT b.deposit_id FROM accounts_user a 
    INNER JOIN accounts_user_deposit b ON a.id = b.user_id 
    WHERE a.invest_type='{target}'
    """
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(rows, columns=columns)

    top_deposits = df['deposit_id'].value_counts().nlargest(3).index.values.tolist()
    if not top_deposits:
        return []

    deposits_str = ','.join(map(str, top_deposits))
    Query_String = f"""
    SELECT fin_prdt_cd, fin_prdt_nm FROM banks_deposit 
    WHERE id IN ({deposits_str})
    """
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        result_df = pd.DataFrame(rows, columns=columns)

    result_list = result_df.to_dict(orient='records')
    return result_list

# 적금
# 비슷한 나이(+5살)의 사람들이 가장 많이 가입한 3개
def saving_recommend_age(target_age):
    Query_String = f"""
    SELECT b.saving_id FROM accounts_user a 
    INNER JOIN accounts_user_saving b ON a.id = b.user_id 
    WHERE a.age BETWEEN {target_age - 5} AND {target_age + 5}
    """
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(rows, columns=columns)

    top_savings = df['saving_id'].value_counts().nlargest(3).index.values.tolist()
    if not top_savings:
        return []

    savings_str = ','.join(map(str, top_savings))
    Query_String = f"""
    SELECT fin_prdt_cd, fin_prdt_nm FROM banks_saving 
    WHERE id IN ({savings_str})
    """
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        result_df = pd.DataFrame(rows, columns=columns)

    result_list = result_df.to_dict(orient='records')
    return result_list

# 같은 은행에 있는 상품들 전체
def saving_recommend_bank(target):
    Query_String = f"SELECT fin_prdt_cd, fin_prdt_nm FROM banks_saving WHERE fin_co_no = '{target}';"
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(rows, columns=columns)

    result_list = df.to_dict(orient='records')
    return result_list

# 비슷한 자산 규모의 사람들이 가장 많이 가입한 3개
def saving_recommend_balance(target):
    Query_String = f"""
    SELECT b.saving_id FROM accounts_user a 
    INNER JOIN accounts_user_saving b ON a.id = b.user_id 
    WHERE a.balance BETWEEN {target - 500000} AND {target + 500000}
    """
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(rows, columns=columns)

    top_savings = df['saving_id'].value_counts().nlargest(3).index.values.tolist()
    if not top_savings:
        return []

    savings_str = ','.join(map(str, top_savings))
    Query_String = f"""
    SELECT fin_prdt_cd, fin_prdt_nm FROM banks_saving 
    WHERE id IN ({savings_str})
    """
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        result_df = pd.DataFrame(rows, columns=columns)

    result_list = result_df.to_dict(orient='records')
    return result_list

# 비슷한 연봉의 사람들이 가장 많이 가입한 3개
def saving_recommend_income(target):
    Query_String = f"""
    SELECT b.saving_id FROM accounts_user a 
    INNER JOIN accounts_user_saving b ON a.id = b.user_id 
    WHERE a.income BETWEEN {target - 5000000} AND {target + 5000000}
    """
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(rows, columns=columns)

    top_savings = df['saving_id'].value_counts().nlargest(3).index.values.tolist()
    if not top_savings:
        return []

    savings_str = ','.join(map(str, top_savings))
    Query_String = f"""
    SELECT fin_prdt_cd, fin_prdt_nm FROM banks_saving 
    WHERE id IN ({savings_str})
    """
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        result_df = pd.DataFrame(rows, columns=columns)

    result_list = result_df.to_dict(orient='records')
    return result_list

# 같은 타입인 사람들이 가장 많이 가입한 3개
def saving_recommend_type(target):
    Query_String = f"""
    SELECT b.saving_id FROM accounts_user a 
    INNER JOIN accounts_user_saving b ON a.id = b.user_id 
    WHERE a.invest_type='{target}'
    """
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(rows, columns=columns)

    top_savings = df['saving_id'].value_counts().nlargest(3).index.values.tolist()
    if not top_savings:
        return []

    savings_str = ','.join(map(str, top_savings))
    Query_String = f"""
    SELECT fin_prdt_cd, fin_prdt_nm FROM banks_saving 
    WHERE id IN ({savings_str})
    """
    with connection.cursor() as cursor:
        cursor.execute(Query_String)
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        result_df = pd.DataFrame(rows, columns=columns)

    result_list = result_df.to_dict(orient='records')
    return result_list

# Example usage
# print(deposit_recommend_age(30))
# print(deposit_recommend_bank('0010016'))
# print(deposit_recommend_balance(100000))
# print(deposit_recommend_income(50000000))
# print(deposit_recommend_type('성실'))

# print(saving_recommend_age(30))
# print(saving_recommend_bank('0010016'))
# print(saving_recommend_balance(100000))
# print(saving_recommend_income(50000000))
# print(saving_recommend_type('성실'))



from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from datetime import datetime, timedelta
import requests

from .serializers import DepositSerializer, DepositOptionsSerializers, SavingSerializer, SavingOptionsSerializers, ExchangeSerializer
from .models import Deposit, DepositOptions, Saving, SavingOptions, Exchange
from accounts.serializers import CustomUserSerializer
import logging

logger = logging.getLogger(__name__)
User = get_user_model()

BASE_URL='http://finlife.fss.or.kr/finlifeapi/'


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def deposit_list(request):
    if request.method == 'GET':
        URL = BASE_URL + 'depositProductsSearch.json'
        params = {
            'auth': settings.FIN_API_KEY,
            'topFinGrpNo': '020000',
            'pageNo': 1
        }
        response = requests.get(URL, params=params).json()
        baseList = response.get('result').get('baseList')
        optionList = response.get('result').get('optionList')
        for res in baseList:
            if Deposit.objects.filter(fin_prdt_cd=res.get('fin_prdt_cd')):
                continue
            save_data = {
                'fin_prdt_cd': res.get('fin_prdt_cd'),
                'fin_co_no': res.get('fin_co_no'),
                'kor_co_nm': res.get('kor_co_nm'),
                'fin_prdt_nm': res.get('fin_prdt_nm'),
                'etc_note': res.get('etc_note'),
                'join_deny': int(res.get('join_deny')),
                'join_member': res.get('join_member'),
                'join_way': res.get('join_way'),
                'spcl_cnd': res.get('spcl_cnd'),
                'mtrt_int': res.get('mtrt_int'),
            }
            serializers = DepositSerializer(data=save_data)
            if serializers.is_valid(raise_exception=True):
                serializers.save()
        for res in optionList:
            if DepositOptions.objects.filter(fin_prdt_cd=res.get('fin_prdt_cd'),save_trm=res.get('save_trm'), intr_rate_type_nm=res.get('intr_rate_type_nm')):
                continue
            save_data = {
                'fin_prdt_cd': res.get('fin_prdt_cd'),
                'intr_rate_type_nm': res.get('intr_rate_type_nm'),
                'intr_rate': float(res.get('intr_rate')) if res.get('intr_rate') != None else 999,
                'intr_rate2': float(res.get('intr_rate2')) if res.get('intr_rate2') != None else 999,
                'save_trm': int(res.get('save_trm')),
            }
            serializers = DepositOptionsSerializers(data=save_data)
            if serializers.is_valid(raise_exception=True):
                product = Deposit.objects.get(fin_prdt_cd=save_data['fin_prdt_cd'])
                serializers.save(deposit=product)
                
        deposits = Deposit.objects.all()
        serializer = DepositSerializer(deposits, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def deposit_option_list(request):
    if request.method == 'GET':
        options = DepositOptions.objects.all()
        seriarlizer = DepositOptionsSerializers(options, many=True)
        return Response(seriarlizer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_detail(request, fin_prdt_cd):
    if request.method == 'GET':
        deposit = Deposit.objects.get(fin_prdt_cd=fin_prdt_cd)
        serializer = DepositSerializer(deposit)
        return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_detail_option(request, fin_prdt_cd):
    if request.method == 'GET':
        options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
        serializer = DepositOptionsSerializers(options, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deposit_detail_join(request, fin_prdt_cd):
    user = User.objects.get(username=request.user)
    deposit = Deposit.objects.get(fin_prdt_cd=fin_prdt_cd)
    if request.method == "POST":
        user.deposit.add(deposit)
        my_dict = {'isJoined': True}
        return Response(my_dict)

@api_view(['GET'])
def saving_list(request):
    if request.method == 'GET':
        URL = BASE_URL + 'savingProductsSearch.json'
        params = {
            'auth': settings.FIN_API_KEY,
            'topFinGrpNo': '020000',
            'pageNo': 1
        }
        response = requests.get(URL, params=params).json()
        baseList = response.get('result').get('baseList')
        optionList = response.get('result').get('optionList')

        for res in baseList:
            if Saving.objects.filter(fin_prdt_cd=res.get('fin_prdt_cd')):
                continue
            save_data = {
                'fin_prdt_cd': res.get('fin_prdt_cd'),
                'fin_co_no': res.get('fin_co_no'),
                'kor_co_nm': res.get('kor_co_nm'),
                'fin_prdt_nm': res.get('fin_prdt_nm'),
                'etc_note': res.get('etc_note'),
                'join_deny': int(res.get('join_deny')),
                'join_member': res.get('join_member'),
                'join_way': res.get('join_way'),
                'spcl_cnd': res.get('spcl_cnd'),
                'mtrt_int': res.get('mtrt_int'),
            }
            serializers = SavingSerializer(data=save_data)
            if serializers.is_valid(raise_exception=True):
                serializers.save()

        for res in optionList:
            if SavingOptions.objects.filter(fin_prdt_cd=res.get('fin_prdt_cd'),save_trm=res.get('save_trm'), intr_rate_type_nm=res.get('intr_rate_type_nm'), rsrv_type_nm=res.get('rsrv_type_nm')):
                continue
            save_data = {
                'fin_prdt_cd': res.get('fin_prdt_cd'),
                'intr_rate_type_nm': res.get('intr_rate_type_nm'),
                'intr_rate': float(res.get('intr_rate')) if res.get('intr_rate') != None else 999,
                'intr_rate2': float(res.get('intr_rate2')) if res.get('intr_rate2') != None else 999,
                'save_trm': int(res.get('save_trm')),
                'rsrv_type_nm': res.get('rsrv_type_nm'),
            }
            serializers = SavingOptionsSerializers(data=save_data)
            if serializers.is_valid(raise_exception=True):
                product = Saving.objects.get(fin_prdt_cd=save_data['fin_prdt_cd'])
                serializers.save(saving=product)
                
        savings = Saving.objects.all()
        serializer = SavingSerializer(savings, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def saving_option_list(request):
    if request.method == 'GET':
        options = SavingOptions.objects.all()
        seriarlizer = SavingOptionsSerializers(options, many=True)
        return Response(seriarlizer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saving_detail(request, fin_prdt_cd):
    if request.method == 'GET':
        saving = Saving.objects.get(fin_prdt_cd=fin_prdt_cd)
        serializer = SavingSerializer(saving)
        return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saving_detail_option(request, fin_prdt_cd):
    if request.method == 'GET':
        options = SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
        serializer = SavingOptionsSerializers(options, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def saving_detail_join(request, fin_prdt_cd):
    user = User.objects.get(username=request.user)
    saving = Saving.objects.get(fin_prdt_cd=fin_prdt_cd)
    if request.method == "POST":
        user.saving.add(saving)
        my_dict = {'isJoined': True}
        return Response(my_dict)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def recommend(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'GET':
        user_serializer = CustomUserSerializer(user)
        age, favorite_bank, balance, income, type = user_serializer.data['age'], user_serializer.data['favorite_bank'], user_serializer.data['balance'], user_serializer.data['income'], user_serializer.data['invest_type']

        context = {
            'deposit': {
                'age': deposit_recommend_age(age) if age != None else None,
                'favorite_bank': deposit_recommend_bank(favorite_bank) if favorite_bank != None else None,
                'balance': deposit_recommend_balance(balance) if balance != None else None,
                'income': deposit_recommend_income(income) if income != None else None,
                'invest_type': deposit_recommend_type(type) if type != None else None
            },
            'saving' :{
                'age': saving_recommend_age(age) if age != None else None,
                'favorite_bank': saving_recommend_bank(favorite_bank) if favorite_bank != None else None,
                'balance': saving_recommend_balance(balance) if balance != None else None,
                'income': saving_recommend_income(income) if income != None else None,
                'invest_type': saving_recommend_type(type) if type != None else None
                },
            }
        
    return Response(context)

def get_previous_business_day(date):
    while True:
        date -= timedelta(days=1)
        if date.weekday() < 5:  # 주말 여부 확인
            return date

@api_view(['GET'])
def exchange(request):
    URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    date = datetime.now()

    if date.hour < 11:
        date = get_previous_business_day(date)

    while True:
        current_date = date.strftime('%Y%m%d')
        params = {
            'authkey': settings.EXCHANGE_API_KEY,
            'searchdate': current_date,
            'data': 'AP01'
        }
        response = requests.get(URL, params=params)
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and result:
                exchangeList = result
                for res in exchangeList:
                    if Exchange.objects.filter(cur_unit=res.get('cur_unit')).exists():
                        continue
                    save_data = {
                        'cur_unit': res.get('cur_unit'),
                        'cur_nm': res.get('cur_nm'),
                        'ttb': float(res.get('ttb').replace(',', '')),
                        'tts': float(res.get('tts').replace(',', '')),
                        'deal_bas_r': float(res.get('deal_bas_r').replace(',', '')),
                        'bkpr': res.get('bkpr'),
                        'yy_efee_r': res.get('yy_efee_r'),
                        'ten_dd_efee_r': res.get('ten_dd_efee_r'),
                        'kftc_deal_bas_r': res.get('kftc_deal_bas_r'),
                        'kftc_bkpr': res.get('kftc_bkpr'),
                        'date': datetime.strptime(current_date, '%Y%m%d')
                    }
                    serializer = ExchangeSerializer(data=save_data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()
                break
            else:
                date = get_previous_business_day(date)
        else:
            logger.error(f"Error fetching exchange rates: {response.status_code}")
            return Response({"error": "Failed to fetch exchange rates."}, status=response.status_code)

    exchanges = Exchange.objects.all()
    if not exchanges.exists():
        return Response({"message": "데이터가 존재하지 않습니다. 나중에 다시 시도해주세요."}, status=404)

    serializer = ExchangeSerializer(exchanges, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_local_exchange(request):
    try:
        latest_exchange = Exchange.objects.latest('date')
        serializer = ExchangeSerializer(latest_exchange)
        return Response(serializer.data)
    except Exchange.DoesNotExist:
        return Response({"error": "No exchange data found"}, status=404)

@api_view(['GET'])
def bank_list(request):
    banks = Deposit.objects.values_list('kor_co_nm', flat=True).distinct()
    return Response(banks)

# banks/views.py
@api_view(['GET'])
def deposit_options_detail(request, fin_prdt_cd):
    logger.debug(f"Request received for deposit options with fin_prdt_cd: {fin_prdt_cd}")
    try:
        options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
        if options.exists():
            serializer = DepositOptionsSerializers(options, many=True)
            return Response(serializer.data)
        logger.debug(f"No options found for fin_prdt_cd: {fin_prdt_cd}")
        return Response(status=404)
    except DepositOptions.DoesNotExist:
        logger.error(f"Deposit options for fin_prdt_cd: {fin_prdt_cd} does not exist")
        return Response(status=404)

@api_view(['GET'])
def saving_options_detail(request, fin_prdt_cd):
    logger.debug(f"Request received for saving options with fin_prdt_cd: {fin_prdt_cd}")
    try:
        options = SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
        if options.exists():
            serializer = SavingOptionsSerializers(options, many=True)
            return Response(serializer.data)
        logger.debug(f"No options found for fin_prdt_cd: {fin_prdt_cd}")
        return Response(status=404)
    except SavingOptions.DoesNotExist:
        logger.error(f"Saving options for fin_prdt_cd: {fin_prdt_cd} does not exist")
        return Response(status=404)