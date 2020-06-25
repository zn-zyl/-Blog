from django.db import models


# Create your models here.

# 一个mysql软件中，可以有多个数据库
# 一个数据库中，可以有多张数据库表
# 一张数据表中 ，有多条数据（多条记录）以及多个字段（多个列）

# 1. 可以在子应用projects/modes.py文件中，来定义数据模型 创建模型类，通过模型类来自动创建数据库表
# 2.一个数据模型类对应一个数据表
# 3.数据模型类 需要继承Model父类或者Model子类
# 4.在数据模型类中，添加的类属性（Field对象）来对应数据表中的字段
# 5.创建完数据库模型类之后，需要迁移才能生成数据表
# a.生成迁移脚本放在projects/migrations目录中:python manage.py makemigrations
# b.执行迁移脚本：python manage.py migrate
# c.如果不添加选项，会将所有的子应用迁移
# 6.会自动创建字段名为id的类属性，自增 主键 非空
class Projects(models.Model):
    # 7.只要某一字段中primary_key=True, 那么django中就不会自动创建id字段，会使用自定义 AutoField自增
    # 8.CharField >varchar IntegerField > int  TextField > text
    id = models.AutoField(primary_key=True)
    # 9.verbose_name：个性化信息
    # 10.help_text：帮助文本信息 在api接口文档平台和admin后端站点中会用于提示往往和verbose_name一致
    # 11.unique用于指定唯一键 默认为False
    # 12.CharField至少要指定一个max_length必传参数，代表此字段的最大长度，不能为负数
    name = models.CharField(max_length=200, verbose_name="项目名称", help_text="项目名称", unique=True)
    leader = models.CharField(max_length=50, verbose_name="项目负责人", help_text="项目负责人")
    tester = models.CharField(max_length=50, verbose_name="测试人员", help_text="测试人员")
    programmer = models.CharField(max_length=50, verbose_name="开发人员", help_text="开发人员")
    # 13.null 指定数据在保存时是否可以为空，默认不能为空 如果null=True 可以为空
    # 14.blank 指定前端用户在创建数据时，是否需要传递,默认需要传递 如果blank=True,可以不传递
    # 15.default为魔衣字段指定默认值 往往会跟blank一起使用
    desc = models.TextField(verbose_name="项目简介", help_text="项目简介", null=True, default="xxxx简介", blank=True)
    # 16.DateTimeField 可以添加auto_now_add选项，django会自动添加创建记录时的时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    # 17.DateTimeField 可以添加auto_now选项，django会自动添加更新记录时的时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="更新时间")

    # 18. 执行迁移脚本之后，生成的数据表名默认为子应用名_模型类名小写

    class Meta:
        # 19.可以在模型类下定义Meta子类 子类名称固定
        # 20.可以使用db_table属性来指定表明
        db_table = "tb_projects"
        # 21.指定表的个性化描述
        verbose_name = "项目表"


    # 删除表重新迁移步骤 1.删除migrations下面的迁移脚本 2.删除数据库里的表 3.删除数据库里Django_migration表里有关子应用的迁移记录
