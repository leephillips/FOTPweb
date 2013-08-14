from models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs): #[1]
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
            return db_field.formfield(**kwargs)
        return super(PostAdmin, self).formfield_for_foreignkey(
                     db_field, request, **kwargs)
    # def formfield_for_charfield(self, db_field, request, **kwargs):
    #     if db_field.name == 'byline':
    #         kwargs['initial'] = request.user.name()
    #         return db_field.formfield(**kwargs)

    fields = ['author', 'byline', 'title', 'publish', 'content']

admin.site.register(Post, PostAdmin)


#[1] http://stackoverflow.com/questions/5632848/default-value-for-user-foreignkey-with-django-admin
