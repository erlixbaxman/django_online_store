from django.contrib import admin

from .models import EmailVerification, User

admin.site.register(User)
admin.site.register(EmailVerification)


class EmailVerification(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration')
    fields = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created',)
