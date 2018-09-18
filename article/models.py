from django.db import models
from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar ")
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    document = models.FileField(blank = True,null = True,verbose_name="Makaleye Fotoğraf Ekleyin",upload_to='documents/%Y/%m/%d/')
    def __str__(self):
        return self.title

