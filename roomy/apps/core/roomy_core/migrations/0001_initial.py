# Generated by Django 3.0.1 on 2020-01-27 20:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.ImageField(upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=56)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('fee_type', models.IntegerField(choices=[(0, 'Misc Fees'), (1, 'Add-ons')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('img_path', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
            options={
                'unique_together': {('title', 'img_path')},
            },
        ),
        migrations.CreateModel(
            name='OwnerAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateTimeField(blank=True, null=True)),
                ('cell_number', models.PositiveIntegerField(blank=True, null=True)),
                ('provincial_address', models.CharField(blank=True, max_length=128, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.IntegerField(choices=[(0, 'Condominium'), (1, 'Apartment'), (2, 'Dormitory')], default=0)),
                ('name', models.CharField(max_length=56, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('property_address', models.CharField(blank=True, max_length=256, null=True)),
                ('owner_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='roomy_core.OwnerAccount')),
                ('property_image', models.ManyToManyField(blank=True, related_name='property_image', to='roomy_core.ImageFile')),
            ],
            options={
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('rating', models.PositiveIntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('rating_description', models.TextField(blank=True, null=True)),
                ('rated', models.BooleanField(default=False)),
                ('add_ons', models.ManyToManyField(blank=True, to='roomy_core.Fee')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomy_core.Room')),
            ],
        ),
        migrations.CreateModel(
            name='TenantAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateTimeField(blank=True, null=True)),
                ('cell_number', models.PositiveIntegerField(blank=True, null=True)),
                ('provincial_address', models.CharField(blank=True, max_length=128, null=True)),
                ('transaction_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='roomy_core.Transaction')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoomCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=56, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('floor', models.PositiveIntegerField(default=1)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=9)),
                ('room_type', models.IntegerField(choices=[(0, 'Fixed Rate'), (1, 'Submetered')], default=0)),
                ('img_2d', models.ManyToManyField(blank=True, related_name='img_2d', to='roomy_core.ImageFile')),
                ('img_3d', models.ManyToManyField(blank=True, related_name='img_3d', to='roomy_core.ImageFile')),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomy_core.Property')),
            ],
            options={
                'unique_together': {('property_id', 'name')},
            },
        ),
        migrations.AddField(
            model_name='room',
            name='catalog_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='roomy_core.RoomCatalog'),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=56)),
                ('description', models.TextField(blank=True, null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Processed'), (2, 'Denied')], default=0)),
                ('transaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomy_core.Transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('body', models.TextField(blank=True, null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('sent', models.BooleanField(default=False)),
                ('read', models.BooleanField(default=False)),
                ('tenant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomy_core.TenantAccount')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('inside', models.BooleanField(default=True)),
                ('transaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomy_core.Transaction')),
            ],
        ),
        migrations.AddField(
            model_name='fee',
            name='property_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='roomy_core.Property'),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField()),
                ('description', models.CharField(max_length=56)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomy_core.Property')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=56, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Denied')], default=0)),
                ('add_ons', models.ManyToManyField(blank=True, to='roomy_core.Fee')),
                ('catalog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomy_core.RoomCatalog')),
                ('document1_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document1', to='roomy_core.Document')),
                ('document2_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document2', to='roomy_core.Document')),
                ('tenant_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='roomy_core.TenantAccount')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateField(blank=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('billing_fee', models.ManyToManyField(blank=True, to='roomy_core.Fee')),
                ('transaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomy_core.Transaction')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='room',
            unique_together={('catalog_id', 'number')},
        ),
        migrations.AlterUniqueTogether(
            name='fee',
            unique_together={('description', 'amount')},
        ),
    ]
