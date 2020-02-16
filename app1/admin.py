from django.contrib import admin
from app1.models import Student,Track
# # Register your models here.
class CustomStudent(admin.ModelAdmin):
    fieldsets = (['Personal Info', {'fields': ['fname', 'lname', 'age']}],
		['Scholarship Info', {'fields': ['studentTrack']}])

    list_display = ['fname', 'lname', 'age', 'studentTrack',]
    list_filter=['fname','studentTrack']
    search_fields=['fname','studentTrack__trackName']



class InlineStudent(admin.StackedInline):
	model = Student
	extra = 3

class CustomTrack(admin.ModelAdmin):
	inlines = [InlineStudent]

admin.site.register(Student,CustomStudent)
admin.site.register(Track, CustomTrack)
