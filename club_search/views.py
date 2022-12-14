from django.shortcuts import render, get_object_or_404

from club_search.models import Club


# Create your views here.
def index(request):
    context = {
        "navbar_active": "홈",
    }

    return render(request, 'club_search/index.html', context)


def club_list(request, club_department):
    if club_department == "com_edu":
        club_department_raw = "컴퓨터교육과"
    elif club_department == "edu":
        club_department_raw = "교육학과"
    elif club_department == "math_edu":
        club_department_raw = "수학교육과"
    elif club_department == "han_edu":
        club_department_raw = "한문교육과"
    else:
        club_department_raw = "사범대학"

    clubs = Club.objects.filter(department=club_department_raw)

    context = {
        "header_title": club_department_raw,
        "navbar_active": club_department_raw,
        "club_list": clubs,
    }

    return render(request, 'club_search/club_list.html', context)


def club_detail(request, club_id):
    club = Club.objects.get(id=club_id)

    context = {
        "header_title": club.department,
        "navbar_active": club.department,
        "club": club,
    }

    return render(request, 'club_search/club_detail.html', context)
