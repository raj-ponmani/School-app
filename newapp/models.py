from django.db import models

# Create your models here.

class destination(models.Model):
    CITY_CHOICES = [
        ('ND', 'NEW DELHI'),
        ('MI', 'MUMBAI'),
        ('GA', 'GOA'),
        ('TN', 'TAMILNADU'),
        ('KL', 'KERALA')
    ]
    COURSE_CHOICES = [
        ('PS','PLAY SCHOOL'),
        ('PG','PRE-KG'),
        ('FS','FIRST STANDARD'),
    ]
    GENDER_CHOICE = [
        ('MALE','male'),
        ('FEMALE','female'),
        ('OTHERS','others'),
    ]

    Student_Name = models.CharField(max_length=100)
    Father_Name = models.CharField(max_length=100)
    Postal_address = models.TextField()
    Personal_Address = models.TextField()
    Sex = models.CharField(max_length=10,choices=(('male',u'male'), ('famale',u'female')),default='male')
    City = models.CharField(max_length=225,choices=CITY_CHOICES)
    Course = models.CharField(max_length=225,choices=COURSE_CHOICES)
    Pincode = models.IntegerField()
    EmailID = models.EmailField()
    DOB = models.DateField()
    MobileNO = models.CharField(max_length=10)