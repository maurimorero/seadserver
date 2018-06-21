# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Provincia(models.Model):
	name = models.CharField(max_length=400)

	def __str__(self):
		return (self.name)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organizacion = models.CharField(max_length=200, default='')
    email = models.EmailField(default='')
    nombre = models.CharField(max_length=200, default='')
    puesto = models.CharField(max_length=200, default='')
    provincia = models.ForeignKey(Provincia,default=1, null=True)
    localidad= models.CharField(max_length=200, null=True, blank=True, default='')
    direccion = models.CharField(max_length=500,null=True, blank=True, default='')
    telefono = models.CharField(max_length=50, default='')

    def __str__(self):
        return (self.user.username)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
