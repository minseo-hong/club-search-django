from django.urls import path

from club_search import views

app_name = "club_search"

urlpatterns = [
    path("<int:club_id>/", views.club_detail, name="detail"),
    path("<str:club_department>/", views.club_list, name="club_list"),
]
