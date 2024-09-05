# Generated by Django 4.1.1 on 2023-01-02 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='itemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='试题类型名称')),
            ],
            options={
                'verbose_name': '试题类型',
                'verbose_name_plural': '试题类型',
            },
        ),
        migrations.CreateModel(
            name='paperTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='试卷模板名称')),
                ('date', models.DateTimeField(verbose_name='制卷时间')),
                ('typeOneCount', models.PositiveSmallIntegerField(default=40, verbose_name='单项选择题数量')),
                ('typeOneScore', models.DecimalField(decimal_places=1, default=1, max_digits=3, verbose_name='单项选择题分值')),
                ('typeTwoCount', models.PositiveSmallIntegerField(default=3, verbose_name='基本操作题数量')),
                ('typeTwoScore', models.DecimalField(decimal_places=1, default=5, max_digits=3, verbose_name='基本操作题分值')),
                ('typeThreeCount', models.PositiveSmallIntegerField(default=2, verbose_name='简单应用题数量')),
                ('typeThreeScore', models.DecimalField(decimal_places=1, default=12.5, max_digits=3, verbose_name='简单应用题分值')),
                ('typeFourCount', models.PositiveSmallIntegerField(default=1, verbose_name='综合应用题数量')),
                ('typeFourScore', models.DecimalField(decimal_places=1, default=20, max_digits=3, verbose_name='综合应用题分值')),
            ],
            options={
                'verbose_name': '试题模板',
                'verbose_name_plural': '试题模板',
            },
        ),
        migrations.CreateModel(
            name='testItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=600, verbose_name='试题题干')),
                ('options', models.TextField(blank=True, max_length=600, null=True, verbose_name='试题选项')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='picssss', verbose_name='试题图片')),
                ('answer', models.TextField(max_length=1000, verbose_name='参考答案')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ItemPool.itemtype', verbose_name='试题类型')),
            ],
            options={
                'verbose_name': '试题',
                'verbose_name_plural': '试题',
            },
        ),
        migrations.CreateModel(
            name='paperContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='试卷名称')),
                ('content', models.TextField(max_length=400, verbose_name='试题ID列表')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ItemPool.papertemplate', verbose_name='试卷模板')),
            ],
            options={
                'verbose_name': '试题内容',
                'verbose_name_plural': '试题内容',
            },
        ),
    ]
