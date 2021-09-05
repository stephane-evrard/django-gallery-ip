from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length= 255, blank =False, null=False)
    active   = models.BooleanField(default=True)
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    @classmethod
    def get_location(cls):
        locations = cls.objects.all()
        return locations
    
    def __str__(self):
        return self.location
    
    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

class Category(models.Model):
    category = models.CharField(max_length=255, blank=False, null=False, unique=True)
    active   = models.BooleanField(default=True)
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
        
    @classmethod
    def get_category(cls):
        categories = cls.objects.all()
        return categories
    
    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images
    
    def __str__(self):
        return self.category
   
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
