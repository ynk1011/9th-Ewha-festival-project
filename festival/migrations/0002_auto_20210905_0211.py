# Generated by Django 3.2 on 2021-09-04 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('festival', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artpost',
            name='image',
        ),
        migrations.RemoveField(
            model_name='businesspost',
            name='image',
        ),
        migrations.RemoveField(
            model_name='convergencepost',
            name='image',
        ),
        migrations.RemoveField(
            model_name='edupost',
            name='image',
        ),
        migrations.RemoveField(
            model_name='engineeringpost',
            name='image',
        ),
        migrations.RemoveField(
            model_name='hokmapost',
            name='image',
        ),
        migrations.RemoveField(
            model_name='humanitiespost',
            name='image',
        ),
        migrations.RemoveField(
            model_name='musicpost',
            name='image',
        ),
        migrations.RemoveField(
            model_name='naturalpost',
            name='image',
        ),
        migrations.RemoveField(
            model_name='pharmacypost',
            name='image',
        ),
        migrations.RemoveField(
            model_name='scratonpost',
            name='image',
        ),
        migrations.RemoveField(
            model_name='socialpost',
            name='image',
        ),
        migrations.CreateModel(
            name='socialImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='boothImage/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='festival.socialpost')),
            ],
        ),
        migrations.CreateModel(
            name='scratonmage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='boothImage/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='festival.scratonpost')),
            ],
        ),
        migrations.CreateModel(
            name='pharmacyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='boothImage/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='festival.pharmacypost')),
            ],
        ),
        migrations.CreateModel(
            name='naturalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='boothImage/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='festival.naturalpost')),
            ],
        ),
        migrations.CreateModel(
            name='musicImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='boothImage/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='festival.musicpost')),
            ],
        ),
        migrations.CreateModel(
            name='humanitiesImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='boothImage/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='festival.humanitiespost')),
            ],
        ),
        migrations.CreateModel(
            name='hokmaImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='boothImage/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='festival.hokmapost')),
            ],
        ),
        migrations.CreateModel(
            name='engineeringImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='boothImage/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='festival.engineeringpost')),
            ],
        ),
        migrations.CreateModel(
            name='eduImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='boothImage/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='festival.edupost')),
            ],
        ),
        migrations.CreateModel(
            name='convergenceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='boothImage/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='festival.convergencepost')),
            ],
        ),
        migrations.CreateModel(
            name='businessImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='boothImage/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='festival.businesspost')),
            ],
        ),
        migrations.CreateModel(
            name='artImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='boothImage/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='festival.artpost')),
            ],
        ),
    ]
