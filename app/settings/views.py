from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from app.settings.models import PatientAdvice, BannerHome, Advantage, ServiceShowcase, Settings, FreeConcsultation, Team, Services
from app.settings.serializers import BannerHomeSerializers, AdvantageSerializer, ServiceShowcaseSerializer, SettingsSerializer, PatientAdviceSerializer, FreeConcsultationSerializers, TeamSerializer,\
ServicesSerializer

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


##################### HOME PAGE #################################


class TeamAPI(mixins.ListModelMixin, GenericViewSet):
    queryset = (
        Team.objects
        .prefetch_related(
            "achievements",
            "skills"
        )
    )
    serializer_class =  TeamSerializer

##################### TEAM #################################

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

##################### service #################################
