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