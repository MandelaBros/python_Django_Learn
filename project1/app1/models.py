# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aozora(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ind = models.CharField(db_column='IND', max_length=10, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    book = models.CharField(db_column='BOOK', max_length=300, blank=True, null=True)  # Field name made lowercase.
    cmt = models.CharField(db_column='CMT', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aozora'


class App1Member(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app1_member'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Inputdata(models.Model):
    text = models.CharField(db_column='TEXT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    insert_date = models.DateTimeField(db_column='INSERT_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inputdata'


class Iseki(models.Model):
    ledger_id = models.CharField(db_column='LEDGER_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    manage_id = models.CharField(db_column='MANAGE_ID', max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    buillding_name = models.CharField(db_column='BUILLDING_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cultural_kind = models.CharField(db_column='CULTURAL_KIND', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kind1 = models.CharField(db_column='KIND1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kind2 = models.CharField(db_column='KIND2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='AGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    imp_clt_dgn_ymd = models.CharField(db_column='IMP_CLT_DGN_YMD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nat_trs_dgn_ymd = models.CharField(db_column='NAT_TRS_DGN_YMD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    prefectures = models.CharField(db_column='PREFECTURES', max_length=10, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    storage_name = models.CharField(db_column='STORAGE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    owner = models.CharField(db_column='OWNER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    manager = models.CharField(db_column='MANAGER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lat = models.CharField(db_column='LAT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lon = models.CharField(db_column='LON', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'iseki'
        unique_together = (('ledger_id', 'manage_id'),)


class Userdata(models.Model):
    name = models.CharField(db_column='NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    realpassword = models.CharField(db_column='REALPASSWORD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    insert_date = models.DateTimeField(db_column='INSERT_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userdata'
