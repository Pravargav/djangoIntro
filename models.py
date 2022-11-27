
from django.db import models
import datetime
from django.utils import timezone

class Student_registration(models.Model):
    student_name = models.CharField(max_length=224)
    student_date_of_birth = models.CharField(max_length=224)
    student_date_of_registration=models.DateTimeField('date_of_registration')
    student_sex=models.CharField(max_length=224)
    student_aadhaar_num=models.BigIntegerField()
    student_email_id=models.EmailField(max_length=224)
    

    def __str__(self):
        return f'{self.student_name},{self.student_date_of_birth},{self.student_date_of_registration},{self.student_sex},{self.student_aadhaar_num},{self.student_email_id}'

    def recently_registered(self):
        return self.student_date_of_registration >= timezone.now() - datetime.timedelta(days=27)  

class School(models.Model):
    student=models.ForeignKey(Student_registration, on_delete=models.CASCADE)
    school_name=models.CharField(max_length=224)
    courses=models.CharField(max_length=224)
    output=models.CharField(max_length=224)
    choices = models.IntegerField(default=0)


