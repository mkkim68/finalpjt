from django.db import models

# 예금
class Deposit(models.Model):
    kor_co_nm = models.TextField()  # 금융회사 명
    fin_co_no = models.TextField()  # 금융회사 코드
    fin_prdt_cd = models.TextField(unique=True)  # 금융상품 코드
    fin_prdt_nm = models.TextField()  # 금융 상품명
    join_way = models.TextField()  # 가입 방법
    mtrt_int = models.TextField()  # 만기 후 이자율
    spcl_cnd = models.TextField()  # 우대 조건
    join_deny = models.IntegerField()  # 가입제한 (1: 없음, 2:서민전용, 3:일부제한)
    join_member = models.TextField()  # 가입 대상
    etc_note = models.TextField()  # 기타 유의사항

# 예금 옵션
class DepositOptions(models.Model):
    deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)  # 저축 금리 유형명
    intr_rate = models.FloatField()  # 저축 금리 (소수점 2자리)
    intr_rate2 = models.FloatField()  # 최고 우대 금리 (소수점 2자리)
    save_trm = models.IntegerField()  # 저축 기간 (개월)


# 적금
class Saving(models.Model):
    kor_co_nm = models.TextField()  # 금융회사 명
    fin_co_no = models.TextField()  # 금융회사 코드
    fin_prdt_cd = models.TextField(unique=True)  # 금융상품 코드
    fin_prdt_nm = models.TextField()  # 금융 상품명
    join_way = models.TextField()  # 가입 방법
    mtrt_int = models.TextField()  # 만기 후 이자율
    spcl_cnd = models.TextField()  # 우대 조건
    join_deny = models.IntegerField()  # 가입제한 (1: 없음, 2:서민전용, 3:일부제한)
    join_member = models.TextField()  # 가입 대상
    etc_note = models.TextField()  # 기타 유의사항

# 적금 옵션
class SavingOptions(models.Model):
    saving = models.ForeignKey(Saving, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    save_trm = models.IntegerField()  # 저축 기간 (개월)
    intr_rate = models.FloatField()  # 저축 금리 (소수점 2자리)
    intr_rate2 = models.FloatField()  # 최고 우대 금리 (소수점 2자리)
    intr_rate_type_nm = models.TextField()  # 저축 금리 유형명
    rsrv_type_nm = models.TextField()  # 적립 유형명

# 환율
class Exchange(models.Model):
    cur_unit = models.CharField(max_length=10) # 통화코드
    cur_nm = models.CharField(max_length=50) # 통화명
    ttb = models.FloatField() # 송금 받을 때
    tts = models.FloatField() # 송금 보낼 때
    deal_bas_r = models.FloatField() # 매매기준율
    date = models.DateField(auto_now_add=True)