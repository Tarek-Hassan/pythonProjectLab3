from django.db import models

# Create your models here.
class Track(models.Model):
    trackName=models.CharField(max_length=30)
    def __str__(self):
        return self.trackName
        
class Student(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    age=models.IntegerField()
    studentTrack = models.ForeignKey(Track, on_delete=models.DO_NOTHING)



	# def is_adult(self):
	# 	if self.age >18:
	# 		return True
	# 	else:
	# 		return False
	# is_adult.boolean = True
	# is_adult.short_description = 'Adult Student'