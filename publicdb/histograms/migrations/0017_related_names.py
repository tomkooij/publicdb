# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-20 00:57
from __future__ import unicode_literals

import django.db.models.deletion

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('histograms', '0016_meta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configurations', to='histograms.Summary'),
        ),
        migrations.AlterField(
            model_name='dailydataset',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datasets', to='histograms.Summary'),
        ),
        migrations.AlterField(
            model_name='dailydataset',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datasets', to='histograms.DatasetType'),
        ),
        migrations.AlterField(
            model_name='dailyhistogram',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histograms', to='histograms.Summary'),
        ),
        migrations.AlterField(
            model_name='dailyhistogram',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histograms', to='histograms.HistogramType'),
        ),
        migrations.AlterField(
            model_name='detectortimingoffset',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detector_timing_offsets', to='histograms.Summary'),
        ),
        migrations.AlterField(
            model_name='multidailydataset',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multi_datasets', to='histograms.Summary'),
        ),
        migrations.AlterField(
            model_name='multidailydataset',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multi_datasets', to='histograms.DatasetType'),
        ),
        migrations.AlterField(
            model_name='multidailyhistogram',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multi_histograms', to='histograms.Summary'),
        ),
        migrations.AlterField(
            model_name='multidailyhistogram',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multi_histograms', to='histograms.HistogramType'),
        ),
        migrations.AlterField(
            model_name='networkhistogram',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='network_histograms', to='histograms.NetworkSummary'),
        ),
        migrations.AlterField(
            model_name='networkhistogram',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='network_histograms', to='histograms.HistogramType'),
        ),
        migrations.AlterField(
            model_name='pulseheightfit',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pulseheight_fits', to='histograms.Summary'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='summaries', to='inforecords.Station'),
        ),
    ]