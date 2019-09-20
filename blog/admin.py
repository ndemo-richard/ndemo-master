from django.contrib import admin
from blog.models import Post,Imagee

admin.site.site_header = 'Ndemo Richard django Panel'


# post modelAdmin
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status", 'tags')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)



class ImageAdmin(admin.ModelAdmin):
    list_display = ['title']

    class Meta:
        model = Imagee


admin.site.register(Imagee, ImageAdmin)
