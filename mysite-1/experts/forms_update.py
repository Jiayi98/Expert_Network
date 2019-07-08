from django import forms
from .models import ExpertInfo,ExpertComments,WorkExp


# 从ExpertInfo模型中动态地创建表单
class ExpertInfoFormUpdate(forms.ModelForm):
    ename = forms.CharField(max_length=50, required=True)

    class Meta:
        model = ExpertInfo
        fields = ('ename',)
        #fields = ('ename','esex','emobile','eemail','etrade',
        #          'esubtrade','ebirthday','elandline','elocation',
        #          'emsn','eqq','ephoto','estate','ecomefrom','eremark','admin_id')

    def __init__(self, *args, **kwargs):
        super(ExpertInfoFormUpdate, self).__init__(*args, **kwargs)
        for field_name in self.base_fields:
            field = self.base_fields[field_name]
            field.widget.attrs.update({"class":"form-control"})

class ExpertInfoFormUpdateDB(forms.ModelForm):
    ename = forms.CharField(max_length=50, required=True)
    esex = forms.CharField(max_length=2, required=False)
    emobile = forms.CharField(max_length=50, required=False)
    eemail = forms.CharField(max_length=80, required=False)
    etrade = forms.CharField(max_length=150, required=False)
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
        #fields = ('ename',)
        fields = ('ename','esex','emobile','eemail','etrade',
                  'esubtrade','ebirthday','elandline','elocation',
                  'emsn','eqq','ephoto','estate','ecomefrom','eremark','admin_id')

    def __init__(self, *args, **kwargs):
        super(ExpertInfoFormUpdateDB, self).__init__(*args, **kwargs)
        for field_name in self.base_fields:
            field = self.base_fields[field_name]
            field.widget.attrs.update({"class":"form-control"})


#刚加的

class CommentFormUpdateDB(forms.ModelForm):
    eproblem = forms.CharField(required=False)
    ecomment = forms.CharField(required=False)

    class Meta:
        model = ExpertComments
        fields = ('eproblem','ecomment')

    def __init__(self, *args, **kwargs):
        super(CommentFormUpdateDB, self).__init__(*args, **kwargs)
        for field_name in self.base_fields:
            field = self.base_fields[field_name]
            field.widget.attrs.update({"class":"form-control"})


class WorkexpFormUpdateDB(forms.ModelForm):
    stime = forms.DateField(required=False)
    etime = forms.DateField(required=False)
    company = forms.CharField(max_length=50, required=False)
    agency = forms.CharField(max_length=50, required=False)
    position = forms.CharField(max_length=50, required=False)
    duty = forms.CharField(max_length=50, required=False)
    area = forms.CharField(max_length=50, required=False)
    istonow = forms.IntegerField(required=False)

    class Meta:
        model = WorkExp
        fields = ('stime','etime','company','agency','position','duty','area','istonow')

    def __init__(self, *args, **kwargs):
        super(WorkexpFormUpdateDB, self).__init__(*args, **kwargs)
        for field_name in self.base_fields:
            field = self.base_fields[field_name]
            field.widget.attrs.update({"class":"form-control"})
            
