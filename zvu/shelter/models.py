from django.db import models

# Create your models here.
class Dobrovolnik(models.Model):
    id_dobrovolnik = models.AutoField(primary_key=True)
    meno = models.CharField(max_length=255)
    priezvisko = models.CharField(max_length=255)
    datum_narodenia = models.DateField()
    doveryhodnost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Dobrovolnik'


class Pecovatel(models.Model):
    id_pecovatel = models.AutoField(primary_key=True)
    meno = models.CharField(max_length=255)
    priezvisko = models.CharField(max_length=255)
    datum_narodenia = models.DateField()

    class Meta:
        managed = False
        db_table = 'Pecovatel'


class Poziadavka(models.Model):
    id_poziadavky = models.AutoField(primary_key=True)
    datum_vytvorenia = models.DateField()
    obsah = models.CharField(max_length=255)
    stav = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Poziadavka'


class Rezervacia(models.Model):
    id_rezervacie = models.AutoField(primary_key=True)
    datum_vytvorenia = models.DateField()
    rezervovany_od = models.DateField()
    rezervovany_do = models.DateField()
    schvalenie = models.IntegerField()
    stav = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Rezervacia'


class Uzivatel(models.Model):
    id_uzivatel = models.AutoField(primary_key=True)
    typ = models.CharField(max_length=11)
    email = models.CharField(unique=True, max_length=255, db_collation='utf8mb4_unicode_520_ci')
    heslo = models.CharField(max_length=255, db_collation='utf8mb4_unicode_520_ci')
    aktivni = models.IntegerField()
    zamestnanec_id = models.PositiveIntegerField(blank=True, null=True)
    klient_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Uzivatel'


class Vencenie(models.Model):
    id_vencenia = models.AutoField(primary_key=True)
    venceny_od = models.DateField()
    venceny_do = models.DateField()

    class Meta:
        managed = False
        db_table = 'Vencenie'


class Veterinar(models.Model):
    id_veterinar = models.AutoField(primary_key=True)
    meno = models.CharField(max_length=255)
    priezvisko = models.CharField(max_length=255)
    datum_narodenia = models.DateField()

    class Meta:
        managed = False
        db_table = 'Veterinar'


class Zviera(models.Model):
    id_zviera = models.AutoField(primary_key=True)
    druh = models.CharField(max_length=255)
    meno = models.CharField(max_length=255)
    vek = models.PositiveIntegerField()
    datum_registracie = models.DateField()
    obrazok = models.CharField(max_length=255, db_collation='utf8mb4_unicode_520_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Zviera'


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