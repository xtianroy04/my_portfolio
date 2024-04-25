from django.contrib import admin
from app.models import *

class InformationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name','last_name']

class HobbyAdmin(admin.ModelAdmin):
    list_display = ['hobby_name', 'hobby_description']

class EducationAdmin(admin.ModelAdmin):
    list_display = ['education_name', 'year']

class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill_name', 'percent']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'description']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'created_at']

class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'date']

admin.site.register(Client, ClientAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Hobby, HobbyAdmin)
admin.site.register(Information, InformationAdmin)