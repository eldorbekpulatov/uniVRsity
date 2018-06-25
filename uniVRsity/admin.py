from django.contrib import admin
from .models import Team, Member

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
	list_display = ['name',]
	list_display_links = ['name']
	search_fields = ['name'] 
	list_filter = ["name"]
	class Meta:
		team=Team
admin.site.register(Team, TeamAdmin)


class MemberAdmin(admin.ModelAdmin):
	list_display = ["firstName", "lastName"]
	list_display_links = ["firstName", "lastName"]
	list_filter = ['partOf']
	search_fields = ["firstName", "lastName", 'email', 'position']
	class Meta:
		member=Member
admin.site.register(Member, MemberAdmin)

