# Create your views here.
from django.shortcuts import render,get_object_or_404
#from django.http import HttpResponse,HttpResponseRedirect
from .models import ExpertInfo,ExpertComments,WorkExp
#from .forms import ExpertInfoForm, CommentForm,WorkexpForm
from .forms_update import ExpertInfoFormUpdate,ExpertInfoFormUpdateDB
from django.contrib.auth.decorators import login_required





@login_required
def expertInfoUpdate(request):
    form = ExpertInfoFormUpdate()
    return render(request, 'experts/update_expert.html',{'form': form})


def expertInfoUpdateToDatabase(request):
    print("!!!!!!!!!!!UPDATE这里！!!!!!!!!")
    form = ExpertInfoFormUpdate()
    ename = request.POST["ename"]
    expert_objs = ExpertInfo.objects.filter(ename=ename)
    for obj in expert_objs:
        print(obj.eid)

    #return HttpResponseRedirect('/updateexpert/')
    return render(request, 'experts/update_expert.html', {'form': form,'expert_objs': expert_objs})



