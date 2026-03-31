from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("members/", views.members, name="members"),
    path("values/", views.values, name="values"),
    path("table/members/", views.table_members, name="table_members"),
    path("mypage/", views.mypage, name="mypage"),
    path("insert/", views.insert_data, name="insert"),
    path("show/", views.show_data, name="show"),
    path("delete/<int:id>/", views.delete_data, name="delete"),
    path("numbers/", views.number_view, name="number_view"),
]
