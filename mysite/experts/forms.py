from django import forms
from .models import ExpertInfo,ExpertComments,WorkExp
#import datetime

# 从ExpertInfo模型中动态地创建表单
class ExpertInfoForm(forms.ModelForm):
    ename = forms.CharField(max_length=50, required=True)
    esex = forms.CharField(max_length=2, required=False)
    emobile = forms.CharField(max_length=50, required=True)
    eemail = forms.CharField(max_length=80, required=False)
    etrade = forms.CharField(max_length=150, required=True)
    esubtrade = forms.CharField(max_length=150, required=False)
    ebirthday = forms.DateField(required=False)
    elandline = forms.CharField(max_length=50, required=False)
    elocation = forms.CharField(max_length=150, required=False)
    eqq = forms.CharField(max_length=50, required=False)
    ephoto = forms.CharField(max_length=20, required=False)
    estate = forms.IntegerField(required=False)
    ecomefrom = forms.CharField(required=False)
    eremark = forms.CharField(required=False)
    admin_id = forms.IntegerField(required=False)
    #addtime = forms.DateTimeField(initial=datetime.now())

    class Meta:
        model = ExpertInfo
        fields = ('ename','esex','emobile','eemail','etrade',
                  'esubtrade','ebirthday','elandline','elocation',
                  'emsn','eqq','ephoto','estate','ecomefrom','eremark','admin_id')

    def __init__(self, *args, **kwargs):
        super(ExpertInfoForm, self).__init__(*args, **kwargs)
        for field_name in self.base_fields:
            field = self.base_fields[field_name]
            field.widget.attrs.update({"class":"form-control"})


# 从ExpertInfo模型中动态地创建表单
class CommentForm(forms.ModelForm):

    ename = forms.CharField(max_length=50, required=True)
    emobile = forms.CharField(max_length=50, required=True)
    allExperts = ExpertInfo.objects.all()

    for exp in allExperts:
        if(exp.ename==ename and exp.emobile==emobile):
            eid = exp.eid
            exp.eid.eproblem = forms.TextField(required=True)
            exp.eid.ecomment = forms.TextField(required=True)


    class Meta:
        model = ExpertComments
        fields = ('ename','emobile','eproblem','ecomment')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field_name in self.base_fields:
            field = self.base_fields[field_name]
            field.widget.attrs.update({"class":"form-control"})



# 从ExpertInfo模型中动态地创建表单
class WorkexpForm(forms.ModelForm):
    ename = forms.CharField(max_length=50, required=True)
    emobile = forms.CharField(max_length=50, required=True)
    allExperts = ExpertInfo.objects.all()
    for exp in allExperts:
        if(exp.ename==ename and exp.emobile==emobile):
            eid = exp.eid
            exp.eid.stime = forms.DateField(required=False)
            exp.eid.etime = forms.DateField(required=False)
            exp.eid.company = forms.CharField(max_length=150,requried=False)
            exp.eid.agency = forms.CharField(required=False)
            exp.eid.position = forms.CharField(required=False)
            exp.eid.duty = forms.CharField(required=False)
            exp.eid.area = forms.CharField(required=False)
            exp.eid.istonow = forms.IntegerField(required=False)

    class Meta:
        model = WorkExp
        fields = ('ename','emobile','stime','etime',
                  'company','agency','position','duty',
                  'area','istonow')

    def __init__(self, *args, **kwargs):
        super(WorkexpForm, self).__init__(*args, **kwargs)
        for field_name in self.base_fields:
            field = self.base_fields[field_name]
            field.widget.attrs.update({"class":"form-control"})

class deleteConfirmForm(forms.Form):
    ename = forms.CharField(required=True)
    emobile = forms.CharField(required=True)
    class Meta:
        model = ExpertInfo
        fields = ['ename','emobile']

    def __init__(self, *args, **kwargs):
        super(deleteConfirmForm, self).__init__(*args, **kwargs)
        for field_name in self.base_fields:
            print(field_name)
            field = self.base_fields[field_name]
            field.widget.attrs.update({"class":"form-control"})