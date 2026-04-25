from django.contrib import admin

from .models import Booking, FoodItem, Order, Room, TableReservation

admin.site.site_header = 'Northgate Resort Isiolo Admin'
admin.site.site_title = 'Northgate Resort Isiolo'
admin.site.index_title = 'Resort Management'


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_type', 'price', 'is_available')
    list_filter = ('room_type', 'is_available')
    search_fields = ('name', 'description')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'check_in', 'check_out', 'total_price')
    list_filter = ('room',)
    search_fields = ('user__username', 'room__name')


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_filter = ('available',)
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'total_price')
    list_filter = ()
    search_fields = ('user__username',)


@admin.register(TableReservation)
class TableReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'guests', 'date', 'time')
    list_filter = ('date',)
    search_fields = ('user__username',)
