from django_resized import ResizedImageField
from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    telephone = models.CharField(max_length=10,null=True,blank=True)
    image = ResizedImageField(size=[500,300],quality=85,keep_meta=True,upload_to='images/%Y/%m/%d/',default=None,null=True,blank=True)
   
    def __str__(self):
        return self.name +" "+self.surname

class Webpage(models.Model):
    url = models.URLField()
    person = models.ForeignKey(Person,null=True,blank=True,on_delete=models.CASCADE,related_name='websites')
    
    def __str__(self):
        return self.url

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    person = models.ForeignKey(Person, default=None,on_delete=models.CASCADE,null=True,blank=True,related_name='notes')
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Place(models.Model):
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=7)
    city = models.ForeignKey(City,on_delete=models.PROTECT,related_name='places')
    description = models.TextField()
    persons = models.ManyToManyField(Person, default=None,blank=True,related_name='places')

    def __str__(self):
        owner = self.persons.all().first()
        if owner:
            return f"{self.city.name} {self.street} {self.number} - {owner.name} {owner.surname}"
        else:
            return f"{self.city.name} {self.street} {self.number}"

    

class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    fuel = models.CharField(max_length=3)
    year = models.CharField(max_length=9)
    plate = models.CharField(max_length=10)
    owner = models.ForeignKey(Person,default=None,on_delete=models.PROTECT,null=True,blank=True,related_name='vehicles')

    def __str__(self):
        return f"{self.brand} {self.model} {self.plate}"

class File(models.Model):
    file = models.FileField(upload_to='files/%Y/%m/%d/')
    person = models.ForeignKey(Person,on_delete=models.PROTECT,related_name='files')

    def __str__(self):
        return f"{self.file}"

