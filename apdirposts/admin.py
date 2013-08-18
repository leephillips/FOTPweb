from models import Post
from django.contrib import admin
# from django import models
from django.forms import ModelForm
from django.forms import CharField

# class PostAdminForm(ModelForm):
#    byline =    ?
#    class Meta:
#       model = Post

class PostAdmin(admin.ModelAdmin):
    # form = PostAdminForm
    def formfield_for_foreignkey(self, db_field, request, **kwargs): #[1]
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
            return db_field.formfield(**kwargs)
        return super(PostAdmin, self).formfield_for_foreignkey(
                     db_field, request, **kwargs)

        # if db_field.name == 'byline':
        #     kwargs['initial'] = 'hihihihi'
        #     return db_field.formfield(**kwargs)
        # return super(PostAdmin, self).formfield_for_dbfield(
        #              db_field, **kwargs)

    fields = ['author', 'byline', 'title', 'publish', 'content']

admin.site.register(Post, PostAdmin)


#[1] http://stackoverflow.com/questions/5632848/default-value-for-user-foreignkey-with-django-admin
