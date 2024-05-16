from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404
from django.conf import settings
from django.http import JsonResponse

import requests

from .serializers import DepositSerializer, DepositOptionsSerializers, SavingSerializer, SavingOptionsSerializers
from .models import Deposit, Saving

BASE_URL='http://finlife.fss.or.kr/finlifeapi/'

@api_view(['GET'])
def save_deposit_products(request):
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
        save_data = {
            'fin_prdt_cd': res.get('fin_prdt_cd'),
            'kor_co_nm': res.get('kor_co_nm'),
            'fin_prdt_nm': res.get('fin_prdt_nm'),
            'etc_note': res.get('etc_note'),
            'join_deny': int(res.get('join_deny')),
            'join_member': res.get('join_member'),
            'join_way': res.get('join_way'),
            'spcl_cnd': res.get('spcl_cnd'),
            'mtrt_int': float(res.get('mtrt_int')),
            'max_limit': int(res.get('max_limit'))
        }
        serializers = DepositSerializer(data=save_data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()

    for res in optionList:
        save_data = {
            'fin_prdt_cd': res.get('fin_prdt_cd'),
            'intr_rate_type_nm': res.get('intr_rate_type_nm'),
            'intr_rate': float(res.get('intr_rate')),
            'intr_rate2': float(res.get('intr_rate2')),
            'save_trm': int(res.get('save_trm')),
        }
        serializers = DepositOptionsSerializers(data=save_data)
        if serializers.is_valid(raise_exception=True):
            product = Deposit.objects.get(fin_prdt_cd=save_data['fin_prdt_cd'])
            serializers.save(deposit=product)
            
    return Response(status=status.HTTP_201_CREATED)

@api_view(['GET'])
def save_saving_products(request):
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
        save_data = {
            'fin_prdt_cd': res.get('fin_prdt_cd'),
            'kor_co_nm': res.get('kor_co_nm'),
            'fin_prdt_nm': res.get('fin_prdt_nm'),
            'etc_note': res.get('etc_note'),
            'join_deny': int(res.get('join_deny')),
            'join_member': res.get('join_member'),
            'join_way': res.get('join_way'),
            'spcl_cnd': res.get('spcl_cnd'),
            'mtrt_int': float(res.get('mtrt_int')),
            'max_limit': int(res.get('max_limit'))
        }
        serializers = SavingSerializer(data=save_data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()

    for res in optionList:
        save_data = {
            'fin_prdt_cd': res.get('fin_prdt_cd'),
            'intr_rate_type_nm': res.get('intr_rate_type_nm'),
            'intr_rate': float(res.get('intr_rate')),
            'intr_rate2': float(res.get('intr_rate2')),
            'save_trm': int(res.get('save_trm')),
            'rsrv_type_nm': res.get('rsrv_type_nm'),
        }
        serializers = SavingOptionsSerializers(data=save_data)
        if serializers.is_valid(raise_exception=True):
            product = Saving.objects.get(fin_prdt_cd=save_data['fin_prdt_cd'])
            serializers.save(saving=product)
            
    return Response(status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_list(request):
    return

def deposit_detail(request, fin_prdt_cd):
    return

def saving_list(request):
    return

def saving_detail(request, fin_prdt_cd):
    return