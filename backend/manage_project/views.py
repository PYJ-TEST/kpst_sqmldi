from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TblDsDatasetListSerializer, TblDatasetListJoinStatusSerializer
from .models import TblProject, TblDsDatasetList, TblJobDsStatus

class TblProjectView(generics.ListAPIView):
    model = TblJobDsStatus
    serializer_class = TblDatasetListJoinStatusSerializer
    permission_classes = [AllowAny,]

    def get(self, request, format=None):
        queryset = TblJobDsStatus.objects.raw('select prj.* , stat.*, creator_id as creator from tbl_project as prj \
                                                            left join tbl_job_prj_status as stat on fk_project_id = prj.id;')
        try:
            projects = TblDatasetListJoinStatusSerializer(queryset, many=True).data
            return Response({"message": "success",
                            "projects": projects})
        except:
            return Response({"message": "failed"})
