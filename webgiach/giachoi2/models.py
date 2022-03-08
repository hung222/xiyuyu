from django.db import models
class giachoi2(models.Model):
     tengoi=models.CharField(max_length=500)
     congdung=models.CharField(max_length=400)
     chuatri=models.CharField(max_length=300)  
