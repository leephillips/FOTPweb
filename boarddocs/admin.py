from models import Annualreport, Minutes, Agenda, Boardfile, LegalDoc, Historical, Picture, Budgetreport
from django.contrib import admin
from django.db import models
from django.forms import ModelForm, CharField, TextInput
# import os

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

class BudgetreportAdmin(BoardfileAdmin):
    list_display = ('name', 'whenUploaded', 'user', 'startDate', 'endDate')

class AnnualreportAdmin(BoardfileAdmin):
    list_display = ('name', 'whenUploaded', 'user', 'startDate', 'endDate')

class AgendaAdmin(BoardfileAdmin):
    list_display = ('name', 'whenUploaded', 'user', 'meetingDate')

class MinutesAdmin(BoardfileAdmin):
    list_display = ('name', 'whenUploaded', 'user', 'meetingDate')

class LegalDocAdmin(BoardfileAdmin):
    list_display = ('name', 'whenUploaded', 'user')

class HistoricalAdmin(BoardfileAdmin):
    list_display = ('name', 'whenUploaded', 'user')

class PictureAdmin(admin.ModelAdmin):
    list_display = ('pic', 'caption')
    list_display_links = ('pic',)

admin.site.register(Annualreport, AnnualreportAdmin)
admin.site.register(Minutes, MinutesAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Boardfile, BoardfileAdmin)
admin.site.register(Budgetreport, BudgetreportAdmin)
admin.site.register(LegalDoc, LegalDocAdmin)
admin.site.register(Picture, PictureAdmin)
