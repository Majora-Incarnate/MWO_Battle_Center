from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	callsign = models.CharField(max_length=32)
	password = models.CharField(max_length=32)
	email = models.CharField(max_length=64)

	def __str__(self):
		return self.callsign

	def __unicode__(self):
		return self.callsign

class Code_Group(models.Model):
	name = models.CharField(max_length=16)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

class Code(models.Model):
	name = models.CharField(max_length=16)
	code_group = models.ForeignKey(Code_Group)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

class Map(models.Model):
	mode = models.ForeignKey(Code)
	name = models.CharField(max_length=32)
	picture = models.FileField(upload_to='map_screens/')

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

class Chassis(models.Model):
	name = models.CharField(max_length=16)
	weight = models.IntegerField()
	tech_base = models.ForeignKey(Code)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

class Variant(models.Model):
	chassis = models.ForeignKey(Chassis)
	name = models.CharField(max_length=16)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

class Specialization_Grade(models.Model):
	grade = models.IntegerField()

class Specialization(models.Model):
	user = models.ForeignKey(User)
	chassis = models.ForeignKey(Chassis)
	grade = models.ForeignKey(Specialization_Grade)

class Match(models.Model):
	team_one = models.CharField(max_length=32)
	team_two = models.CharField(max_length=32)
	tournament = models.CharField(max_length=32)
	season = models.IntegerField()
	week = models.IntegerField()

class Day(models.Model):
	match = models.ForeignKey(Match)
	date = models.DateTimeField()

class Drop(models.Model):
	day = models.ForeignKey(Day)
	map = models.ForeignKey(Map)
	max_tonnage = models.IntegerField()
	max_lights = models.IntegerField()
	max_mediums = models.IntegerField()
	max_heavies = models.IntegerField()
	max_assaults = models.IntegerField()
	max_clan = models.IntegerField()
	max_inner_sphere = models.IntegerField()
	max_duplicates = models.IntegerField()
	screenshot = models.FileField(upload_to='match_screens/')

class Dropdec(models.Model):
	drop = models.ForeignKey(Drop)
	comments = models.CharField(max_length=256)

class Dropslot(models.Model):
	dropdec = models.ForeignKey(Dropdec)
	pilot = models.ForeignKey(User)
	mech = models.ForeignKey(Variant)
	role = models.ForeignKey(Code)
	comments = models.CharField(max_length=256)

class Dropresult(models.Model):
	dropslot = models.ForeignKey(Dropslot)
	match_score = models.IntegerField()
	damage = models.IntegerField()
	assists = models.IntegerField()
	kills = models.IntegerField()
	deaths = models.IntegerField()

class Attendance(models.Model):
	user = models.ForeignKey(User)
	day = models.ForeignKey(Day)
	expected = models.IntegerField()
	actual = models.IntegerField()