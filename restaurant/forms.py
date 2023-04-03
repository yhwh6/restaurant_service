from django.db import migrations, models

from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='cooks',
        ),
        migrations.AddField(
            model_name='dish',
            name='cooks',
            field=models.ManyToManyField(related_name='dishes', to=settings.AUTH_USER_MODEL),
        ),
    ]
