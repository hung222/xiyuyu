from django.db import models
class giachoi(models.Model):
       tengoi=models.CharField(max_length=300)
       chucnamg=models.CharField(max_length=400)
       khanang=models.CharField(max_length=500)
       chongchidinh=models.CharField(max_length=600)
