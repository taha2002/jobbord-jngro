from django.db import models

# Create your models here.

# title - location - job type - description - published at - Vacancy - salary - category - experience

job_option = (
    ('full time','full time'),
    ('part time','part time'),
)

class job (models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50, choices=job_option)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now= True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('categorys', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class categorys (models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now= True)
    def __str__(self):
        return self.name   





