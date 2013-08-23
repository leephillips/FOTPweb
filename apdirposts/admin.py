from models import Post
from django.contrib import admin
from django.db import models
from django.forms import ModelForm
from django.forms import CharField

       
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
    list_display = ('author', 'byline', 'title', 'publish', 'content')
    # form = PostAdminForm
    def get_form(self, req, obj=None, **kwargs):
        # save the logged in user 
        self.current_user = req.user
        return super(PostAdmin, self).get_form(req, obj, **kwargs)
    def formfield_for_dbfield(self, field, **kwargs):
       if field.name == "byline":
          return CharField(initial = self.current_user.get_full_name())
       return super(PostAdmin, self).formfield_for_dbfield(field, **kwargs)
  # Also see https://pypi.python.org/pypi/django-cuser/
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            self.who = request.user.id
            kwargs['initial'] = self.who
            return db_field.formfield(**kwargs)
        return super(PostAdmin, self).formfield_for_foreignkey(
                     db_field, request, **kwargs)
    # formfield_overrides = {models.CharField: {'initial': 'hihihi'},}

admin.site.register(Post, PostAdmin)


