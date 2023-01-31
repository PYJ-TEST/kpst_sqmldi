from rest_framework import serializers
from .models import TblProject, TblDsDatasetList, TblCmnJobType, TblJobDsStatus

# 이후에 read_only, write_only option 체크
class TblProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    creator_id = serializers.CharField()
    ip = serializers.CharField()
    export_path = serializers.CharField()
    export_fps = serializers.IntegerField()
    create_time = serializers.DateTimeField()
    masking_range = serializers.IntegerField()
    exp_format = serializers.IntegerField()
    exp_quality = serializers.IntegerField()
    is_img = serializers.IntegerField()
    json_save = serializers.IntegerField()

    class Meta:
        model = TblProject
        fields = "__all__"


class TblDsDatasetListSerializer(serializers.ModelSerializer):
    fk_project = serializers.StringRelatedField()
    file_name = serializers.CharField()
    masking_table_name = serializers.CharField()
    masked_frame_table_name = serializers.CharField()
    fps = serializers.IntegerField()
    total_frames = serializers.IntegerField()
    auto_detection = serializers.IntegerField()
    manual_de_id = serializers.IntegerField()
    re_id = serializers.IntegerField()
    redo = serializers.IntegerField()
    plate = serializers.IntegerField()
    calc_error = serializers.IntegerField()
    face = serializers.IntegerField()
    width = serializers.IntegerField()
    height = serializers.IntegerField()
    hash = serializers.CharField()
    db_save = serializers.IntegerField()

    # tblprj = TblProjectSerializer(many=True, read_only=True)

    class Meta:
        model = TblDsDatasetList
        fields = ('id', 'fk_project', 'file_name', 'masking_table_name', 'masked_frame_table_name', 'fps', 'total_frames',
                    'auto_detection', 'manual_de_id', 're_id', 'redo', 'plate', 'calc_error', 'face', 'width', 'height'
                    'hash', 'db_save')


class TblCmnJobType(serializers.ModelSerializer):
    id = serializers.IntegerField()
    type = serializers.CharField()

    class Meta:
        model = TblCmnJobType
        fields = "__all__"


class TblDatasetListJoinStatusSerializer(serializers.ModelSerializer):
    state = serializers.IntegerField()
    p_state = serializers.IntegerField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    progress_rate = serializers.FloatField()
    error_rate = serializers.FloatField()
    last_frame_idx = serializers.IntegerField()
    node_id = serializers.IntegerField()
    gpu_id = serializers.IntegerField()
    
    tblprj = TblProjectSerializer(many=True, read_only=True)

    class Meta:
        model = TblJobDsStatus
        fields = ('tblprj', 'state', 'p_state', 'start_time', 'end_time',
                    'progress_rate', 'error_rate', 'last_frame_idx', 'node_id', 'gpu_id')