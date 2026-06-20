from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline
from django.contrib.admin import TabularInline

from app.settings import translation 

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


admin.site.register(FreeConcsultation)

class BannerImageInline(TranslationTabularInline):
    model = BannerImage
    extra = 1
    

class DirectorGalleryInline(TabularInline):
    model = DirectorGallery
    extra = 1

class PreparationArticleImageInline(admin.TabularInline):
    model = PreparationArticleImage
    extra = 1



# ------------------- ABOUT PAGE -------------------
@admin.register(Director)
class DirectorAdmin(TabbedTranslationAdmin):
    list_display = (
        "fio",
        "position",
        "description",
        "image",
    )
    search_fields = (
        "fio",
        "position",
    )
    inlines = [
        DirectorGalleryInline,
    ]

@admin.register(HistoryClinic)
class HistoryClinicAdmin(TabbedTranslationAdmin):
    list_display = (
        "year",
        "title",
        "description",
        "image",
    )
    search_fields = (
        "year",
        "title",
    )

@admin.register(AboutClinic)
class AboutClinicAdmin(TabbedTranslationAdmin):
    list_display = (
        "title",
        "description",
    )
    search_fields = (
        "title",
    )

@admin.register(AdvicePatient)
class AdvicePatientAdmin(TabbedTranslationAdmin):
    list_display = (
        "title",
        "description",
        "image"
    )
    search_fields = (
        "title",
    )

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "image",
        "video"
    )
    search_fields = (
        "video",
    )

# ------------------- PATIENT PAGE -------------------
@admin.register(PatientTip)
class PatientTipAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'description', 'image')
    search_fields = ('title',)

@admin.register(VideoMaterial)
class VideoMaterialAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'description', 'thumbnail', 'video_url')
    search_fields = ('title',)

@admin.register(RecommendedSpecialist)
class RecommendedSpecialistAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'full_name', 'specialty', 'photo')
    search_fields = ('full_name',)

@admin.register(PreparationArticle)
class PreparationArticleAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'title', 'content')
    search_fields = ('title',)
    inlines = [PreparationArticleImageInline]

@admin.register(FAQ)
class FAQAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'question', 'answer', 'image', 'order')
    search_fields = ('question',)


##################### HOME PAGE #################################
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


##################### TEAM #################################

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

##################### service #################################
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
