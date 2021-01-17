# Generated by Django 3.1.2 on 2020-10-13 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albumin',
            options={'ordering': ['-date_time'], 'verbose_name': 'Albumin', 'verbose_name_plural': 'Albumin'},
        ),
        migrations.AlterModelOptions(
            name='alkaline_phosphatase',
            options={'ordering': ['-date_time'], 'verbose_name': 'Alkaline_Phosphatase', 'verbose_name_plural': 'Alkaline_Phosphatase'},
        ),
        migrations.AlterModelOptions(
            name='baseline_survey',
            options={'ordering': ['-date_time'], 'verbose_name': 'Baseline_Survey', 'verbose_name_plural': 'Baseline_Survey'},
        ),
        migrations.AlterModelOptions(
            name='bicarbonate',
            options={'ordering': ['-date_time'], 'verbose_name': 'Bicarbonate', 'verbose_name_plural': 'Bicarbonate'},
        ),
        migrations.AlterModelOptions(
            name='bun',
            options={'ordering': ['-date_time'], 'verbose_name': 'BUN', 'verbose_name_plural': 'BUN'},
        ),
        migrations.AlterModelOptions(
            name='calcium',
            options={'ordering': ['-date_time'], 'verbose_name': 'Calcium', 'verbose_name_plural': 'Calcium'},
        ),
        migrations.AlterModelOptions(
            name='comorbidities',
            options={'ordering': ['-date_time'], 'verbose_name': 'Comorbidities', 'verbose_name_plural': 'Comorbidities'},
        ),
        migrations.AlterModelOptions(
            name='creatinine',
            options={'ordering': ['-date_time'], 'verbose_name': 'Creatinine', 'verbose_name_plural': 'Creatinine'},
        ),
        migrations.AlterModelOptions(
            name='demography',
            options={'ordering': ['-date_time'], 'verbose_name': 'Demography', 'verbose_name_plural': 'Demography'},
        ),
        migrations.AlterModelOptions(
            name='dialysis',
            options={'ordering': ['-date_time'], 'verbose_name': 'Dialysis', 'verbose_name_plural': 'Dialysis'},
        ),
        migrations.AlterModelOptions(
            name='hemoglobin',
            options={'ordering': ['-date_time'], 'verbose_name': 'Hemoglobin', 'verbose_name_plural': 'Hemoglobin'},
        ),
        migrations.AlterModelOptions(
            name='medical_info',
            options={'ordering': ['-date_time'], 'verbose_name': 'Medical_Info', 'verbose_name_plural': 'Medical_Info'},
        ),
        migrations.AlterModelOptions(
            name='phosphorus',
            options={'ordering': ['-date_time'], 'verbose_name': 'Phosphorus', 'verbose_name_plural': 'Phosphorus'},
        ),
        migrations.AlterModelOptions(
            name='potassium',
            options={'ordering': ['-date_time'], 'verbose_name': 'Potassium', 'verbose_name_plural': 'Potassium'},
        ),
        migrations.AlterModelOptions(
            name='pth',
            options={'ordering': ['-date_time'], 'verbose_name': 'PTH', 'verbose_name_plural': 'PTH'},
        ),
        migrations.AlterModelOptions(
            name='sodium',
            options={'ordering': ['-date_time'], 'verbose_name': 'Sodium', 'verbose_name_plural': 'Sodium'},
        ),
        migrations.AlterModelOptions(
            name='third_month_survey',
            options={'ordering': ['-date_time'], 'verbose_name': 'Third_Month_Survey', 'verbose_name_plural': 'Third_Month_Survey'},
        ),
    ]
