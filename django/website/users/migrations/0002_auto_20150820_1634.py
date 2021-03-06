# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='area_of_specialisation',
            field=models.CharField(max_length=128, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='business_address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='business_email',
            field=models.EmailField(default='user@example.com', unique=True, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='business_tel',
            field=models.CharField(max_length=20, verbose_name=b'Business telephone', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='contact_type',
            field=models.CharField(default='None', max_length=32, verbose_name=b'Type of Contact'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, help_text=b'The country in which the contact is currently working in', max_length=64, choices=[(b'Member countries', ((b'BW', b'Botswana'), (b'BI', b'Burundi'), (b'CD', b'Congo - Kinshasa'), (b'ET', b'Ethiopia'), (b'KE', b'Kenya'), (b'LS', b'Lesotho'), (b'MW', b'Malawi'), (b'MZ', b'Mozambique'), (b'NA', b'Namibia'), (b'RW', b'Rwanda'), (b'ZA', b'South Africa'), (b'SD', b'Sudan'), (b'SS', b'South Sudan'), (b'SZ', b'Swaziland'), (b'TZ', b'Tanzania'), (b'UG', b'Uganda'), (b'ZM', b'Zambia'), (b'ZW', b'Zimbabwe'))), (b'Rest of the world', ((b'AF', b'Afghanistan'), (b'AL', b'Albania'), (b'DZ', b'Algeria'), (b'AS', b'American Samoa'), (b'AD', b'Andorra'), (b'AO', b'Angola'), (b'AI', b'Anguilla'), (b'AQ', b'Antarctica'), (b'AG', b'Antigua and Barbuda'), (b'AR', b'Argentina'), (b'AM', b'Armenia'), (b'AW', b'Aruba'), (b'AU', b'Australia'), (b'AT', b'Austria'), (b'AZ', b'Azerbaijan'), (b'BS', b'Bahamas'), (b'BH', b'Bahrain'), (b'BD', b'Bangladesh'), (b'BB', b'Barbados'), (b'BY', b'Belarus'), (b'BE', b'Belgium'), (b'BZ', b'Belize'), (b'BJ', b'Benin'), (b'BM', b'Bermuda'), (b'BT', b'Bhutan'), (b'BO', b'Bolivia'), (b'BA', b'Bosnia and Herzegovina'), (b'BV', b'Bouvet Island'), (b'BR', b'Brazil'), (b'BQ', b'British Antarctic Territory'), (b'IO', b'British Indian Ocean Territory'), (b'VG', b'British Virgin Islands'), (b'BN', b'Brunei'), (b'BG', b'Bulgaria'), (b'BF', b'Burkina Faso'), (b'KH', b'Cambodia'), (b'CM', b'Cameroon'), (b'CA', b'Canada'), (b'CT', b'Canton and Enderbury Islands'), (b'CV', b'Cape Verde'), (b'KY', b'Cayman Islands'), (b'CF', b'Central African Republic'), (b'TD', b'Chad'), (b'CL', b'Chile'), (b'CN', b'China'), (b'CX', b'Christmas Island'), (b'CC', b'Cocos [Keeling] Islands'), (b'CO', b'Colombia'), (b'KM', b'Comoros'), (b'CG', b'Congo - Brazzaville'), (b'CK', b'Cook Islands'), (b'CR', b'Costa Rica'), (b'HR', b'Croatia'), (b'CU', b'Cuba'), (b'CY', b'Cyprus'), (b'CZ', b'Czech Republic'), (b'CI', b'C\xc3\xb4te d\xe2\x80\x99Ivoire'), (b'DK', b'Denmark'), (b'DJ', b'Djibouti'), (b'DM', b'Dominica'), (b'DO', b'Dominican Republic'), (b'NQ', b'Dronning Maud Land'), (b'DD', b'East Germany'), (b'EC', b'Ecuador'), (b'EG', b'Egypt'), (b'SV', b'El Salvador'), (b'GQ', b'Equatorial Guinea'), (b'ER', b'Eritrea'), (b'EE', b'Estonia'), (b'FK', b'Falkland Islands'), (b'FO', b'Faroe Islands'), (b'FJ', b'Fiji'), (b'FI', b'Finland'), (b'FR', b'France'), (b'GF', b'French Guiana'), (b'PF', b'French Polynesia'), (b'TF', b'French Southern Territories'), (b'FQ', b'French Southern and Antarctic Territories'), (b'GA', b'Gabon'), (b'GM', b'Gambia'), (b'GE', b'Georgia'), (b'DE', b'Germany'), (b'GH', b'Ghana'), (b'GI', b'Gibraltar'), (b'GR', b'Greece'), (b'GL', b'Greenland'), (b'GD', b'Grenada'), (b'GP', b'Guadeloupe'), (b'GU', b'Guam'), (b'GT', b'Guatemala'), (b'GG', b'Guernsey'), (b'GN', b'Guinea'), (b'GW', b'Guinea-Bissau'), (b'GY', b'Guyana'), (b'HT', b'Haiti'), (b'HM', b'Heard Island and McDonald Islands'), (b'HN', b'Honduras'), (b'HK', b'Hong Kong SAR China'), (b'HU', b'Hungary'), (b'IS', b'Iceland'), (b'IN', b'India'), (b'ID', b'Indonesia'), (b'IR', b'Iran'), (b'IQ', b'Iraq'), (b'IE', b'Ireland'), (b'IM', b'Isle of Man'), (b'IL', b'Israel'), (b'IT', b'Italy'), (b'JM', b'Jamaica'), (b'JP', b'Japan'), (b'JE', b'Jersey'), (b'JT', b'Johnston Island'), (b'JO', b'Jordan'), (b'KZ', b'Kazakhstan'), (b'KI', b'Kiribati'), (b'KW', b'Kuwait'), (b'KG', b'Kyrgyzstan'), (b'LA', b'Laos'), (b'LV', b'Latvia'), (b'LB', b'Lebanon'), (b'LR', b'Liberia'), (b'LY', b'Libya'), (b'LI', b'Liechtenstein'), (b'LT', b'Lithuania'), (b'LU', b'Luxembourg'), (b'MO', b'Macau SAR China'), (b'MK', b'Macedonia'), (b'MG', b'Madagascar'), (b'MY', b'Malaysia'), (b'MV', b'Maldives'), (b'ML', b'Mali'), (b'MT', b'Malta'), (b'MH', b'Marshall Islands'), (b'MQ', b'Martinique'), (b'MR', b'Mauritania'), (b'MU', b'Mauritius'), (b'YT', b'Mayotte'), (b'FX', b'Metropolitan France'), (b'MX', b'Mexico'), (b'FM', b'Micronesia'), (b'MI', b'Midway Islands'), (b'MD', b'Moldova'), (b'MC', b'Monaco'), (b'MN', b'Mongolia'), (b'ME', b'Montenegro'), (b'MS', b'Montserrat'), (b'MA', b'Morocco'), (b'MM', b'Myanmar [Burma]'), (b'NR', b'Nauru'), (b'NP', b'Nepal'), (b'NL', b'Netherlands'), (b'AN', b'Netherlands Antilles'), (b'NT', b'Neutral Zone'), (b'NC', b'New Caledonia'), (b'NZ', b'New Zealand'), (b'NI', b'Nicaragua'), (b'NE', b'Niger'), (b'NG', b'Nigeria'), (b'NU', b'Niue'), (b'NF', b'Norfolk Island'), (b'KP', b'North Korea'), (b'VD', b'North Vietnam'), (b'MP', b'Northern Mariana Islands'), (b'NO', b'Norway'), (b'OM', b'Oman'), (b'PC', b'Pacific Islands Trust Territory'), (b'PK', b'Pakistan'), (b'PW', b'Palau'), (b'PS', b'Palestinian Territories'), (b'PA', b'Panama'), (b'PZ', b'Panama Canal Zone'), (b'PG', b'Papua New Guinea'), (b'PY', b'Paraguay'), (b'YD', b"People's Democratic Republic of Yemen"), (b'PE', b'Peru'), (b'PH', b'Philippines'), (b'PN', b'Pitcairn Islands'), (b'PL', b'Poland'), (b'PT', b'Portugal'), (b'PR', b'Puerto Rico'), (b'QA', b'Qatar'), (b'RO', b'Romania'), (b'RU', b'Russia'), (b'RE', b'R\xc3\xa9union'), (b'BL', b'Saint Barth\xc3\xa9lemy'), (b'SH', b'Saint Helena'), (b'KN', b'Saint Kitts and Nevis'), (b'LC', b'Saint Lucia'), (b'MF', b'Saint Martin'), (b'PM', b'Saint Pierre and Miquelon'), (b'VC', b'Saint Vincent and the Grenadines'), (b'WS', b'Samoa'), (b'SM', b'San Marino'), (b'SA', b'Saudi Arabia'), (b'SN', b'Senegal'), (b'RS', b'Serbia'), (b'CS', b'Serbia and Montenegro'), (b'SC', b'Seychelles'), (b'SL', b'Sierra Leone'), (b'SG', b'Singapore'), (b'SK', b'Slovakia'), (b'SI', b'Slovenia'), (b'SB', b'Solomon Islands'), (b'SO', b'Somalia'), (b'GS', b'South Georgia and the South Sandwich Islands'), (b'KR', b'South Korea'), (b'ES', b'Spain'), (b'LK', b'Sri Lanka'), (b'SR', b'Suriname'), (b'SJ', b'Svalbard and Jan Mayen'), (b'SE', b'Sweden'), (b'CH', b'Switzerland'), (b'SY', b'Syria'), (b'ST', b'S\xc3\xa3o Tom\xc3\xa9 and Pr\xc3\xadncipe'), (b'TW', b'Taiwan'), (b'TJ', b'Tajikistan'), (b'TH', b'Thailand'), (b'TL', b'Timor-Leste'), (b'TG', b'Togo'), (b'TK', b'Tokelau'), (b'TO', b'Tonga'), (b'TT', b'Trinidad and Tobago'), (b'TN', b'Tunisia'), (b'TR', b'Turkey'), (b'TM', b'Turkmenistan'), (b'TC', b'Turks and Caicos Islands'), (b'TV', b'Tuvalu'), (b'UM', b'U.S. Minor Outlying Islands'), (b'PU', b'U.S. Miscellaneous Pacific Islands'), (b'VI', b'U.S. Virgin Islands'), (b'UA', b'Ukraine'), (b'SU', b'Union of Soviet Socialist Republics'), (b'AE', b'United Arab Emirates'), (b'GB', b'United Kingdom'), (b'US', b'United States'), (b'ZZ', b'Unknown or Invalid Region'), (b'UY', b'Uruguay'), (b'UZ', b'Uzbekistan'), (b'VU', b'Vanuatu'), (b'VA', b'Vatican City'), (b'VE', b'Venezuela'), (b'VN', b'Vietnam'), (b'WK', b'Wake Island'), (b'WF', b'Wallis and Futuna'), (b'EH', b'Western Sahara'), (b'YE', b'Yemen'), (b'AX', b'\xc3\x85land Islands')))]),
        ),
        migrations.AddField(
            model_name='user',
            name='fax',
            field=models.CharField(max_length=20, verbose_name=b'Fax no', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default='male', max_length=6, choices=[(b'female', b'Female'), (b'male', b'Male')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='home_address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='home_tel',
            field=models.CharField(max_length=20, verbose_name=b'Home telephone', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='job_title',
            field=models.CharField(max_length=64, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='msn_id',
            field=models.CharField(max_length=32, verbose_name=b'MSN ID', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nationality',
            field=models.CharField(blank=True, max_length=64, choices=[(b'Member countries', [(b'Botswana', b'Botswana'), (b'Burundi', b'Burundi'), (b'Congo - Kinshasa', b'Congo - Kinshasa'), (b'Ethiopia', b'Ethiopia'), (b'Kenya', b'Kenya'), (b'Lesotho', b'Lesotho'), (b'Malawi', b'Malawi'), (b'Mozambique', b'Mozambique'), (b'Namibia', b'Namibia'), (b'Rwanda', b'Rwanda'), (b'South Africa', b'South Africa'), (b'Sudan', b'Sudan'), (b'South Sudan', b'South Sudan'), (b'Swaziland', b'Swaziland'), (b'Tanzania', b'Tanzania'), (b'Uganda', b'Uganda'), (b'Zambia', b'Zambia'), (b'Zimbabwe', b'Zimbabwe')]), (b'Rest of the world', [(b'Afghanistan', b'Afghanistan'), (b'Albania', b'Albania'), (b'Algeria', b'Algeria'), (b'American Samoa', b'American Samoa'), (b'Andorra', b'Andorra'), (b'Angola', b'Angola'), (b'Anguilla', b'Anguilla'), (b'Antarctica', b'Antarctica'), (b'Antigua and Barbuda', b'Antigua and Barbuda'), (b'Argentina', b'Argentina'), (b'Armenia', b'Armenia'), (b'Aruba', b'Aruba'), (b'Australia', b'Australia'), (b'Austria', b'Austria'), (b'Azerbaijan', b'Azerbaijan'), (b'Bahamas', b'Bahamas'), (b'Bahrain', b'Bahrain'), (b'Bangladesh', b'Bangladesh'), (b'Barbados', b'Barbados'), (b'Belarus', b'Belarus'), (b'Belgium', b'Belgium'), (b'Belize', b'Belize'), (b'Benin', b'Benin'), (b'Bermuda', b'Bermuda'), (b'Bhutan', b'Bhutan'), (b'Bolivia', b'Bolivia'), (b'Bosnia and Herzegovina', b'Bosnia and Herzegovina'), (b'Bouvet Island', b'Bouvet Island'), (b'Brazil', b'Brazil'), (b'British Antarctic Territory', b'British Antarctic Territory'), (b'British Indian Ocean Territory', b'British Indian Ocean Territory'), (b'British Virgin Islands', b'British Virgin Islands'), (b'Brunei', b'Brunei'), (b'Bulgaria', b'Bulgaria'), (b'Burkina Faso', b'Burkina Faso'), (b'Cambodia', b'Cambodia'), (b'Cameroon', b'Cameroon'), (b'Canada', b'Canada'), (b'Canton and Enderbury Islands', b'Canton and Enderbury Islands'), (b'Cape Verde', b'Cape Verde'), (b'Cayman Islands', b'Cayman Islands'), (b'Central African Republic', b'Central African Republic'), (b'Chad', b'Chad'), (b'Chile', b'Chile'), (b'China', b'China'), (b'Christmas Island', b'Christmas Island'), (b'Cocos [Keeling] Islands', b'Cocos [Keeling] Islands'), (b'Colombia', b'Colombia'), (b'Comoros', b'Comoros'), (b'Congo - Brazzaville', b'Congo - Brazzaville'), (b'Cook Islands', b'Cook Islands'), (b'Costa Rica', b'Costa Rica'), (b'Croatia', b'Croatia'), (b'Cuba', b'Cuba'), (b'Cyprus', b'Cyprus'), (b'Czech Republic', b'Czech Republic'), (b'C\xc3\xb4te d\xe2\x80\x99Ivoire', b'C\xc3\xb4te d\xe2\x80\x99Ivoire'), (b'Denmark', b'Denmark'), (b'Djibouti', b'Djibouti'), (b'Dominica', b'Dominica'), (b'Dominican Republic', b'Dominican Republic'), (b'Dronning Maud Land', b'Dronning Maud Land'), (b'East Germany', b'East Germany'), (b'Ecuador', b'Ecuador'), (b'Egypt', b'Egypt'), (b'El Salvador', b'El Salvador'), (b'Equatorial Guinea', b'Equatorial Guinea'), (b'Eritrea', b'Eritrea'), (b'Estonia', b'Estonia'), (b'Falkland Islands', b'Falkland Islands'), (b'Faroe Islands', b'Faroe Islands'), (b'Fiji', b'Fiji'), (b'Finland', b'Finland'), (b'France', b'France'), (b'French Guiana', b'French Guiana'), (b'French Polynesia', b'French Polynesia'), (b'French Southern Territories', b'French Southern Territories'), (b'French Southern and Antarctic Territories', b'French Southern and Antarctic Territories'), (b'Gabon', b'Gabon'), (b'Gambia', b'Gambia'), (b'Georgia', b'Georgia'), (b'Germany', b'Germany'), (b'Ghana', b'Ghana'), (b'Gibraltar', b'Gibraltar'), (b'Greece', b'Greece'), (b'Greenland', b'Greenland'), (b'Grenada', b'Grenada'), (b'Guadeloupe', b'Guadeloupe'), (b'Guam', b'Guam'), (b'Guatemala', b'Guatemala'), (b'Guernsey', b'Guernsey'), (b'Guinea', b'Guinea'), (b'Guinea-Bissau', b'Guinea-Bissau'), (b'Guyana', b'Guyana'), (b'Haiti', b'Haiti'), (b'Heard Island and McDonald Islands', b'Heard Island and McDonald Islands'), (b'Honduras', b'Honduras'), (b'Hong Kong SAR China', b'Hong Kong SAR China'), (b'Hungary', b'Hungary'), (b'Iceland', b'Iceland'), (b'India', b'India'), (b'Indonesia', b'Indonesia'), (b'Iran', b'Iran'), (b'Iraq', b'Iraq'), (b'Ireland', b'Ireland'), (b'Isle of Man', b'Isle of Man'), (b'Israel', b'Israel'), (b'Italy', b'Italy'), (b'Jamaica', b'Jamaica'), (b'Japan', b'Japan'), (b'Jersey', b'Jersey'), (b'Johnston Island', b'Johnston Island'), (b'Jordan', b'Jordan'), (b'Kazakhstan', b'Kazakhstan'), (b'Kiribati', b'Kiribati'), (b'Kuwait', b'Kuwait'), (b'Kyrgyzstan', b'Kyrgyzstan'), (b'Laos', b'Laos'), (b'Latvia', b'Latvia'), (b'Lebanon', b'Lebanon'), (b'Liberia', b'Liberia'), (b'Libya', b'Libya'), (b'Liechtenstein', b'Liechtenstein'), (b'Lithuania', b'Lithuania'), (b'Luxembourg', b'Luxembourg'), (b'Macau SAR China', b'Macau SAR China'), (b'Macedonia', b'Macedonia'), (b'Madagascar', b'Madagascar'), (b'Malaysia', b'Malaysia'), (b'Maldives', b'Maldives'), (b'Mali', b'Mali'), (b'Malta', b'Malta'), (b'Marshall Islands', b'Marshall Islands'), (b'Martinique', b'Martinique'), (b'Mauritania', b'Mauritania'), (b'Mauritius', b'Mauritius'), (b'Mayotte', b'Mayotte'), (b'Metropolitan France', b'Metropolitan France'), (b'Mexico', b'Mexico'), (b'Micronesia', b'Micronesia'), (b'Midway Islands', b'Midway Islands'), (b'Moldova', b'Moldova'), (b'Monaco', b'Monaco'), (b'Mongolia', b'Mongolia'), (b'Montenegro', b'Montenegro'), (b'Montserrat', b'Montserrat'), (b'Morocco', b'Morocco'), (b'Myanmar [Burma]', b'Myanmar [Burma]'), (b'Nauru', b'Nauru'), (b'Nepal', b'Nepal'), (b'Netherlands', b'Netherlands'), (b'Netherlands Antilles', b'Netherlands Antilles'), (b'Neutral Zone', b'Neutral Zone'), (b'New Caledonia', b'New Caledonia'), (b'New Zealand', b'New Zealand'), (b'Nicaragua', b'Nicaragua'), (b'Niger', b'Niger'), (b'Nigeria', b'Nigeria'), (b'Niue', b'Niue'), (b'Norfolk Island', b'Norfolk Island'), (b'North Korea', b'North Korea'), (b'North Vietnam', b'North Vietnam'), (b'Northern Mariana Islands', b'Northern Mariana Islands'), (b'Norway', b'Norway'), (b'Oman', b'Oman'), (b'Pacific Islands Trust Territory', b'Pacific Islands Trust Territory'), (b'Pakistan', b'Pakistan'), (b'Palau', b'Palau'), (b'Palestinian Territories', b'Palestinian Territories'), (b'Panama', b'Panama'), (b'Panama Canal Zone', b'Panama Canal Zone'), (b'Papua New Guinea', b'Papua New Guinea'), (b'Paraguay', b'Paraguay'), (b"People's Democratic Republic of Yemen", b"People's Democratic Republic of Yemen"), (b'Peru', b'Peru'), (b'Philippines', b'Philippines'), (b'Pitcairn Islands', b'Pitcairn Islands'), (b'Poland', b'Poland'), (b'Portugal', b'Portugal'), (b'Puerto Rico', b'Puerto Rico'), (b'Qatar', b'Qatar'), (b'Romania', b'Romania'), (b'Russia', b'Russia'), (b'R\xc3\xa9union', b'R\xc3\xa9union'), (b'Saint Barth\xc3\xa9lemy', b'Saint Barth\xc3\xa9lemy'), (b'Saint Helena', b'Saint Helena'), (b'Saint Kitts and Nevis', b'Saint Kitts and Nevis'), (b'Saint Lucia', b'Saint Lucia'), (b'Saint Martin', b'Saint Martin'), (b'Saint Pierre and Miquelon', b'Saint Pierre and Miquelon'), (b'Saint Vincent and the Grenadines', b'Saint Vincent and the Grenadines'), (b'Samoa', b'Samoa'), (b'San Marino', b'San Marino'), (b'Saudi Arabia', b'Saudi Arabia'), (b'Senegal', b'Senegal'), (b'Serbia', b'Serbia'), (b'Serbia and Montenegro', b'Serbia and Montenegro'), (b'Seychelles', b'Seychelles'), (b'Sierra Leone', b'Sierra Leone'), (b'Singapore', b'Singapore'), (b'Slovakia', b'Slovakia'), (b'Slovenia', b'Slovenia'), (b'Solomon Islands', b'Solomon Islands'), (b'Somalia', b'Somalia'), (b'South Georgia and the South Sandwich Islands', b'South Georgia and the South Sandwich Islands'), (b'South Korea', b'South Korea'), (b'Spain', b'Spain'), (b'Sri Lanka', b'Sri Lanka'), (b'Suriname', b'Suriname'), (b'Svalbard and Jan Mayen', b'Svalbard and Jan Mayen'), (b'Sweden', b'Sweden'), (b'Switzerland', b'Switzerland'), (b'Syria', b'Syria'), (b'S\xc3\xa3o Tom\xc3\xa9 and Pr\xc3\xadncipe', b'S\xc3\xa3o Tom\xc3\xa9 and Pr\xc3\xadncipe'), (b'Taiwan', b'Taiwan'), (b'Tajikistan', b'Tajikistan'), (b'Thailand', b'Thailand'), (b'Timor-Leste', b'Timor-Leste'), (b'Togo', b'Togo'), (b'Tokelau', b'Tokelau'), (b'Tonga', b'Tonga'), (b'Trinidad and Tobago', b'Trinidad and Tobago'), (b'Tunisia', b'Tunisia'), (b'Turkey', b'Turkey'), (b'Turkmenistan', b'Turkmenistan'), (b'Turks and Caicos Islands', b'Turks and Caicos Islands'), (b'Tuvalu', b'Tuvalu'), (b'U.S. Minor Outlying Islands', b'U.S. Minor Outlying Islands'), (b'U.S. Miscellaneous Pacific Islands', b'U.S. Miscellaneous Pacific Islands'), (b'U.S. Virgin Islands', b'U.S. Virgin Islands'), (b'Ukraine', b'Ukraine'), (b'Union of Soviet Socialist Republics', b'Union of Soviet Socialist Republics'), (b'United Arab Emirates', b'United Arab Emirates'), (b'United Kingdom', b'United Kingdom'), (b'United States', b'United States'), (b'Unknown or Invalid Region', b'Unknown or Invalid Region'), (b'Uruguay', b'Uruguay'), (b'Uzbekistan', b'Uzbekistan'), (b'Vanuatu', b'Vanuatu'), (b'Vatican City', b'Vatican City'), (b'Venezuela', b'Venezuela'), (b'Vietnam', b'Vietnam'), (b'Wake Island', b'Wake Island'), (b'Wallis and Futuna', b'Wallis and Futuna'), (b'Western Sahara', b'Western Sahara'), (b'Yemen', b'Yemen'), (b'\xc3\x85land Islands', b'\xc3\x85land Islands')])]),
        ),
        migrations.AddField(
            model_name='user',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='personal_email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(null=True, upload_to=users.models.get_picture_path, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='skype_id',
            field=models.CharField(max_length=32, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='title',
            field=models.CharField(default='Mr', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='yahoo_messenger',
            field=models.CharField(max_length=32, verbose_name=b'Yahoo Messenger', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
