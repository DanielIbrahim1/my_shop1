# Generated by Django 4.0.6 on 2022-08-06 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0005_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('catId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.categoriy')),
                ('prodId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
