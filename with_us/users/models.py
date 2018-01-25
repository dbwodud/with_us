from django.db import models
from django.forms import ModelForm

# Create your models here.
class User(models.Model):
    Man = 'M'
    Woman = 'W'
    GENDER_CHOICES=(
    (Man, 'M'),
    (Woman, 'W'),
    )
    
    user_no = models.AutoField(primary_key=True)
    user_email = models.EmailField(max_length=254)
    user_pw = models.CharField(max_length=50)
    user_gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=Man,
    )
    user_birthday = models.DateField(blank=True)
    user_jdate = models.DateTimeField(auto_now_add=True)

    def is_upperclass(self):
        return self.user_gender in (self.Man, self.Woman)
