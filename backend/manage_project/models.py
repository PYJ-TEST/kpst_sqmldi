from django.db import models

class TblProject(models.Model):
    name = models.CharField(max_length=100)
    creator_id = models.CharField(max_length=50)
    ip = models.CharField(max_length=50, blank=True, null=True)
    export_path = models.TextField()
    export_fps = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    masking_range = models.IntegerField(blank=True, null=True)
    exp_format = models.IntegerField(blank=True, null=True)
    exp_quality = models.IntegerField(blank=True, null=True)
    is_img = models.IntegerField(blank=True, null=True)
    json_save = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_project'


class TblDsDatasetList(models.Model):
    fk_project = models.ForeignKey(TblProject, models.DO_NOTHING, related_name='tblprj')
    file_name = models.CharField(max_length=100, blank=True, null=True)
    masking_table_name = models.CharField(max_length=100, blank=True, null=True)
    masked_frame_table_name = models.CharField(max_length=100, blank=True, null=True)
    fps = models.IntegerField(blank=True, null=True)
    total_frames = models.IntegerField(blank=True, null=True)
    auto_detection = models.IntegerField(blank=True, null=True)
    manual_de_id = models.IntegerField(blank=True, null=True)
    re_id = models.IntegerField(blank=True, null=True)
    redo = models.IntegerField(blank=True, null=True)
    plate = models.IntegerField(blank=True, null=True)
    calc_error = models.IntegerField(blank=True, null=True)
    face = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    hash = models.CharField(max_length=300, blank=True, null=True)
    db_save = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ds_dataset_list'


class TblCmnJobType(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tbl_cmn_job_type'


class TblJobDsStatus(models.Model):
    fk_dataset =  models.ForeignKey(TblDsDatasetList, on_delete=models.CASCADE, related_name='with_status_prj')
    job_type = models.ForeignKey(TblCmnJobType, models.DO_NOTHING, db_column='job_type', blank=True, null=True, related_name='tbl_jop_type')
    state = models.IntegerField(blank=True, null=True)
    p_state = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    progress_rate = models.FloatField(blank=True, null=True)
    error_rate = models.FloatField(blank=True, null=True)
    last_frame_idx = models.IntegerField(blank=True, null=True)
    node_id = models.IntegerField(blank=True, null=True)
    gpu_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_job_ds_status'

