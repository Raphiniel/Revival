from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Description(models.Model):
    name = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

class Blog(models.Model):
    content = models.TextField()
    