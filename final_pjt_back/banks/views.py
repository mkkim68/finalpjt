from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from datetime import datetime, timedelta
import requests

from .serializers import DepositSerializer, DepositOptionsSerializers, SavingSerializer, SavingOptionsSerializers, ExchangeSerializer
from .models import Deposit, DepositOptions, Saving, SavingOptions, Exchange
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