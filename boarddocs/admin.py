from models import Annualreport, Minutes
from django.contrib import admin
from django.db import models
from django.forms import ModelForm, CharField, TextInput

class AnnualreportAdmin(admin.ModelAdmin):
    list_display = ('docname', 'pub_date')
    list_display_links = ('title',)
    readonly_fields = ['pub_date'] 
    # form = PostAdminForm
    def get_form(self, req, obj=None, **kwargs):
        # save the logged in user 
        self.current_user = req.user
        return super(PostAdmin, self).get_form(req, obj, **kwargs)
    # http://www.vimtips.org/2009/04/28/django-using-modeladmin-default-currently-logged-u/
    def formfield_for_dbfield(self, db_field, **kwargs):
       if db_field.name == "byline":
          byline = Director.objects.get(user=self.current_user).nameinbyline
          # return CharField(
          return db_field.formfield(
                           initial = byline,
                           max_length = 500, 
                           widget=TextInput(attrs={'size':'40'}))
       return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)
  # Also see https://pypi.python.org/pypi/django-cuser/
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            self.who = request.user.id
            kwargs['initial'] = self.who
            return db_field.formfield(**kwargs)
        return super(PostAdmin, self).formfield_for_foreignkey(
                     db_field, request, **kwargs)

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'on')
    list_display_links = ('title',)
    readonly_fields = ['pub_date'] 
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            self.who = request.user.id
            kwargs['initial'] = self.who
            return db_field.formfield(**kwargs)
        return super(PostAdmin, self).formfield_for_foreignkey(
                     db_field, request, **kwargs)


class EventAdmin(PostAdmin):
    list_display = ('title', 'publish', 'on', 'ebcode')
    list_display_links = ('title',)
    # exclude = ['author']
    def formfield_for_dbfield(self, field, **kwargs):
       if field.name == "byline":
          byline = Director.objects.get(user=self.current_user).nameinbyline
          return CharField(initial = byline,
                           max_length = 500,
                           widget=TextInput(attrs={'size':'40'}))
       if field.name == 'rpost':
          kwargs['queryset'] = Post.objects.all().order_by('-pub_date')
          kwargs['label'] = "Related article"
       return super(PostAdmin, self).formfield_for_dbfield(field, **kwargs)

class DirectorAdmin(admin.ModelAdmin):
   def queryset(self, request):
      if request.user.is_superuser:
          return Director.objects.all()
      return Director.objects.filter(user=request.user)
   list_display = ('user', 'nameinbyline', 'formalname')
   list_display_links = ('user', 'nameinbyline', 'formalname')
   exclude = ['user']
   def get_form(self, req, obj=None, **kwargs):
      self.current_user = req.user #Just for capturing current user
      return super(DirectorAdmin, self).get_form(req, obj, **kwargs)
   def formfield_for_dbfield(self, field, **kwargs):
      if field.name == "nameinbyline":
         return CharField(label = 'Name as byline', initial = self.current_user.get_full_name())
   #    # elif field == "formalname":
   #    #    return CharField(initial = self.current_user.title + ' ' + 
   #    #                     self.current_user.get_full_name())
      return super(DirectorAdmin, self).formfield_for_dbfield(field, **kwargs)

admin.site.register(Post, PostAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Illustration)
admin.site.register(Postcategory)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Event, EventAdmin)


