from rest_framework import serializers
from app.settings.models import (
    Director,
    DirectorGallery,
    HistoryClinic,
    AboutClinic,
    AdvicePatient,
    Event,

    PatientTip,
    VideoMaterial,
    RecommendedSpecialist,
    PreparationArticle,
    PreparationArticleImage,
    FAQ,

    BannerHome,
    BannerImage,
    Advantage,
    ServiceShowcase,
    Settings,
    PatientAdvice,
    FreeConcsultation,
    Team,
    Achievement,
    Skills,
    Services
)

##################### HOME PAGE #################################
class BannerImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = ["image"]


class BannerHomeSerializers(serializers.ModelSerializer):
    banners = BannerImageSerializers(
        many=True,
        read_only=True
    )

    class Meta:
        model = BannerHome
        fields = [
            "id",
            "title",
            "description",
            "banners",
        ]

class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = (
            "id",
            "title",
            "description",
            "image",
        )

class ServiceShowcaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceShowcase
        fields = (
            "id",
            "number",
            "title",
            "description",
        )


class SettingsSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Settings

        fields = (
            "id",

            "title_services",
            "description_services",

            "title_center",
            "description_center",

            "title_pacsient",
            "description_pacsient",

            "title_conscintation",
            "description_conscintation",

            "logo",
            "image_footer",
            "video",
            "image1",
            "image2"
        )

class PatientAdviceSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = PatientAdvice

        fields = (
            "id",
            "title",
            "description",
            "image",
        )

class FreeConcsultationSerializers(serializers.ModelSerializer):
    class Meta:
        model = FreeConcsultation
        fields = ["id", "fio", "phone", "is_active"]

##################### TEAM #################################   

class AchievementSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Achievement
        fields = (
            "id",
            "icon",
            "title",
        )


class SkillsSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Skills
        fields = (
            "id",
            "title",
        )


class TeamSerializer(
    serializers.ModelSerializer
):
    achievements = AchievementSerializer(
        many=True,
        read_only=True
    )

    skills = SkillsSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Team

        fields = (
            "id",
            "fio",
            "direction",
            "image",
            "achievements",
            "skills",
        )
    
##################### service #################################

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services

        fields = (
            "id",
            "title",
            "description",
            "image",
            "type"
        )

# ---------------------- ABOUT PAGE ----------------------
class PatientTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientTip
        fields = ("title", "description", "image", "button_text", "button_url")

class VideoMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoMaterial
        fields = ("title", "description", "thumbnail", "video_url")
        
class RecommendedSpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedSpecialist
        fields = ("full_name", "specialty", "photo", "profile_url")


class PreparationArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreparationArticleImage
        fields = ("image", "sort_order")


class PreparationArticleSerializer(serializers.ModelSerializer):
    images = PreparationArticleImageSerializer(many=True, read_only=True)

    class Meta:
        model = PreparationArticle
        fields = ("title", "content", "images")


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ("question", "answer")

# ---------------------- ABOUT PAGE ----------------------
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = (
            "id",
            "fio",
            "position",
            "description",
            "image",
        )

class DirectorGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorGallery
        fields = (
            "id",
            "image"
        )

class HistoryClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryClinic
        fields = (
            "id",
            "year",
            "title",
            "description",
            "image"
        )

class AboutClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutClinic
        fields = (
            "id",
            "title",
            "description"
        )
    
class AdvicePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvicePatient
        fields = (
            "id",
            "title",
            "description"
        )

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "video"
        )