# Generated by Django 4.2 on 2023-05-25 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_rename_vmc_members_vmc_member_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='website/images')),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Administrative_Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='website/files')),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='member_list',
            name='designation',
            field=models.CharField(choices=[('principal', 'Principal'), ('PGT (Physics)', 'PGT (Physics)'), ('PGT (Chemistry)', 'PGT (Chemistry)'), ('PGT (Maths)', 'PGT (Maths)'), ('PGT (Biology)', 'PGT (Biology)'), ('PGT (Computer)', 'PGT (Computer)'), ('PGT (Economics)', 'PGT (Economics)'), ('PGT (Commerce)', 'PGT (Commerce)'), ('PGT (English)', 'PGT (English)'), ('PGT (Hindi)', 'PGT (Hindi)'), ('TGT (Science)', 'TGT (Science)'), ('TGT (Maths)', 'TGT (Maths)'), ('TGT (Sanskrit)', 'TGT (Sanskrit)'), ('TGT (Social Science)', 'TGT (Social Science)'), ('TGT (English)', 'TGT (English)'), ('TGT (Hindi)', 'TGT (Hindi)'), ('PRT', 'PRT'), ('SSA', 'SSA'), ('Lab Attendant', 'Lab Attendant'), ('Sub Staff', 'Sub Staff'), ('JR. Secratariat Assistant', 'JR. Secratariat Assistant')], max_length=32),
        ),
        migrations.AlterField(
            model_name='member_list',
            name='origin',
            field=models.CharField(choices=[('Local', 'Local'), ('Indian', 'Indian')], max_length=6),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='vacant_designation',
            field=models.CharField(choices=[('principal', 'Principal'), ('PGT (Physics)', 'PGT (Physics)'), ('PGT (Chemistry)', 'PGT (Chemistry)'), ('PGT (Maths)', 'PGT (Maths)'), ('PGT (Biology)', 'PGT (Biology)'), ('PGT (Computer)', 'PGT (Computer)'), ('PGT (Economics)', 'PGT (Economics)'), ('PGT (Commerce)', 'PGT (Commerce)'), ('PGT (English)', 'PGT (English)'), ('PGT (Hindi)', 'PGT (Hindi)'), ('TGT (Science)', 'TGT (Science)'), ('TGT (Maths)', 'TGT (Maths)'), ('TGT (Sanskrit)', 'TGT (Sanskrit)'), ('TGT (Social Science)', 'TGT (Social Science)'), ('TGT (English)', 'TGT (English)'), ('TGT (Hindi)', 'TGT (Hindi)'), ('PRT', 'PRT'), ('SSA', 'SSA'), ('Lab Attendant', 'Lab Attendant'), ('Sub Staff', 'Sub Staff'), ('JR. Secratariat Assistant', 'JR. Secratariat Assistant')], max_length=32),
        ),
    ]
