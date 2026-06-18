from rest_framework import mixins, viewsets
from rest_framework.viewsets import GenericViewSet

from app.settings.models import (
    Director,
    HistoryClinic,
    AboutClinic,
    AdvicePatient,
    Event,
    PatientTip,
    VideoMaterial,
    RecommendedSpecialist,
    PreparationArticle,
    FAQ,
)

from app.settings.serializers import (
    DirectorSerializer,
    HistoryClinicSerializer,
    AboutClinicSerializer,
    AdvicePatientSerializer,
    EventSerializer,
    PatientTipSerializer,
    VideoMaterialSerializer,
    RecommendedSpecialistSerializer,
    PreparationArticleSerializer,
    FAQSerializer,
)

# ---------------------- PATIENT TIPS ---------------------
class PatientTipViewSet(viewsets.ModelViewSet):
    queryset = PatientTip.objects.all()
    serializer_class = PatientTipSerializer


class VideoMaterialViewSet(viewsets.ModelViewSet):
    queryset = VideoMaterial.objects.all()
    serializer_class = VideoMaterialSerializer


class RecommendedSpecialistViewSet(viewsets.ModelViewSet):
    queryset = RecommendedSpecialist.objects.all()
    serializer_class = RecommendedSpecialistSerializer


class PreparationArticleViewSet(viewsets.ModelViewSet):
    queryset = PreparationArticle.objects.prefetch_related("images")
    serializer_class = PreparationArticleSerializer


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer



##################### ABOUT PAGE #################################


class DirectorAPI(
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = (
        Director.objects
        .prefetch_related(
            "gallery"
        )
    )
    serializer_class = DirectorSerializer


class HistoryClinicAPI(
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = HistoryClinic.objects.all()
    serializer_class = HistoryClinicSerializer


class AboutClinicAPI(
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = AboutClinic.objects.all()
    serializer_class = AboutClinicSerializer


class AdvicePatientAPI(
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = AdvicePatient.objects.all()
    serializer_class = AdvicePatientSerializer


class EventAPI(
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Event.objects.all()
    serializer_class = EventSerializer