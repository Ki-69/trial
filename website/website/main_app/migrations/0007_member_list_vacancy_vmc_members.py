# Generated by Django 4.2 on 2023-05-25 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_rename_classe_class_alter_tc_serial_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='member_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('designation', models.CharField(choices=[('principal', 'Principal'), ('pgt_physics', 'PGT (Physics)'), ('pgt_chemistry', 'PGT (Chemistry)'), ('pgt_maths', 'PGT (Maths)'), ('pgt_biology', 'PGT (Biology)'), ('pgt_computer', 'PGT (Computer)'), ('pgt_economics', 'PGT (Economics)'), ('pgt_commerce', 'PGT (Commerce)'), ('pgt_english', 'PGT (English)'), ('pgt_hindi', 'PGT (Hindi)'), ('tgt_science', 'TGT (Science)'), ('tgt_maths', 'TGT (Maths)'), ('tgt_sanskrit', 'TGT (Sanskrit)'), ('tgt_social_science', 'TGT (Social Science)'), ('tgt_english', 'TGT (English)'), ('tgt_hindi', 'TGT (Hindi)'), ('prt', 'PRT'), ('ssa', 'SSA'), ('lab_attendant', 'Lab Attendant'), ('sub_staff', 'Sub Staff'), ('jrsa', 'JR. Secratariat Assistant')], max_length=32)),
                ('origin', models.CharField(choices=[('local', 'Local'), ('indian', 'Indian')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('vacant_deignation', models.CharField(choices=[('principal', 'Principal'), ('pgt_physics', 'PGT (Physics)'), ('pgt_chemistry', 'PGT (Chemistry)'), ('pgt_maths', 'PGT (Maths)'), ('pgt_biology', 'PGT (Biology)'), ('pgt_computer', 'PGT (Computer)'), ('pgt_economics', 'PGT (Economics)'), ('pgt_commerce', 'PGT (Commerce)'), ('pgt_english', 'PGT (English)'), ('pgt_hindi', 'PGT (Hindi)'), ('tgt_science', 'TGT (Science)'), ('tgt_maths', 'TGT (Maths)'), ('tgt_sanskrit', 'TGT (Sanskrit)'), ('tgt_social_science', 'TGT (Social Science)'), ('tgt_english', 'TGT (English)'), ('tgt_hindi', 'TGT (Hindi)'), ('prt', 'PRT'), ('ssa', 'SSA'), ('lab_attendant', 'Lab Attendant'), ('sub_staff', 'Sub Staff'), ('jrsa', 'JR. Secratariat Assistant')], max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='VMC_members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('post', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=128)),
            ],
        ),
    ]
