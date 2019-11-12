from django.db import models, connection


# Create your models here.
class SMenu(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=256)
    type = models.IntegerField()
    pid = models.IntegerField()
    sort = models.IntegerField()
    icon = models.CharField(max_length=20)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 's_menu'


class SRole(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 's_role'


class SRoleMenu(models.Model):
    role_id = models.IntegerField()
    menu_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 's_role_menu'


class SUser(models.Model):
    user_code = models.CharField(unique=True, max_length=10)
    password = models.CharField(max_length=50)
    user_type = models.IntegerField()
    status = models.IntegerField()
    user_name = models.CharField(max_length=10)
    english_name = models.CharField(max_length=10)
    sex = models.IntegerField()
    post = models.CharField(max_length=20)
    hiredate = models.BigIntegerField()
    contact_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    education = models.IntegerField()
    birthday = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=100)
    create_time = models.BigIntegerField()
    create_user_id = models.BigIntegerField()
    modify_time = models.BigIntegerField()
    modify_user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 's_user'


class SUserAuth(models.Model):
    user_id = models.IntegerField()
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 's_user_auth'


class TArticle(models.Model):
    title = models.CharField(max_length=100)
    column_id = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    releas_time = models.BigIntegerField()
    status = models.IntegerField()
    sort = models.IntegerField()
    recommend = models.IntegerField()
    create_time = models.BigIntegerField()
    create_user_id = models.IntegerField()
    modify_time = models.BigIntegerField()
    modify_user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_article'


class TColumn(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    pid = models.IntegerField()
    sort = models.IntegerField()
    status = models.IntegerField()
    type = models.IntegerField()
    style = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 't_column'


class TImage(models.Model):
    title = models.CharField(max_length=50)
    type = models.IntegerField()
    url = models.CharField(max_length=256)
    sort = models.IntegerField()
    href = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 't_image'

def do_save_info(username,password):
    with connection.cursor() as cursor:
        try:
            cursor.execute('insert into t_article(title,content) values(%s,%s)'%(username,password))
            print('yes')
        except:
            print('no')
