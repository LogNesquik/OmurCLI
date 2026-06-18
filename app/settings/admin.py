from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline
from app.settings import translation

from app.settings.models import (
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

admin.site.register(FreeConcsultation)

class BannerImageInline(TranslationTabularInline):
    model = BannerImage
    extra = 1


@admin.register(BannerHome)
class BannerHomeAdmin(TabbedTranslationAdmin):
    list_display = (
        "id",
        "title",
        "description",
    )
    search_fields = (
        "title",
        "description",
    )
    inlines = [BannerImageInline]


@admin.register(BannerImage)
class BannerImageAdmin(TabbedTranslationAdmin):
    list_display = (
        "id",
        "banner",
        "image",
    )
    list_filter = (
        "banner",
    )


@admin.register(Advantage)
class AdvantageAdmin(TabbedTranslationAdmin):
    list_display = (
        "id",
        "title",
    )
    search_fields = (
        "title",
    )

@admin.register(ServiceShowcase)
class ServiceShowcaseAdmin(TabbedTranslationAdmin):
    list_display = (
        "number",
        "title",
    )
    search_fields = (
        "title",
    )

@admin.register(Settings)
class SettingsAdmin(
    TabbedTranslationAdmin
):
    list_display = (
        "id",
        "title_center",
    )


@admin.register(PatientAdvice)
class PatientAdviceAdmin(
    TabbedTranslationAdmin
):
    list_display = (
        "id",
        "title",
        
    )
    search_fields = (
        "title",
    )


##################### HOME PAGE #################################

class AchievementInline(
    TranslationTabularInline
):
    model = Achievement
    extra = 1


class SkillsInline(
    TranslationTabularInline
):
    model = Skills
    extra = 1


@admin.register(Team)
class TeamAdmin(
    TabbedTranslationAdmin
):
    list_display = (
        "id",
        "fio",
        "direction",
    )

    search_fields = (
        "fio",
    )

    inlines = [
        AchievementInline,
        SkillsInline
    ]

##################### TEAM #################################

@admin.register(Services)
class ServicesAdmin(
    TabbedTranslationAdmin
):
    list_display = (
        "id",
        "title",
    )

    search_fields = (
        "title",
    )

##################### service #################################
