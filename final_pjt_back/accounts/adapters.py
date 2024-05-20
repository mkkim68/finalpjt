# adapters.py

from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        user = super().save_user(request, user, form, False)
        # 추가 저장 필드: profile_image
        income = data.get('income')
        if income:
            user.income = income
        balance = data.get('balance')
        if balance:
            user.balance = balance
        age = data.get('age')
        if age:
            user.age = age
        favorite_bank = data.get('favorite_bank')
        if favorite_bank:
            user.favorite_bank = favorite_bank
        invest_type = data.get('invest_type')
        if invest_type:
            user.invest_type = invest_type

        user.save()
        return user