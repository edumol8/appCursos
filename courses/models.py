from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.title
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course, related_name='Students')

    def __str__(self):
        return self.name