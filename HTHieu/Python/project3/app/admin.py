from django.contrib import admin
# Register your models here.
from app.models import User, Directory, Path

admin.site.register(User)
admin.site.register(Directory)
admin.site.register(Path)