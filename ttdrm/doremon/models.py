from django.db import models
class drm(models.Model):
       tennv = models.CharField(max_length=800)
       theloai = models.CharField(max_length=1200)
       congnang = models.CharField(max_length=1500)
def __str__(self):
        return self.tinnhan 
def __str__(self):
        return self.st 
def nbt(self, *args, **kwargs): #3
        self.slug = slugify(self.name) #4
        if self.parent_category_id is not None: #5
            Categories.objects.filter(parent_category=self.id).update(parent_category=None)
def nbtt(self, *args, **kwargs): #3
        self.slug = slugify(self.name) #4
        if self.parent_category_id is not None: #5
            Categories.objects.filter(parent_category=self.id).update(parent_category=None)
      
       
       



