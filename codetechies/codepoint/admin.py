from django.contrib import admin

# Register your models here.
from .models import *


class videos_info(admin.TabularInline):
    model = Course_Information


class course_info(admin.ModelAdmin):
    inlines = [videos_info]


admin.site.register(Course_Category, course_info)
admin.site.register(Course_Information, )

admin.site.register(testing)
