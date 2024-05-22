# make_data.py 파일은 랜덤한 더미 데이터를 만드는 예시 파일입니다.
# 반드시, 사용하는 필드를 확인한 후 본인의 프로젝트에 맞게 수정하여 진행해야 합니다.

# [참고] 현재 코드는 아래 User 모델을 기준으로 작성되어 있습니다.
"""
class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)
    income = models.IntegerField(blank=True, null=True)
    # 가입한 상품 목록 리스트를 ,로 구분된 문자열로 저장함
    financial_products = models.TextField(blank=True, null=True)

    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
"""


import random
import requests

first_name_samples = '김이박최정강조윤장임'
middle_name_samples = '민서예지도하주윤채현지'
last_name_samples = '준윤우원호후서연아은진'


def random_last_name():
    result = ''
    result += random.choice(first_name_samples)
    return result

def random_first_name():
    result = ''
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result + str(random.randint(1, 100))

# 현재 API 에 들어있는 금융 상품 코드 리스트 저장
# DP_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
# SP_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

# API_KEY = 'dcc9609fb012da993b8214401bb6c5ab'

# financial_products = []

# params = {
#     'auth': API_KEY,
#     # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
#     'topFinGrpNo': '020000',
#     'pageNo': 1,
# }

# # 정기예금 목록 저장
# response = requests.get(DP_URL, params=params).json()
# baseList = response.get('result').get('baseList')  # 상품 목록

# for product in baseList:
#     financial_products.append(product['fin_prdt_cd'])

# # 적금 목록 저장
# response = requests.get(SP_URL, params=params).json()
# baseList = response.get('result').get('baseList')  # 상품 목록

# for product in baseList:
#     financial_products.append(product['fin_prdt_cd'])
deposit = random.randint(1, 37)
saving = random.randint(1, 64)
banks = ["0010001",
"0010927",
"0011625",
"0010002",
"0010006",
"0013909",
"0013175",
"0015130",
"0017801",
"0010016",
"0010017",
"0010019",
"0010020",
"0014807"]
types = ['알뜰', '도전', '성실']

dict_keys = [
    'username',
    'age',
    'balance',
    'income',
    'first_name',
    'last_name'
]

# json 파일 만들기
import json
from collections import OrderedDict

file = OrderedDict()

username_first_list = [] #이름
username_last_list = [] #성
N = 10000
i = 0

while i < N:
    rn = random_first_name()
    if rn in username_first_list:
        continue

    username_first_list.append(rn)
    i += 1

j=0
while j < N:
    rn = random_last_name()

    username_last_list.append(rn)
    j += 1


# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = r'final_pjt_back\accounts\fixtures\accouts\user_data.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')

    for i in range(1, N+1):
        # 랜덤한 데이터를 삽입
        file['model'] = 'accounts.User'
        file['pk'] = i
        file['fields'] = {
            'username': f'user{i}',  # 유저 이름
            'first_name': username_first_list[i-1],
            'last_name': username_last_list[i-1],
            'age': random.randint(1, 100),  # 나이
            'balance': random.randrange(0, 100000000, 100000),  # 현재 가진 금액
            'income': random.randrange(0, 1500000000, 1000000),  # 연봉
            'password': '1234',
            'is_active': True,
            'is_staff': False,
            'is_superuser': False,
            'invest_type': types[random.randint(0, 2)],
            'favorite_bank': banks[random.randint(0, 13)]
        }

        json.dump(file, f, ensure_ascii=False, indent='\t')
        if i != N:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')


