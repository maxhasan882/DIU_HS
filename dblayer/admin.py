from django.contrib import admin
from .models import (
    SkillCategory,Post,UserInfo,SkillDescription
)
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(SkillCategory)
admin.site.register(SkillDescription)
admin.site.register(Post)