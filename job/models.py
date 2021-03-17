from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

# title - location - job type - description - published at - Vacancy - salary - category - experience

job_option = (
    ('full time','full time'),
    ('part time','part time'),
)

def image_upload(instance, filename):
    imagename , extention = filename.split(".") 
    return "job/%s.%s"%(instance.id,extention)


class job (models.Model):
    owner = models.ForeignKey(User , related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50, choices=job_option)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now= True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('categorys', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(job,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class categorys (models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now= True)
    def __str__(self):
        return self.name  


class applayer(models.Model):
    job = models.ForeignKey(job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    site = models.URLField( max_length=200)
    cv = models.FileField(upload_to= '')
    cover_letter = models.TextField(max_length= 1000)

    def __str__(self):
        return self.name
