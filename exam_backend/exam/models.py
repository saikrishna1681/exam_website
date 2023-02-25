from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Exam(models.Model):

    name=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    starttime=models.DateTimeField(null=True)
    duration=models.IntegerField(default=120)
    no_of_questions=models.IntegerField(default=0)
    answer_key=models.TextField(default="",blank=True)
    students=models.ManyToManyField(User,blank=True,null=True)
    exam_result=models.TextField(default="",blank=True)
    marking_scheme=models.TextField(default="",blank=True)
    total_marks=models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}____{self.name}'


class Student_Response(models.Model):
    
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    student_response=models.TextField(default="",blank=True)
    student_marks=models.IntegerField(default=0)
    student_rank=models.IntegerField(default=0)
    is_submitted=models.BooleanField(default=False)


    def __str__(self):
        return f'{self.student.id}___{self.exam.name}'


class User_data(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    is_student=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}'


class Question(models.Model):

    question_number=models.IntegerField(default=0)
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    statement=models.TextField(default="",blank=True)
    positivemarks=models.PositiveIntegerField(default=0)
    negativemarks=models.PositiveIntegerField(default=0)
    answer=models.TextField(default="",blank=True)

    def __str__(self):
        return f'{self.question_number}___{self.exam.id}'

    

    
