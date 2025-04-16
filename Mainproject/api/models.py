from django.db import models

# Create your models here.
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(choices=(('IT','IT'),('Non IT','Non IT')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name




class Employee(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    address=models.TextField()
    phone=models.CharField(max_length=20)
    about=models.TextField()
    position=models.CharField(max_length=20,choices=(
        ('Manager','Manager'),
        ('Developer','Developer'),
        ('team leader','team leader')
    ))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)


    def __str__(self):
        return self.name