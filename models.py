from django.db import models

class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    principal = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField()
    guardian_name = models.CharField(max_length=200)
    guardian_phone_number = models.CharField(max_length=15)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    
    def __str__(self):
        return self.name
