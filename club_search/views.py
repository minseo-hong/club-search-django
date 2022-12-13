from django.shortcuts import render

from club_search.models import Club


# Create your views here.
def index(request):
    context = {
        "navbar_active": "홈",
    }

    return render(request, 'club_search/index.html', context)


def edu_group(request):
    club_list = Club.objects.filter(department="사범대학")
    club_list = club_list.order_by('name')

    context = {
        "header_title": "사범대학",
        "navbar_active": "사범대학",
        "club_list": club_list,
    }

    return render(request, 'club_search/club_list.html', context)


def com_edu(request):
    club_list = Club.objects.filter(department="컴퓨터교육과")
    club_list = club_list.order_by('name')

    context = {
        "header_title": "컴퓨터교육과",
        "navbar_active": "컴퓨터교육과",
        "club_list": club_list,
    }

    return render(request, 'club_search/club_list.html', context)


def edu(request):
    club_list = Club.objects.filter(department="교육학과")
    club_list = club_list.order_by('name')

    context = {
        "header_title": "교육학과",
        "navbar_active": "교육학과",
        "club_list": club_list,
    }

    return render(request, 'club_search/club_list.html', context)


def han_edu(request):
    club_list = Club.objects.filter(department="한문교육과")
    club_list = club_list.order_by('name')

    context = {
        "header_title": "한문교육과",
        "navbar_active": "한문교육과",
        "club_list": club_list,
    }

    return render(request, 'club_search/club_list.html', context)


def math_edu(request):
    club_list = Club.objects.filter(department="수학교육과")
    club_list = club_list.order_by('name')

    context = {
        "header_title": "수학교육과",
        "navbar_active": "수학교육과",
        "club_list": club_list,
    }

    return render(request, 'club_search/club_list.html', context)


def detail(request, club_id):
    club = Club.objects.get(id=club_id)

    context = {
        "header_title": club.department,
        "navbar_active": club.department,
        "club": club,
    }

    return render(request, 'club_search/club_detail.html', context)
