from django.db import models

# 예금
class Deposit(models.Model):
    dcls_month = models.DateField()  # 공시 제출월
    fin_co_no = models.TextField()  # 금융회사 코드
    kor_co_nm = models.TextField()  # 금융회사 명
    fin_prdt_cd = models.TextField()  # 금융상품 코드
    fin_prdt_nm = models.TextField()  # 금융 상품명
    join_way = models.TextField()  # 가입 방법
    mtrt_int = models.FloatField()  # 만기 후 이자율
    spcl_cnd = models.TextField()  # 우대 조건
    join_deny = models.TextField()  # 가입제한 (1: 없음, 2:서민전용, 3:일부제한)
    join_member = models.TextField()  # 가입 대상
    etc_note = models.TextField()  # 기타 유의사항
    max_limit = models.IntegerField()  # 최고한도
    save_trm = models.IntegerField()  # 저축 기간 (개월)
    intr_rate = models.FloatField()  # 저축 금리 (소수점 2자리)
    intr_rate2 = models.FloatField()  # 최고 우대 금리 (소수점 2자리)
    intr_rate_type_nm = models.TextField()  # 저축 금리 유형명

# 적금
class Saving(models.Model):
    dcls_month = models.DateField()  # 공시 제출월
    fin_co_no = models.TextField()  # 금융회사 코드
    kor_co_nm = models.TextField()  # 금융회사 명
    fin_prdt_cd = models.TextField()  # 금융상품 코드
    fin_prdt_nm = models.TextField()  # 금융 상품명
    join_way = models.TextField()  # 가입 방법
    mtrt_int = models.FloatField()  # 만기 후 이자율
    spcl_cnd = models.TextField()  # 우대 조건
    join_deny = models.TextField()  # 가입제한 (1: 없음, 2:서민전용, 3:일부제한)
    join_member = models.TextField()  # 가입 대상
    etc_note = models.TextField()  # 기타 유의사항
    max_limit = models.IntegerField()  # 최고한도
    save_trm = models.IntegerField()  # 저축 기간 (개월)
    intr_rate = models.FloatField()  # 저축 금리 (소수점 2자리)
    intr_rate2 = models.FloatField()  # 최고 우대 금리 (소수점 2자리)
    intr_rate_type_nm = models.TextField()  # 저축 금리 유형명
    rsrv_type_nm = models.TextField()  # 적립 유형명