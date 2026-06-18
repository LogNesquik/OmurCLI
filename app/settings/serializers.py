from rest_framework import serializers
from app.settings.models import BannerHome, BannerImage, Advantage, ServiceShowcase, Settings, PatientAdvice, FreeConcsultation, Team, Achievement, Skills, Services


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


##################### HOME PAGE #################################

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

##################### TEAM #################################

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

##################### service #################################
