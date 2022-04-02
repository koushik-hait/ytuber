from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):

	def myphoto(self, object):
		return format_html('<img src="{}" width="30" />'.format(object.photo.url))

	list_display = ('id','first_name','myphoto','created_date')
	list_display_link = ('id','first_name')
	list_filter = ('role','created_date')
	search_fields = ('first_name','role')


# Register your models here.
admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)
