from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=40, null=False)
    isHolder = models.BooleanField()
    isSeeker = models.BooleanField()
    companyName = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username


class SkillCategory(models.Model):
    skillName = models.CharField(max_length=30, primary_key=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.skillName


class SkillDescription(models.Model):
    skillCategory = models.ForeignKey(SkillCategory, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.skillCategory.skillName


class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    category = models.ForeignKey(SkillCategory, blank=False, on_delete=models.CASCADE)
    requirements = ArrayField(
         ArrayField(
             models.CharField(max_length=30, blank=True),
         ),
     )

    def __str__(self):
        return self.title