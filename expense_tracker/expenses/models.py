from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.CharField(
        max_length=50,
        choices= [
        ('FOOD', 'Food'),
        ('TRANS', 'Transportation'),
        ('HOUS', 'Housing'),
        ('UTIL', 'Utilities'),
        ('OTHER', 'Other'),
        ],
        default= 'OTHER'
    )

    date = models.DateField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.amount}"

