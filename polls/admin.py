from django.contrib import admin
from .models import Question,Answers,User


admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(User)

# Register your models here.
