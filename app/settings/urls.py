from rest_framework.routers import DefaultRouter

from app.settings.views import (
    DirectorAPI,
    HistoryClinicAPI,
    AboutClinicAPI,
    AdvicePatientAPI,
    EventAPI,
    PatientTipViewSet,
    VideoMaterialViewSet,
    RecommendedSpecialistViewSet,
    PreparationArticleViewSet,
    FAQViewSet,
)

router = DefaultRouter()
# ------------------- PATIENT TIPS -------------------
router.register("patient-tips", PatientTipViewSet, basename="patient-tips")
router.register("video-materials", VideoMaterialViewSet, basename="video-materials")
router.register("recommended-specialists", RecommendedSpecialistViewSet, basename="recommended-specialists")
router.register("preparation-articles", PreparationArticleViewSet, basename="preparation-articles")
router.register("faqs", FAQViewSet, basename="faqs")
# ------------------- ABOUT PAGE -------------------
router.register("director", DirectorAPI, basename="director")
router.register("history", HistoryClinicAPI, basename="history")
router.register("about-clinic", AboutClinicAPI, basename="about-clinic")
router.register("advice-patient", AdvicePatientAPI, basename="advice-patient")
router.register("event", EventAPI, basename="event")

urlpatterns = router.urls