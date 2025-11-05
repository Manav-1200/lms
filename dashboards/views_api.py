from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DashboardSummaryAPI(APIView):
    def get(self, request):
        data = {
            "total_users": 0,  # replace with real logic
            "total_courses": 0,
            "total_enrollments": 0,
            "total_sponsors": 0,
            "total_notifications": 0,
        }
        return Response(data, status=status.HTTP_200_OK)
