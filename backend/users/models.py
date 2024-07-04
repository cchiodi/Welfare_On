from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	GENDER_CHOICES = [
		('M', 'Male'),
		('F', 'Female'),
		('O', 'Other'),
	]

	MARITAL_STATUS_CHOICES = [
		('S', 'Single'),
		('M', 'Married'),
		('D', 'Divorced'),
		('W', 'Widowed'),
	]

	role = models.CharField(max_length=50, default='user')
	name_last_name = models.CharField(max_length=255, blank=True, null=True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	birthdate = models.DateField(blank=True, null=True)
	workplace = models.CharField(max_length=255, blank=True, null=True)
	phone_number = models.CharField(max_length=20)
	marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
	has_children = models.BooleanField(default=False)
	has_elders = models.BooleanField(default=False)
	interests = models.ManyToManyField('interests.Interest', related_name='users', blank=True)

	def save(self, *args, **kwargs):
		self.name_last_name = f"{self.first_name}.{self.last_name}"
		super().save(*args, **kwargs)

	def __str__(self):
		return f"{self.name_last_name} ({self.username})"


User = get_user_model()
User.services = models.ManyToManyField('services.Service', through='services.UserService', related_name='users', blank=True)


class Log(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	event = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.timestamp} - {self.event} - {self.user}"
