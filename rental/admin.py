from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Car, Rental, Profile,Promocode,CarouselImage


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')
    search_fields = ('user__username', 'phone', 'address')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'brand', 'model_name', 'year', 'car_type', 'current_price', 'available_city', 'isavailable')
    search_fields = ('car_name', 'brand', 'model_name', 'available_city')
    list_filter = ('car_type', 'isavailable', 'year')
    ordering = ('-created_at',)

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'total_price')
    list_filter = ('user', 'car')
    ordering = ('user',)


@admin.register(Promocode)
class Promo(admin.ModelAdmin):
    list_display=('code','discount_per')
    
@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ("title",)
