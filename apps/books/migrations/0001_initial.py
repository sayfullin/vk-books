# Generated by Django 2.1 on 2019-11-23 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_account_locale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('source', models.SmallIntegerField(choices=[(0, 'custom'), (1, 'google')], default=0)),
                ('external_id', models.CharField(max_length=255, null=True, unique=True)),
                ('image', models.ImageField(null=True, upload_to='books/')),
                ('image_external_url', models.URLField(blank=True, max_length=512, null=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'active'), (1, 'not active'), (2, 'deleted')], default=0)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='accounts.Account')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='BookAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_type', models.SmallIntegerField(choices=[(0, 'add'), (1, 'activate'), (2, 'deactivate'), (3, 'update_comment'), (4, 'delete')])),
                ('dump', models.TextField(verbose_name='Dump')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('vk_session', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.VkSession')),
            ],
        ),
    ]
