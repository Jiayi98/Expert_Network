from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import ExpertInfo,ExpertComments,WorkExp
from .forms import ExpertInfoForm, CommentForm,WorkexpForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def base(request):
    return render(request, 'experts/base.html')


"""
EXPERTS INFORMATION
"""


@login_required
def addExpert(request):
    form = ExpertInfoForm()
    return render(request, 'experts/addexpert.html', {'form': form})


@login_required
def addExpertToDatabase(request):
    if request.method == "POST":
        print("-----------POST----------")
        expertInfo_form = ExpertInfoForm(data=request.POST)
        if expertInfo_form.is_valid():
            print("-----------Does not exit!----------")
            new_expert = expertInfo_form.save(commit=False)
            expert = ExpertInfo.objects.filter(ename=new_expert.ename, emobile=new_expert.emobile)
            if expert.exists() == 0:
                print("-----------Does not exit!----------")
                new_expert = expertInfo_form.save()
            else:
                print("!!!!!!!!!!!This expert already existed!!!!!!!!")
                return render(request, 'experts/expert_already_exist.html')
                #return HttpResponseRedirect('/expertalreadyexist/')
        else:
            print("-----------NOT VALID----------")
    else:
        print("!!!!!!!!!!!GET!!!!!!!!")

    # 重定向
    return HttpResponseRedirect('/addcomplete/')


"""
"""


@login_required
def addComment(request):
    form = CommentForm()
    return render(request, 'experts/addcomment.html', {'form': form})


@login_required
def addCommentToDatabase(request):
    if request.method == "POST":
        ename = request.POST["ename"]
        emobile = request.POST["emobile"]
        eproblem = request.POST["eproblem"]
        ecomment = request.POST["ecomment"]
        try:
            expert = ExpertInfo.objects.get(ename=ename, emobile=emobile)
            print(expert.eid)
        except:
            print("!!!!!!!!!!!This expert not exist!!!!!!!!")
            return HttpResponseRedirect('/addecomment/')
            #return HttpResponseRedirect('experts/expertnotexist/')
        else:
            print("----------Expert Exists----------")
            newComment = ExpertComments()
            newComment.eid_id = expert.eid
            newComment.eproblem = eproblem
            newComment.ecomment = ecomment
            newComment.save()
            return HttpResponseRedirect('/addcomplete/')

    else:
        return render(request, 'addcomment.html')





@login_required
def addWorkexp(request):
    form = WorkexpForm()
    return render(request, 'experts/addworkexp.html',{'form': form})



@login_required
def addWorkexpToDatabase(request):
    if request.method == "POST":
        ename = request.POST["ename"]
        emobile = request.POST["emobile"]
        stime = request.POST["stime"]
        etime = request.POST["etime"]
        company = request.POST["company"]
        agency = request.POST["agency"]
        position = request.POST["position"]
        duty = request.POST["duty"]
        area = request.POST["area"]
        istonow = request.POST["istonow"]

        try:
            expert = ExpertInfo.objects.get(ename=ename, emobile=emobile)
            print(expert.eid)
        except:
            print("!!!!!!!!!!!This expert not exist!!!!!!!!")
            return HttpResponseRedirect('/addeworkexp/')
            # return HttpResponseRedirect('experts/expertnotexist/')
        else:
            print("----------Expert Exists----------")
            newExp = WorkExp()
            newExp.eid_id = expert.eid
            newExp.stime = stime
            newExp.etime = etime
            newExp.company = company
            newExp.agency = agency
            newExp.position = position
            newExp.duty = duty
            newExp.area = area
            newExp.istonow = istonow
            newExp.save()
            return HttpResponseRedirect('/addcomplete/')

    else:
        return render(request, 'addworkexp.html')




# 返回页面addok
@login_required
def addok(request):
    return render(request, 'experts/add_complete.html')


def expertInfo_list(request):
    experts_list = ExpertInfo.objects.all()
    paginator = Paginator(experts_list, 10)
    page = request.GET.get('page')
    try:
        experts = paginator.page(page)
    except PageNotAnInteger:
        experts = paginator.page(1)
    except EmptyPage:
        experts = paginator.page(paginator.num_pages)
    return render(request, 'experts/expertinfo_list.html', {'page':page, 'experts':experts})

def expert_detail(request, ename, emobile):
    expert = get_object_or404(ExpertInfo, ename=ename, emobile=emobile)
    return render(request, 'expert_detail.html', {'expert':expert})

