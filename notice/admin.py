from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):

    class Meta:
       model = Notice