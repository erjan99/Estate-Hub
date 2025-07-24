from django.db import models
from django.core.validators import MinValueValidator


class City(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"

class District(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='districts')

    def __str__(self):
        return f"{self.name}, {self.city.name}"

    class Meta:
        unique_together = ['name', 'city']

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent_category = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Categories')

    def __str__(self):
        ancestors = []
        category = self
        visited = set()

        while category and category.id not in visited:
            if category.id:
                visited.add(category.id)
            ancestors.append(category.name)
            category = category.parent_category

        return ' > '.join(reversed(ancestors))



    class Meta:
        verbose_name_plural = "Categories"

class Estate(models.Model):
    name = models.CharField(max_length=255)
    area = models.FloatField(validators=[MinValueValidator(0.0)])
    geo = models.CharField(max_length=255,)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    description = models.TextField()
    video = models.FileField(upload_to='media/video/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='estates')
    district = models.ForeignKey(District, on_delete=models.PROTECT, related_name='estates')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='estates')
    image = models.ImageField(upload_to='media/images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media/images/')

    def __str__(self):
        return f"Image {self.id} for {self.estate.name}"