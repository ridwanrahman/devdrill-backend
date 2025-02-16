from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Category, Question, UserQuestion

admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(UserQuestion)
