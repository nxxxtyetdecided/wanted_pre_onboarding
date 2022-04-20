import datetime

from django.db import models
from django.utils.timezone import now

from user.models import User


class Product(models.Model):
    title = models.CharField( max_length=150, verbose_name='상품명')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='게시자명')
    cnt = models.IntegerField(default=0, verbose_name='펀딩 수')
    desc = models.TextField(verbose_name='상품 설명')
    goal = models.IntegerField(verbose_name='목표 금액')
    end_date = models.DateTimeField(verbose_name='펀딩 종료일')
    charge = models.IntegerField(verbose_name='1회 펀딩금액')
    total = models.IntegerField(default=0, verbose_name='총 펀딩금액')
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.title

    # d-day
    def d_day(self):
        return (self.end_date.date() - now().date()).days

    # 달성률
    def achievement(self):
        return str(int(self.total / self.goal * 100))+'%'


class Funding(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
