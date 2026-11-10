from django.db import models
""" Abstarct Model """
# Create your models here.
class CommonInfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()
    
    class Meta:
        abstract = True
        
class Student(CommonInfo):
    fees = models.CharField()
    date = None
    
class Teacher(CommonInfo):
    fees = models.CharField()
    date = None
    
    
    """
        Multilevel Inharitance
    """
    
    class ExamCenter(models.Model):
        cname = models.CharField(max_length=200)
        city = models.CharField(max_length=200)
        
        
    class Student(ExamCenter):
        name = models.CharField(max_length=200)
        roll = models.IntegerField()
        
""" Abstarct Model """

class ExamCenter(models.Model):
    cname = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

class MyExamCeneter(ExamCenter):
    class Meta:
        proxy = True
        