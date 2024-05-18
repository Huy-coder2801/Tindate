from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Profile
from django.contrib.auth.models import User
from friends.models import FriendRequest
from operator import itemgetter
from django.contrib import messages

from .forms import UserSearchForm
from django.db.models import Q

def home_view(request, *args, **kwargs):
    """
    Homepage has default interface.
    If user chooses to serach others, it will redirect to user's infomation. (only basic info will be showed to user without login)
    """
    # print(request)
    top3_list = []
    top3_dict = {}
    top3_num = []
    for user in User.objects.all():     
        received_requests = FriendRequest.objects.filter(receiver=user)
        top3_list.append(user)
        top3_num.append(received_requests.count())
        top3_dict.update({str(user): received_requests.count()})
    print(top3_dict)
    top3_list =sorted(top3_list,  key=lambda x: top3_dict[str(x)], reverse=True)
    print(top3_list)
    top3_num = sorted(top3_num, reverse=True)[:3]
    top3_list = top3_list[:3]
    try:
        top1 = top3_list[0]
        top1_num = top3_num[0]
    except:
        top1 = None
        top1_num = None
    try:
        top2 = top3_list[1]
        top2_num = top3_num[1]
    except:
        top2 = None
        top2_num = None
    try:
        top3 = top3_list[2]
        top3_num = top3_num[2]
    except:
        top3 = None
        top3_num = None
    context = {
        'top1_user': top1,
        'top2_user': top2,
        'top3_user': top3,
        'top1_num': top1_num,
        'top2_num': top2_num,
        'top3_num': top3_num
    }
    return render(request, 'home.html', context)

    


def search_view(request):
    form = UserSearchForm(request.GET or None)
    if form.is_valid():
        query = form.cleaned_data.get('query')
        results = Profile.objects.filter(
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query) |
                Q(bio__icontains=query) |
                Q(gender__icontains=query) |
                Q(education__icontains=query) |
                Q(pronouns__icontains=query) |
                Q(sexuality__icontains=query)
            )
    else:
        
        results = Profile.objects.none()

    context = {
        'form': form,
        'results': results
    }
    return render(request, 'search.html', context)   

def user_detail_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, '../templates/social/user_profile.html', {'user': user})