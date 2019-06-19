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


@login_required
def info_update(request, ename, emobile):

    #if not request.user.has_perm(''):
    #    raise PermissionDenied

    # Either render only the modal content, or a full standalone page

    template_name = 'experts/expert_detail_update.html'


    object = get_object_or_404(ExpertInfo, ename=ename, emobile=emobile)
    if request.method == 'POST':
        form = ExpertInfoFormUpdateDB(instance=object, data=request.POST)
        if form.is_valid():
            form.save()
            # if is_ajax(), we just return the validated form, so the modal will close
    else:
        form = ExpertInfoFormUpdateDB(instance=object)

    return render(request, template_name, {
        'form': form,
    })
