# Create your models here.
from django.db import models
from django.urls import reverse


class ExpertInfo(models.Model):

    eid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=50)
    esex = models.CharField(max_length=2,choices=(('M','M'),('F','F')),default='F')
    emobile = models.CharField(max_length=50, blank=True, null=True)
    eemail = models.CharField(max_length=80, blank=True, null=True)
    etrade = models.CharField(max_length=150, blank=True, null=True)
    esubtrade = models.CharField(max_length=150, blank=True, null=True)
    ebirthday = models.DateField(blank=True, null=True)
    elandline = models.CharField(max_length=50, blank=True, null=True)
    elocation = models.CharField(max_length=150, blank=True, null=True)
    emsn = models.CharField(max_length=80, blank=True, null=True)
    eqq = models.CharField(max_length=50, blank=True, null=True)
    ephoto = models.CharField(max_length=20, blank=True, null=True)
    estate = models.IntegerField(blank=True, null=True)
    ecomefrom = models.TextField(blank=True, null=True)
    eremark = models.TextField(blank=True, null=True)
    admin_id = models.IntegerField(blank=True, null=True)
    addtime = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        ordering = ('-addtime',)

    def __str__(self):
        return "{}-{}".format(self.eid, self.ename)

    def get_absolute_url(self):
        return reverse('expert_detail',args=[self.ename, self.emobile])

    def get_update_url(self):
        return reverse('expert_detail_update', args=[self.ename, self.emobile])


class ExpertComments(models.Model):
    cmtid = models.AutoField(primary_key=True)
    eid = models.ForeignKey('ExpertInfo', on_delete=models.CASCADE)
    eproblem = models.TextField(blank=True, null=True)
    ecomment = models.TextField(blank=True, null=True)

    class Meta:
        managed = True

    def __str__(self):
        # 默认的人们可读的对象表达方式
        return "{}-{}".format(self.eid,self.eproblem)

class WorkExp(models.Model):
    expid = models.AutoField(primary_key=True)
    eid = models.ForeignKey('ExpertInfo', on_delete=models.CASCADE)
    stime = models.DateField(blank=True, null=True)
    etime = models.DateField(blank=True, null=True)
    company = models.CharField(max_length=150, blank=True, null=True)
    agency = models.CharField(max_length=150, blank=True, null=True)
    position = models.CharField(max_length=150, blank=True, null=True)
    duty = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    istonow = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        ordering = ('-etime', 'stime',)

    def __str__(self):
        return "{}-{}".format(self.eid,self.company)