from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100);
    photo = models.ImageField(upload_to='blog_images/')
    text = models.TextField();
    date = models.DateField(auto_now_add=True);

    def __str__(self):
        return self.title


