from django.urls import path

from club_search import views

app_name = "club_search"

urlpatterns = [
    path("edu-group/", views.edu_group, name="edu_group"),
    path("com-edu/", views.com_edu, name="com_edu"),
    path("edu/", views.edu, name="edu"),
    path("han-edu/", views.han_edu, name="han_edu"),
    path("math-edu/", views.math_edu, name="math_edu"),
    path("<int:club_id>/", views.detail, name="detail"),
]
