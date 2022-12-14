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
        club_department = "컴퓨터교육과"
    elif club_department == "edu":
        club_department = "교육학과"
    elif club_department == "math_edu":
        club_department = "수학교육과"
    elif club_department == "han_edu":
        club_department = "한문교육과"
    else:
        club_department = "사범대학"

    search = request.GET.get('search', None)
    sort = request.GET.get('sort', None)

    if search and sort:
        clubs = Club.objects.filter(department=club_department, name__contains=search, sort=sort)
    elif search and not sort:
        clubs = Club.objects.filter(department=club_department, name__contains=search)
    elif not search and sort:
        clubs = Club.objects.filter(department=club_department, sort=sort)
    else:
        clubs = Club.objects.filter(department=club_department)

    context = {
        "header_title": club_department,
        "navbar_active": club_department,
        "club_list": clubs,
        "dropdown_selected": sort,
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


def club_list_all(request):
    search = request.GET.get('search', '')

    searched_clubs = Club.objects.filter(name__contains=search)

    context = {
        "header_title": "검색",
        "navbar_active": "홈",
        "club_list": searched_clubs,
    }

    return render(request, 'club_search/club_list.html', context)
