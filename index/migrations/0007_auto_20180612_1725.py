# Generated by Django 2.0.2 on 2018-06-12 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20180612_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ManyToManyField(to='index.Category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='gallery/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(choices=[('Metropolis', 'Metropolis'), ('Gotham', 'Gotham'), ('Central City', 'Central City'), ('Avengers mansion', 'Avengers mansion'), ('Bifrost', 'Bifrost'), ('Wakanda', 'Wakanda')], max_length=120),
        ),
    ]
