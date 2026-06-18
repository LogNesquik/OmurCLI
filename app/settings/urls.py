from rest_framework.routers import DefaultRouter
from django.urls import path

from app.settings.views import BannerAPI, AdvantageAPI, ServiceShowcaseAPI, PatientAdviceAPI, FreeConcsultationAPI, TeamAPI, ServicesAPI

router = DefaultRouter()

router.register("banner", BannerAPI, basename="banner")
router.register("advantage", AdvantageAPI, basename="advantage")
router.register("showcase", ServiceShowcaseAPI, basename="showcase")
router.register("patient-advice",PatientAdviceAPI,basename="patient-advice")
router.register("free", FreeConcsultationAPI, basename="free")


##################### HOME PAGE #################################

router.register("team",TeamAPI,basename="team")

##################### TEAM #################################

router.register("service",ServicesAPI,basename="service")


##################### service #################################

urlpatterns = [
    
]

urlpatterns += router.urls