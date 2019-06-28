# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import ExpertInfo,ExpertComments,WorkExp
#from .forms import ExpertInfoForm, CommentForm,WorkexpForm
from .forms_update import ExpertInfoFormUpdate
#CommentFormUpdate,WorkexpFormUpdate,ExpertInfoFormUpdateDB
from django.contrib.auth.decorators import login_required
from .views import comment_detail

@login_required
def expertInfoDelete(request):
    #print("============用到了这个吗==========")
    form = ExpertInfoFormUpdate()
    return render(request, 'experts/delete_expert.html',{'form': form})


def expertInfoDeleteFromDatabase(request):
    print("!!!!!!!!!!!views.update.DELETE这里！!!!!!!!!")
    form = ExpertInfoFormUpdate()
    ename = request.POST["ename"]
    expert_objs = ExpertInfo.objects.filter(ename=ename)
    for obj in expert_objs:
        print(obj.eid)

    return render(request, 'experts/delete_expert.html', {'form': form,'expert_objs': expert_objs})


"""
Info
"""
@login_required
def expertInfoUpdate(request):
    #print("============用到了这个吗==========")
    form = ExpertInfoFormUpdate()
    return render(request, 'experts/update_expert.html',{'form': form})


def expertInfoUpdateToDatabase(request):
    print("!!!!!!!!!!!UPDATE这里！!!!!!!!!")
    form = ExpertInfoFormUpdate()

    ename = request.POST["ename"]
    expert_objs = ExpertInfo.objects.filter(ename=ename)
    for obj in expert_objs:
        print(obj.eid)

    return render(request, 'experts/update_expert.html', {'form': form,'expert_objs': expert_objs})

# 6.24
def delete_comment(request, eid, cmtid):
    print("=============views_update.delete_comment======")
    template_name = 'experts/comment_detail.html'
    result = {}
    try:
        print("==============Try========")
        expert = ExpertInfo.objects.get(eid=eid)
        c = ExpertComments.objects.get(cmtid=cmtid)
        print(expert,c)
    except:
        print("==============ERROR========")
        result['status'] = 'error'
    else:
        result['status'] = 'success'
        return render(request, template_name,{'c':c,'expert':expert,'result':result})

def delete_comment_confirm(request, eid, cmtid):
    print("=============views_update.delete_comment_confirm======")
    template_name = 'experts/comment_detail.html'
    result = {}
    try:
        print("==============Try========")
        expert = ExpertInfo.objects.get(eid=eid)
        c = ExpertComments.objects.get(cmtid=cmtid)
        print(expert,c)
    except:
        print("==============ERROR========")
        result['status'] = 'error'
    else:
        c.delete()
        result['status'] = 'success'
        #return comment_detail(request, eid, expert.ename)
        url = 'http://127.0.0.1:8000/{eid}/{ename}/commentdetail'.format(eid=eid,ename=expert.ename)
        return HttpResponseRedirect(url)

    #return render(request, template_name,{'expert':expert,'result':result})

def delete_workexp(request, eid, expid):
    print("=============views_update.delete_workexp======")
    template_name = 'experts/workexp_detail.html'
    result = {}
    try:
        print("==============Try========")
        expert = ExpertInfo.objects.get(eid=eid)
        exp = WorkExp.objects.get(expid=expid)
        print(expert,exp)
    except:
        print("==============ERROR========")
        result['status'] = 'error'
    else:
        result['status'] = 'success'
        return render(request, template_name,{'exp':exp,'expert':expert,'result':result})

def delete_workexp_confirm(request, eid, expid):
    print("=============views_update.delete_workexp_confirm======")
    template_name = 'experts/workexp_detail.html'
    result = {}
    try:
        print("==============Try========")
        expert = ExpertInfo.objects.get(eid=eid)
        exp = WorkExp.objects.get(expid=expid)
        print(expert,exp)
    except:
        print("==============ERROR========")
        result['status'] = 'error'
    else:
        exp.delete()
        result['status'] = 'success'
        url = 'http://127.0.0.1:8000/{eid}/{ename}/workexpdetail'.format(eid=eid,ename=expert.ename)
        return HttpResponseRedirect(url)

    #return render(request, template_name,{'expert':expert,'result':result})

"""
Comment

@login_required
def commentUpdate(request):
    form = CommentFormUpdate()
    return render(request, 'experts/update_comment.html',{'form': form})


def commentUpdateToDatabase(request):
    print("!!!!!!!!!!!更新访谈的view!!!!!!!!")
    form = CommentFormUpdate()
    ename = request.POST["ename"]
    expert_objs = ExpertInfo.objects.filter(ename=ename)

    for obj in expert_objs:
        comment_objs = ExpertComments.objects.filter(eid=obj.eid)
        for c in comment_objs:
            print(obj.eid, c.cmtid)

    return render(request, 'experts/update_comment.html', {'form': form,
                                                           'expert_objs': expert_objs,
                                                           'comment_objs':comment_objs})



Workexp

@login_required
def workexpUpdate(request):
    form = WorkexpFormUpdate()
    return render(request, 'experts/update_workexp.html',{'form': form})


def workexpUpdateToDatabase(request):
    print("!!!!!!!!!!!更新经历的view！!!!!!!!!")
    form = WorkexpFormUpdate()
    ename = request.POST["ename"]
    expert_objs = ExpertInfo.objects.filter(ename=ename)
    for obj in expert_objs:
        print(obj.eid)

    #return HttpResponseRedirect('/updateexpert/')
    return render(request, 'experts/update_workexp.html', {'form': form,'expert_objs': expert_objs})
"""
