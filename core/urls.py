from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("rooms/", views.room_list, name="room_list"),
    path("rooms/<int:pk>/", views.room_detail, name="room_detail"),
    path("experiences/", views.experiences, name="experiences"),
    path("packages/", views.packages, name="packages"),
    path("events/", views.events, name="events"),
    path("contact/", views.contact, name="contact"),
    path("book/<int:pk>/", views.book_room, name="book_room"),
    path("bookings/", views.booking_history, name="booking_history"),
    path("food/", views.food_menu, name="food_menu"),
    path("order/", views.order_food, name="order_food"),
    path("orders/", views.order_history, name="order_history"),
    path("reserve/", views.table_reservation, name="table_reservation"),
    path("register/", views.register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]