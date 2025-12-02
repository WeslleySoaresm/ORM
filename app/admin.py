from django.contrib import admin

from app.models import Category, EcommerceUser

# Register your models here.


admin.site.register(Category)

# add custmize admin for EcommerceUser
@admin.register(EcommerceUser)
class EcommerceUserAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'username', 'email', 'role', 'created_at', 'updated_at')
    search_fields = ('username', 'email')
    list_filter = ('role', 'created_at')
    ordering = ('id_user',) 

