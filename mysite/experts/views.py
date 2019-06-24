from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import ExpertInfo,ExpertComments,WorkExp
from .forms import ExpertInfoForm, CommentForm,WorkexpForm,deleteConfirmForm

from .forms_update import ExpertInfoFormUpdateDB,CommentFormUpdateDB, WorkexpFormUpdateDB,ExpertInfoFormUpdate

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def base(request):
    return render(request, 'experts/base.html')

def myDelete(request, ename, emobile):
    print("=============views.DELETE======")
    template_name = 'experts/delete.html'
    expert = get_object_or_404(ExpertInfo, ename=ename, emobile=emobile)
    return render(request, 'experts/delete.html', {'expert':expert})

#def deleteConfirm(request):
def delete_confirm(request, ename, emobile):
    print("=============views.delete_confirm======")
    template_name = 'experts/delete_confirm.html'
    result = {}
    form = deleteConfirmForm(request.POST)
    name = request.POST.get('ename')
    mobile = request.POST.get('emobile')
    if request.method == 'POST' and request.POST:
        print("==============进来了=")
        if form.is_valid():
            try:
                print("==============Try========")
                expert = ExpertInfo.objects.get(ename=ename,emobile=emobile)
                print(expert)
            except:
                print("==============ERROR========")
                result['status'] = 'error'
            else:
                expert.delete()
                result['status'] = 'success'
                return HttpResponseRedirect('/addcomplete/')

        else:
            print("==============form is INVALID========")
    else:
        form = deleteConfirmForm(request.POST)

    return render(request, template_name, {'form':form,'result':result})

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
            new_expert = expertInfo_form.save(commit=False)
            # filter得到的是一个list，而不是一个object
            expert = ExpertInfo.objects.filter(ename=new_expert.ename, emobile=new_expert.emobile)
            if expert.exists() == 0:
                print("-----------Does not exist!----------")
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
    formC = CommentForm()
    formI = ExpertInfoFormUpdate()

    ename = request.POST.get("ename")
    expert_objs = ExpertInfo.objects.filter(ename=ename)
    for obj in expert_objs:
        print(obj.eid)

    return render(request, 'experts/addcomment.html', {'formC': formC,'formI':formI,'expert_objs':expert_objs})


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
            form = CommentForm(request.POST, instance=expert)
            print("----------Expert Exists----------")
            newComment = ExpertComments()
            newComment.eid_id = expert.eid
            newComment.eproblem = eproblem
            newComment.ecomment = ecomment
            newComment.save()
            return HttpResponseRedirect('/addcomplete/')

    else:
        return render(request, 'experts/addcomment.html')





@login_required
def addWorkexp(request):
    formW = WorkexpForm()
    formI = ExpertInfoFormUpdate()

    ename = request.POST.get("ename")
    expert_objs = ExpertInfo.objects.filter(ename=ename)
    for obj in expert_objs:
        print(obj.eid)

    return render(request, 'experts/addworkexp.html', {'formW': formW, 'formI': formI, 'expert_objs': expert_objs})




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
            form = WorkexpForm(request.POST, instance=expert)
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
    # if not request.user.has_perm(''):
    #    raise PermissionDenied
    print("===========views.expert_detail=========")
    expert = get_object_or_404(ExpertInfo, ename=ename, emobile=emobile)
    #eid = expert.eid
    #comments = ExpertComments.objects.filter(eid=expert.eid)
    #print(expert.eid)
    #for c in comments:
    #    print(c.cmtid)

    return render(request, 'experts/expert_detail.html', {'expert': expert})
    #return render(request, 'experts/expert_detail.html', {'expert':expert, 'comments':comments})


def expert_detail_update(request, ename, emobile):
    template_name = 'experts/expert_detail_update.html'
    object = get_object_or_404(ExpertInfo, ename=ename, emobile=emobile)
    #form = ExpertInfoFormUpdateDB(instance=expert)

    if request.method == 'POST':
        form = ExpertInfoFormUpdateDB(instance=object, data=request.POST)
        if form.is_valid():
            form.save()
            # if is_ajax(), we just return the validated form, so the modal will close
        return HttpResponseRedirect('/addcomplete/')
    else:
        form = ExpertInfoFormUpdateDB(instance=object)

    return render(request, template_name, {'expert':object,'form': form,})



def comment_detail(request, eid, ename):
    # if not request.user.has_perm(''):
    #    raise PermissionDenied
    print("=================在views.py中comment_detail()==========")
    expert = get_object_or_404(ExpertInfo,eid=eid)
    comments = ExpertComments.objects.filter(eid=eid)
    print(eid)
    for c in comments:
        print(c.cmtid)
    return render(request, 'experts/comment_detail.html', {'expert':expert,'comments': comments})

# 刚加的
def comment_detail_update(request, eid, cmtid):
    print("=============views.py中comment_detail_update()")
    template_name = 'experts/comment_detail_update.html'
    expert = get_object_or_404(ExpertInfo, eid=eid)
    comment = get_object_or_404(ExpertComments, cmtid=cmtid)
    #form = ExpertInfoFormUpdateDB(instance=expert)
    #print(eid, comment.eproblem)
    result = {}
    if request.method == 'POST':
        form = CommentFormUpdateDB(instance=comment, data=request.POST)
        #print("~~~~~~~~~~~~~~~~~~", form.is_valid())
        if form.is_valid():
            form.save()
            result['status'] = 'success'
        #return HttpResponseRedirect('/addcomplete/')
    else:
        form = CommentFormUpdateDB(instance=comment)

    return render(request, template_name, {'comment':comment,'expert': expert,'form': form,'result':result})


def workexp_detail(request, eid, ename):
    # if not request.user.has_perm(''):
    #    raise PermissionDenied

    expert = get_object_or_404(ExpertInfo,eid=eid)
    workexps = WorkExp.objects.filter(eid=eid)
    print(eid)
    for w in workexps:
        print(w.expid)
    return render(request, 'experts/workexp_detail.html', {'expert':expert,'workexps': workexps})

# 刚加的
def workexp_detail_update(request, eid, expid):
    print("=============views.py中workexp_detail_update()")
    template_name = 'experts/workexp_detail_update.html'
    expert = get_object_or_404(ExpertInfo, eid=eid)
    workexp = get_object_or_404(WorkExp, expid=expid)
    result = {}
    if request.method == 'POST':
        form = WorkexpFormUpdateDB(instance=workexp, data=request.POST)
        if form.is_valid():
            form.save()
            # if is_ajax(), we just return the validated form, so the modal will close
            result['status'] = 'success'
        #return HttpResponseRedirect('/addcomplete/')
    else:
        form = WorkexpFormUpdateDB(instance=workexp)

    return render(request, template_name, {'workexp':workexp,'expert': expert,'form': form,'result':result})


