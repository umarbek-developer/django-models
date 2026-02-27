from django.contrib import admin

from .models import Universitet, Teacher, Student, Company

admin.site.register(Universitet)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Company)

