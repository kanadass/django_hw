from django.contrib import admin

from .models import Student, Teacher, TeacherStudent



# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Student)
admin.site.register(Teacher)
# admin.site.register(TeacherStudent)

class TeacherStudentInline(admin.TabularInline):
    model = TeacherStudent
    extra = 3
    # fields = ['']

class StudentAdmin(admin.ModelAdmin):
    inlines = [TeacherStudentInline]

admin.site.register(Student, StudentAdmin)