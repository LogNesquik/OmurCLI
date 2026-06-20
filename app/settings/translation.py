from modeltranslation.translator import translator, TranslationOptions, register
from .models import (
    Achievement,
    Director,
    HistoryClinic,
    AboutClinic,
    AdvicePatient,
    
    PatientTip,
    VideoMaterial,
    RecommendedSpecialist,
    PreparationArticle,
    FAQ,

    BannerHome, 
    BannerImage, 
    Advantage, 
    Team, 
    Achievement, 
    Skills, 
    ServiceShowcase, 
    Settings, 
    PatientAdvice, 
    Services
)

##################### HOME PAGE #################################

@register(BannerHome)
class BannerHomeTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
    )


@register(BannerImage)
class BannerImageTranslationOptions(TranslationOptions):
    fields = ()


@register(Advantage)
class AdvantageTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
    )

@register(ServiceShowcase)
class ServiceShowcaseTranslation(TranslationOptions):
    fields = (
        "title",
        "description",
    )

@register(Settings)
class SettingsTranslationOptions(
    TranslationOptions
):
    fields = (
        "title_services",
        "description_services",

        "title_center",
        "description_center",

        "title_pacsient",
        "description_pacsient",

        "title_conscintation",
        "description_conscintation",
    )

@register(PatientAdvice)
class PatientAdviceTranslation(
    TranslationOptions
):
    fields = (
        "title",
        "description",
    )

##################### TEAM #################################

@register(Team)
class TeamTranslation(
    TranslationOptions
):
    fields = (
        "fio",
        "direction",
    )


@register(Achievement)
class AchievementTranslation(
    TranslationOptions
):
    fields = (
        "title",
    )


@register(Skills)
class SkillsTranslation(
    TranslationOptions
):
    fields = (
        "title",
    )

##################### service #################################

@register(Services)
class ServicesTranslation(
    TranslationOptions
):
    fields = (
        "title",
        "description",
    )

# ------------------------ patient tips ------------------------


@register(PatientTip)
class PatientTipTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(VideoMaterial)
class VideoMaterialTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(RecommendedSpecialist)
class RecommendedSpecialistTranslationOptions(TranslationOptions):
    fields = ('full_name', 'specialty')

@register(PreparationArticle)
class PreparationArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


# ------------- ------------------ ABOUT PAGE -------------------

class DirectorTranslationOptions(TranslationOptions):
    fields = ('fio', 'position', 'description')


class HistoryClinicTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class AboutClinicTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class AdvicePatientTranslationOptions(TranslationOptions):
    fields = ('title', 'description')



translator.register(Director, DirectorTranslationOptions)
translator.register(HistoryClinic, HistoryClinicTranslationOptions)
translator.register(AboutClinic, AboutClinicTranslationOptions)
translator.register(AdvicePatient, AdvicePatientTranslationOptions)