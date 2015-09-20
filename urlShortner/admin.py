from django.contrib import admin
from .models import urlShortner

# Register your models here.
class urlShortnerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['fullurl','shorturl']}),
        ('Date information', {'fields': ['entry_date'], 'classes': ['collapse']}),
    ]
    list_display = ('fullurl','shorturl','entry_date')
    list_filter = ['entry_date']
    search_fields = ['fullurl','shorturl']

admin.site.register(urlShortner, urlShortnerAdmin)

