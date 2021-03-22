from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    location = models.ForeignKey('location',on_delete = models.CASCADE)
    category = models.ForeignKey('category',on_delete = models.CASCADE)

    @classmethod
    def images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        return images

    @classmethod
    def filter_by_location(cls,location):
        images = cls.objects.filter(location__name__icontains=location)
        return images

    @classmethod
    def get_image_by_id(cls,id):
        image_id = cls.objects.get(id = id)
        return image_id

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length =30)

    def save_category(self):
        self.save()

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length =30)

    @classmethod
    def location(cls):
        location = cls.objects.all()
        return location

    def save_location(self):
        self.save()

    def __str__(self):
        return self.name