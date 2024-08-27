from django.contrib import admin

from app01.models import userinfo,files
class Files(admin.ModelAdmin):
    list_display = ('files_id','files_name','files_user')
admin.site.register(userinfo)
admin.site.register(files,Files)
# Register your models here.
