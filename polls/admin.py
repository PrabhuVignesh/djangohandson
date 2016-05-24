from django.contrib import admin
from .models import Question,Answers,User,Post,Likes,Comments


admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Comments)


# Register your models here.
