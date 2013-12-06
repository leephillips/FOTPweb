from models import Annualreport, Minutes, Agenda
from django.contrib import admin
from django.db import models
from django.forms import ModelForm, CharField, TextInput

class BoardfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'whenUploaded', 'user')
    list_display_links = ('name',)
    readonly_fields = ['whenUploaded', 'name'] 
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            self.user = request.user.id
            kwargs['initial'] = self.user
            return db_field.formfield(**kwargs)
        return super(BoardfileAdmin, self).formfield_for_foreignkey(
                     db_field, request, **kwargs)


class AnnualreportAdmin(BoardfileAdmin):
    list_display = ('name', 'whenUploaded', 'user', 'startDate', 'endDate')

class AgendaAdmin(BoardfileAdmin):
    list_display = ('name', 'whenUploaded', 'user', 'meetingDate')

class MinutesAdmin(BoardfileAdmin):
    list_display = ('name', 'whenUploaded', 'user', 'meetingDate')

admin.site.register(Annualreport, AnnualreportAdmin)
admin.site.register(Minutes, MinutesAdmin)
admin.site.register(Agenda, AgendaAdmin)
