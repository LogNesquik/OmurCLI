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

    BannerHome,
    BannerImage,
    Advantage,
    ServiceShowcase,
    Settings,
    PatientAdvice,
    FreeConcsultation,
    Team,
    Services
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
    BannerHomeSerializers, 
    AdvantageSerializer, 
    ServiceShowcaseSerializer, 
    SettingsSerializer, 
    PatientAdviceSerializer, 
    FreeConcsultationSerializers, 
    TeamSerializer,
    ServicesSerializer

)

# ---------------------- HOME PAGE ---------------------
class BannerAPI(mixins.ListModelMixin, GenericViewSet):
    queryset = BannerHome.objects.all()
    serializer_class = BannerHomeSerializers


class AdvantageAPI(mixins.ListModelMixin, GenericViewSet):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSerializer

class ServiceShowcaseAPI(
    mixins.ListModelMixin, GenericViewSet
):
    queryset = ServiceShowcase.objects.all()
    serializer_class = ServiceShowcaseSerializer


class SettingsAPI(
    mixins.ListModelMixin, GenericViewSet
):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer

class PatientAdviceAPI(
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = PatientAdvice.objects.all()
    serializer_class = PatientAdviceSerializer

class FreeConcsultationAPI(mixins.CreateModelMixin, GenericViewSet):
    queryset = FreeConcsultation.objects.all()
    serializer_class = FreeConcsultationSerializers

# ---------------------- TEAM ---------------------
class TeamAPI(mixins.ListModelMixin, GenericViewSet):
    queryset = (
        Team.objects
        .prefetch_related(
            "achievements",
            "skills"
        )
    )
    serializer_class =  TeamSerializer

# ---------------------- SERVICES ---------------------
class ServicesAPI(
    mixins.ListModelMixin,
    GenericViewSet
):
    serializer_class = ServicesSerializer

    def get_queryset(self):
        queryset = Services.objects.all()

        service_type = self.request.query_params.get("type")

        if service_type:
            queryset = queryset.filter(type__iexact=service_type)

        return queryset
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