# Generated by Django 4.2.9 on 2024-02-28 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('content_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('main_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki_crawl.content')),
            ],
        ),
        migrations.CreateModel(
            name='InternalLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('anchor_text', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=20)),
                ('content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki_crawl.content')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('alt', models.CharField(max_length=200)),
                ('content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki_crawl.content')),
            ],
        ),
        migrations.CreateModel(
            name='ExternalLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('anchor_text', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=20)),
                ('content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki_crawl.content')),
            ],
        ),
    ]