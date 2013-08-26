from models import Post
from models import Director, Illustration, Postcategory
from django.contrib import admin
from django.db import models
from django.forms import ModelForm, CharField, TextInput

       
# class BylineCharField(CharField):
#    def __init__(self, *args, **kwargs):
#       self.who = queryset(self)
#       self.initial = self.who.get_full_name()
#       return super(BylineCharField, self).__init__(*args, **kwargs)

# class PostAdminForm(ModelForm):
#    # byline = BylineCharField()
#    class Meta:
#       model = Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('byline', 'title', 'publish', 'pub_date')
    list_display_links = ('title',)
    readonly_fields = ['pub_date'] 
    exclude = ['author']
    # form = PostAdminForm
    def get_form(self, req, obj=None, **kwargs):
        # save the logged in user 
        self.current_user = req.user
        return super(PostAdmin, self).get_form(req, obj, **kwargs)
    # http://www.vimtips.org/2009/04/28/django-using-modeladmin-default-currently-logged-u/
    def formfield_for_dbfield(self, field, **kwargs):
       if field.name == "byline":
          return CharField(initial = self.current_user.get_full_name(),
                           max_length = 500,
                           widget=TextInput(attrs={'size':'40'}))
       elif field.name == "title":
          return CharField(initial = self.current_user.get_full_name(),
                           max_length = 500,
                           widget=TextInput(attrs={'size':'80'}))
       return super(PostAdmin, self).formfield_for_dbfield(field, **kwargs)
  # Also see https://pypi.python.org/pypi/django-cuser/
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            self.who = request.user.id
            kwargs['initial'] = self.who
            return db_field.formfield(**kwargs)
        return super(PostAdmin, self).formfield_for_foreignkey(
                     db_field, request, **kwargs)
    def save_model(self, request, obj, form, change):
       obj.author = request.user
       obj.save()

class DirectorAdmin(admin.ModelAdmin):
   def queryset(self, request):
      if request.user.is_superuser:
          return Director.objects.all()
      return Director.objects.filter(user=request.user)
   list_display = ('title', 'nameinbyline', 'formalname')
   list_display_links = ('title', 'nameinbyline', 'formalname')
   def get_form(self, req, obj=None, **kwargs):
      self.current_user = req.user
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


