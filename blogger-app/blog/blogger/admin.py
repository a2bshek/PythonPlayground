from django.contrib import admin
from blogger import models

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp','username')
    def __str__(self):
        return self.title
        
admin.site.register(models.BlogPost,BlogPostAdmin)