from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	pilot_name = models.CharField(max_length=32)
	password = models.CharField(max_length=32)
	email = models.CharField(max_length=64)

class Match(models.Model):
	team_one = models.CharField(max_length=32)
	team_two = models.CharField(max_length=32)
	tournament = models.CharField(max_length=32)
	season = models.NumberField()

class Drop(models.Model):
	match = models.ForeignKey(Match)
	drop_map = models.CharField(max_length=32)
	max_tonnage = models.NumberField()
	max_lights = models.NumberField()
	max_mediums = models.NumberField()
	max_heavies = models.NumberField()
	max_assaults = models.NumberField()
	max_clan = models.NumberField()
	max_inner_sphere = models.NumberField()
	comments = models.CharField(max_length=256)

class Attendance(models.Model):
	user = models.ForeignKey(User)
	match = models.ForeignKey(Match)
	expected = models.NumberField()
	actual = models.NumberField()

class Chassis(models.Model):
	name = models.CharField(max_length=16)
	weight = models.NumberField()
	tech_base = models.NumberField()

class Variant(models.Model):
	name = models.CharField(max_length=8)

class Specialization(models.Model):
	user = models.ForeignKey(User)
	chassis = models.ForeignKey(Chassis)
	tech_base = models.NumberField()