from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ["user","balance"]


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ["wallet","point","credited_on","content_object"]



@admin.register(Debit)
class DebitAdmin(admin.ModelAdmin):
    list_display = ["wallet","point","debited_on","content_object"]