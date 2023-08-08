# Generated by Django 4.1.10 on 2023-08-08 15:00

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('airss', '0004_rssfeedsource_require_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='FetchedNews',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('feed_id', models.TextField()),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airss.rssfeedsource')),
            ],
        ),
    ]
