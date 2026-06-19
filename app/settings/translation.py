from modeltranslation.translator import translator, TranslationOptions, register
from .models import (
    Director,
    HistoryClinic,
    AboutClinic,
    AdvicePatient,
    
    PatientTip,
    VideoMaterial,
    RecommendedSpecialist,
    PreparationArticle,
    FAQ,
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