from __future__ import unicode_literals

from django.db import models

from django.conf import settings


# Create your models here.
class Customer(models.Model):
	dni=models.CharField(max_length=8)
	name=models.CharField(max_length=50)
	firstname=models.CharField(max_length=30)
	lastname=models.CharField(max_length=30)
	email=models.EmailField(max_length=256)
	telephone=models.CharField(max_length=15,blank=True)

	def __unicode__(self):
		 return '%s (%s %s)' % (self.dni, self.name,self.firstname)

class Room_type(models.Model):
	name_type=models.CharField('Room Type',max_length=15)
	description=models.TextField(blank=True)

	def __unicode__(self):
		return self.name_type

class Pay_type(models.Model):
	pay_type=models.CharField(max_length=12)

	def __unicode__(self):
		return self.pay_type

class Rating(models.Model):
	description=models.TextField()

	def __unicode__(self):
		return self.description

class Rent(models.Model):
    name_type=models.ForeignKey(Room_type,verbose_name='Room Type')
    amount=models.DecimalField(max_digits=6, decimal_places=3)
    from_date=models.DateTimeField()
    to_date=models.DateTimeField()
    is_active=models.BooleanField()

    def __unicode__(self):
		return '%s' % (self.name_type)


class Booking(models.Model):
    admin=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,default=1)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    in_date=models.DateTimeField()
    out_date=models.DateTimeField()
    reservation_date=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s (%s)' % (self.customer, self.admin)


class Room(models.Model):
	nro_room=models.CharField(max_length=3)
	name_type=models.ForeignKey(Room_type,verbose_name='Room Type')
	is_reserved=models.BooleanField()
	booking=models.ForeignKey(Booking,blank=True,null=True,on_delete=models.DO_NOTHING)


	def __unicode__(self):
		return self.nro_room


class Room_rating(models.Model):
     room=models.ForeignKey(Room,verbose_name='Room',default=1)
     rating=models.ForeignKey(Rating,blank=True,null=True,on_delete=models.DO_NOTHING)
     from_date=models.DateTimeField()
     to_date=models.DateTimeField()
     is_active=models.BooleanField()

class Bill(models.Model):
	booking=models.ForeignKey(Booking)
	rent=models.ForeignKey(Rent)
	total=models.DecimalField(max_digits=9,decimal_places=2)

	def __unicode__(self):
		return '%s' % (self.booking)

class Bill_payment(models.Model):
	bill=models.ForeignKey(Bill,blank=True,null=True,on_delete=models.DO_NOTHING)
	pay_type=models.ForeignKey(Pay_type,blank=True,null=True,on_delete=models.DO_NOTHING)
	payment_date=models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return '%s' % (self.bill)
