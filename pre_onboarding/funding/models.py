from django.db import models

from user.models import User


class Product(models.Model):
    title = models.CharField('상품명', max_length=150)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.TextField()
    goal = models.DecimalField(max_digits=12, decimal_places=0)
    end_date = models.DateTimeField()
    charge = models.DecimalField(max_digits=6, decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True, null=False)


class Funding(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
