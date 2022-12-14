# Generated by Django 4.1 on 2022-10-30 12:24

from django.db import migrations

def authorize_pharmacy_to_admin(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Pharmacy = apps.get_model('pharmacy', 'Pharmacy')
    group, created = Group.objects.get_or_create(name='app_admin')
    content_type = ContentType.objects.get_for_model(Pharmacy)
    permissions = list(Permission.objects.filter(content_type=content_type))
    for permission in permissions:
        group.permissions.add(permission)


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length')
    ]

    operations = [
        migrations.RunPython(authorize_pharmacy_to_admin)
    ]
