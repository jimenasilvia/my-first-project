from __future__ import unicode_literals

from django.db import models

# Create your models here.

"""class Rol (models.Model):
	rol=models.CharField()
	
class User(models.Model):
	User=models.CharField()
	password=models.CharField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)


class Admin(models.Model):
	user=models.CharField()
	dni=models.CharField()
	name=models.CharField()
	firstname=models.CharField()
	lastname}=models.CharField()
	email=models.EmailField()
	telephone=models.CharField()
	direction=models.CharField()

class Customer(models.Model):
	user=models.CharField()
	dni=models.CharField()
	name=models.CharField()
	firstname=models.CharField()
	lastname}=models.CharField()
	email=models.EmailField()
	telephone=models.CharField()

class Type_room(models.Model):
	name_type=models.CharField()
	description=models.TextField()
class Room(models.Model):
	nro_room=models.CharField()
	name_type=models.ForeignKey(Type_Room)
	is_reserved=models.BooleanField()
class Rating(models.Model):
	description=models.TextField()
class Room_rating(models.Model)
     



class Booking(models.Model):
    admin=models.ForeignKey(Admin)
    customer=models.ForeignKey(Customer)
    room=models.ForeignKey(Room)
    in_date=models.DateTimeField()
    out_date=models.DateTimeField()

class Rent(models.Model):
    name_type=models.ForeignKey(Type_Room)
    amount=models.DecimalField()
    from_date=models.DateTimeField()
    to_date=models.DateTimeField()
    is_active=models.BooleanField()


"""


	

