from django.db import models
class giachoi3(models.Model):
      tengoi=models.CharField(max_length=300)
      congnang=models.CharField(max_length=400)
      hieuqua=models.CharField(max_length=500)
