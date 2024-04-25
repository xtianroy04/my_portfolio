from django.utils import timezone
from django.db import models

class Information(models.Model):
    image = models.ImageField(upload_to='My_Images/', verbose_name="User Image", null=True, blank=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    expertise = models.CharField(max_length=30)
    description = models.TextField(verbose_name="Description",  blank=True, null=True)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Hobby(models.Model):
    hobby_image = models.ImageField(upload_to='hobby_image/', verbose_name="hobby Image", null=True, blank=True)
    hobby_name = models.CharField(max_length=25, verbose_name="hobby_name")
    hobby_description = models.TextField(verbose_name="hobby_description")

    def __str__(self):
        return self.hobby_name

class Education(models.Model):
    education_name = models.CharField(max_length=50, verbose_name="Education Name")
    year =  models.CharField(max_length=20, verbose_name="Year")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return f"{self.education_name} {self.year}"

class Skill(models.Model):
    skill_name = models.CharField(max_length=20, verbose_name="Skill Name")
    percent = models.IntegerField()

    def __str__(self):
        return f"{self.skill_name}"
    
class Project(models.Model):
    project_img = models.ImageField(upload_to='project_image/', verbose_name="Project Image", null=True, blank=True)
    project_name = models.CharField(max_length=250, verbose_name="Project Name")
    description = models.TextField(verbose_name="Description")
    category = models.ManyToManyField('Category', related_name="category", blank=True)
    link = models.CharField(max_length=500, verbose_name="Link", null=True, blank=True)

    def __str__(self):
        return f"{self.project_name}"
    
class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name="Category")
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.category_name}"
    
class Client(models.Model):
    client_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='client_images/')
    date = models.DateField()
    link = models.URLField()

    def __str__(self):
        return self.client_name