from django.contrib import admin
from .models import tips
# Register your models here.
class TipsAdmin(admin.ModelAdmin):
    list_display =( 'title','content','level','type')
admin.site.register(tips,TipsAdmin)
