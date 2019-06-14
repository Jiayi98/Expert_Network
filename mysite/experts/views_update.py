from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ExpertInfo,ExpertComments,WorkExp
from .forms import ExpertInfoForm, CommentForm,WorkexpForm
from django.contrib.auth.decorators import login_required


def expertInfoUpdate(request, ename, emobile):
    try:
        expert_obj = ExpertInfo.objects.get(ename=ename, emobile=emobile)
        print(expert_obj.eid)
    except:
        print("!!!!!!!!!!!This expert not exist!!!!!!!!")
        return HttpResponseRedirect('/updateexpertinfo/')

    else:

        if request.method == 'POST':
            form = ExpertInfoForm(request.POST, instance=expert_obj)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/addcomplete/')

            else:
                print("---------INVALID表单-----------")

        else:
            form = ExpertInfoForm(instance=expert_obj)

        return render(request, 'updateexpertinfo.html')