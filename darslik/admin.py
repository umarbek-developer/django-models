from django.contrib import admin

from .models import Universitet, Teacher, Student, Company, Group, StudentDavomat

admin.site.register(Universitet)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Group)
admin.site.register(StudentDavomat)

