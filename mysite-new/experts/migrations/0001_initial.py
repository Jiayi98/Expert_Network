# Generated by Django 2.2.1 on 2019-06-11 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertInfo',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=50)),
                ('esex', models.CharField(choices=[('M', 'M'), ('F', 'F')], default='', max_length=2)),
                ('emobile', models.CharField(blank=True, max_length=50, null=True)),
                ('eemail', models.CharField(blank=True, max_length=80, null=True)),
                ('etrade', models.CharField(blank=True, max_length=150, null=True)),
                ('esubtrade', models.CharField(blank=True, max_length=150, null=True)),
                ('ebirthday', models.DateField(blank=True, null=True)),
                ('elandline', models.CharField(blank=True, max_length=50, null=True)),
                ('elocation', models.CharField(blank=True, max_length=150, null=True)),
                ('emsn', models.CharField(blank=True, max_length=80, null=True)),
                ('eqq', models.CharField(blank=True, max_length=50, null=True)),
                ('ephoto', models.CharField(blank=True, max_length=20, null=True)),
                ('estate', models.IntegerField(blank=True, null=True)),
                ('ecomefrom', models.TextField(blank=True, null=True)),
                ('eremark', models.TextField(blank=True, null=True)),
                ('admin_id', models.IntegerField(blank=True, null=True)),
                ('addtime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-addtime',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WorkExp',
            fields=[
                ('expid', models.AutoField(primary_key=True, serialize=False)),
                ('stime', models.DateField(blank=True, null=True)),
                ('etime', models.DateField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=150, null=True)),
                ('agency', models.CharField(blank=True, max_length=150, null=True)),
                ('position', models.CharField(blank=True, max_length=150, null=True)),
                ('duty', models.TextField(blank=True, null=True)),
                ('area', models.TextField(blank=True, null=True)),
                ('istonow', models.IntegerField(blank=True, null=True)),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experts.ExpertInfo')),
            ],
            options={
                'ordering': ('-etime', 'stime'),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ExpertComments',
            fields=[
                ('cmtid', models.AutoField(primary_key=True, serialize=False)),
                ('eproblem', models.TextField(blank=True, null=True)),
                ('ecomment', models.TextField(blank=True, null=True)),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experts.ExpertInfo')),
            ],
            options={
                'managed': True,
            },
        ),
    ]