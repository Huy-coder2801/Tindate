# Generated by Django 5.0.4 on 2024-05-06 00:07

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('bio', models.TextField(blank=True, default='', max_length=500)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('gender', models.CharField(choices=[('MAN', 'Man'), ('WOMAN', 'Woman'), ('NONBINARY', 'Nonbinary')], default='MALE', max_length=10)),
                ('pronouns', models.CharField(choices=[('HE/HIM/HIS', 'He/him/his'), ('SHE/HER/HERS', 'She/her/hers'), ('PREFER NOT TO SAY', 'Prefer not to say')], default='HE/HIM/HIS', max_length=20)),
                ('height', models.DecimalField(decimal_places=2, default=180.34, max_digits=10)),
                ('education', models.CharField(choices=[('HIGH SCHOOL', 'High School'), ('UNDERGRAD', 'Undergrad'), ('POSTGRAD', 'Postgrad'), ('PREFER NOT TO SAY', 'Prefer not to say')], default='HIGH SCHOOL', max_length=100)),
                ('birth_date', models.DateField(blank=True, default='1990-01-01', null=True)),
                ('sexuality', models.CharField(choices=[('PREFER NOT TO SAY', 'Prefer not to say'), ('STRAIGHT', 'Straight'), ('BISEXUAL', 'Bisexual'), ('GAY', 'Gay'), ('LESBIAN', 'Lesbian')], default='Straight', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
