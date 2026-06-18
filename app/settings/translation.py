from modeltranslation.translator import register, TranslationOptions
from app.settings.models import BannerHome, BannerImage, Advantage, Team, Achievement, Skills, ServiceShowcase, Settings, PatientAdvice, Services


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


##################### HOME PAGE #################################

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

##################### TEAM #################################


@register(Services)
class ServicesTranslation(
    TranslationOptions
):
    fields = (
        "title",
        "description",
    )

##################### service #################################
