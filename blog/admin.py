from django.contrib import admin
from .models import Post, Comment

# Register your models here. (regs them in the /admin menu)
admin.site.register(Post)
admin.site.register(Comment)
