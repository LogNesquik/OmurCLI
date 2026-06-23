from django.db import models
from app.settings.enum import TYPE

# BASE MODEL

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["sort_order", "id"]


##################### HOME PAGE #################################
class Settings(models.Model):
    title_services = models.CharField(
        max_length=155,
        verbose_name="Заголовок Услуги"
    )
    description_services = models.TextField(
        verbose_name="Описание Услуги"
    )
    title_center = models.CharField(
        max_length=155,
        verbose_name="Заголовок Центра Омур"
    )
    description_center = models.TextField(
        verbose_name="Описание Центра Омур"
    )
    title_pacsient = models.CharField(
        max_length=155,
        verbose_name="Заголовка Пациентов"
    )
    description_pacsient = models.TextField(
        verbose_name="Описание Пациентов"
    )
    title_conscintation = models.CharField(
        max_length=155,
        verbose_name="Заголовка Консультаций"
    )
    description_conscintation = models.TextField(
        verbose_name="Описание Консультаций"
    )
    logo = models.ImageField(
        upload_to="logo",
        verbose_name="Логотип"
    )
    image_footer = models.ImageField(
        upload_to="logo",
        verbose_name="Фото"
    )
    video = models.URLField(
        verbose_name="Ссылка на Видео"
    )
    image1 = models.ImageField(
        upload_to="settings",
        verbose_name="Фото" 
    )
    image2 = models.ImageField(
        upload_to="settings",
        verbose_name="Фото 2" 
    )

    def __str__(self):
        return self.title_center

    class Meta:
        verbose_name = "Настройки Главной Страницы"
        verbose_name_plural = "Настройки Главной Страницы"

class BannerHome(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройки баннера"
        verbose_name_plural = "Настройки баннера"

class BannerImage(models.Model):
    banner = models.ForeignKey(
        BannerHome, 
        on_delete=models.CASCADE,
        related_name="banners",
        verbose_name="Баннер"
    )
    image = models.ImageField(
        upload_to="banners",
        verbose_name="Фото"
    )

    class Meta:
        verbose_name = "Изображение Баннера"
        verbose_name_plural = "Изображение Баннера"

class Advantage(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="advantages/",
        verbose_name="Иконка"
    )

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"

    def __str__(self):
        return self.title

class ServiceShowcase(models.Model):
    number = models.PositiveIntegerField(
        verbose_name="Номер"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Описание"
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="Активная карточка"
    )

    class Meta:
        verbose_name = "Карточка услуг"
        verbose_name_plural = "Карточки услуг"

    def __str__(self):
        return self.title

class PatientAdvice(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="patient_advice/",
        verbose_name="Фото"
    )

    class Meta:
        verbose_name = "Совет нашиму пациенту"
        verbose_name_plural = "Советы нашим пациентам"

    def __str__(self):
        return self.title

class FreeConcsultation(models.Model):
    fio = models.CharField(
        max_length=155,
        verbose_name="ФИО"
    )
    phone = models.CharField(
        max_length=155,
        verbose_name="Номер Телефона"
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="Актив",
        blank=True, null=True
    )

    class Meta:
        verbose_name = "Бесплатная консультация"
        verbose_name_plural = "Бесплатные консультации"
    
    def __str__(self):
        return self.fio

##################### TEAM #################################
class Team(models.Model):
    fio = models.CharField(
        max_length=155,
        verbose_name="ФИО"
    )
    direction = models.CharField(
        max_length=155,
        verbose_name="Направление"
    )
    image = models.ImageField(
        upload_to="team",
        verbose_name="Аватар"
    )

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "Работники"
        verbose_name_plural = "Работники"

class Achievement(models.Model):
    icon = models.ImageField(
        upload_to="icon",
        verbose_name="Иконка"
    )
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="achievements"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижение"

class Skills(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="skills"
    )
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Навыки"
        verbose_name_plural = "Навыки"

##################### service #################################
class Services(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="services",
        verbose_name="Фото"
    )
    type = models.CharField(
        max_length=155,
        verbose_name="Тип услуги",
        choices=TYPE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Наши Услуги"
        verbose_name_plural = "Наши Услуги"

# ----------------------- About Us -----------------------
class Director(models.Model):
    fio = models.CharField(max_length=255, verbose_name="ФИО директора")
    position = models.CharField(max_length=255, verbose_name="Должность директора")
    image = models.ImageField(upload_to="director/", verbose_name="Фото директора")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Руководитель"
        verbose_name_plural = "Руководители"

    def __str__(self):
        return self.fio


class DirectorGallery(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="director/gallery/", verbose_name="Фото")
    order = models.CharField(max_length=10, default=0, verbose_name="Порядок")

    class Meta:
        ordering = ["order"]
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f"Галерея {self.director.fio} - {self.order}"
    

class HistoryClinic(models.Model):
    year = models.CharField(max_length=9, verbose_name="Год")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="history_clinic/", verbose_name="Фото")

    class Meta:
        verbose_name = "История клиники"
        verbose_name_plural = "История клиники"

    def __str__(self):
        return f"{self.title}"
    
class AboutClinic(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "О клинике"
        verbose_name_plural = "О клинике"

    def __str__(self):
        return f"{self.title}"

class AdvicePatient(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="advice_patient/", verbose_name="Фото")

    class Meta:
        verbose_name = "Совет пациенту"
        verbose_name_plural = "Советы пациенту"

    def __str__(self):
        return f"{self.title}"
    

class Event(models.Model):
    image = models.ImageField(upload_to="events/", verbose_name="Превью видео", blank=True, null=True)
    video = models.URLField(verbose_name="Видео", blank=True, null=True)

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        
    def __str__(self):
        return f"{self.title}"
    
# ----------------------- Советы для пациентов -----------------------

class PatientTip(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="patient_tips/", verbose_name="Фото")

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Совет для пациентов'
        verbose_name_plural = 'Советы для пациентов'

class VideoMaterial(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    thumbnail = models.ImageField(upload_to="video_materials/", verbose_name="Баннер видео")
    video_url = models.URLField(verbose_name="URL видео")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Видео материал'
        verbose_name_plural = 'Видео материалы'


class RecommendedSpecialist(BaseModel):
    full_name = models.CharField(max_length=255, verbose_name="ФИО специалиста")
    specialty = models.CharField(max_length=255, verbose_name="Специализация")
    photo = models.ImageField(upload_to="specialists/", verbose_name="Фото специалиста")

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Рекомендуемый специалист'
        verbose_name_plural = 'Рекомендуемые специалисты'


class PreparationArticle(BaseModel):
    content = models.TextField(verbose_name="Содержание статьи(первый абзац)")
    title = models.CharField(max_length=255, verbose_name="Заголовок статьи")
    description = models.TextField(blank=True, null=True, verbose_name="Описание статьи")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статья для подготовки'
        verbose_name_plural = 'Статьи для подготовки'


class PreparationArticleImage(models.Model):
    article = models.ForeignKey(
        PreparationArticle,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="preparation_articles/", verbose_name="Изображение")
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Изображение для статьи подготовки'
        verbose_name_plural = 'Изображения для статей подготовки'


class FAQ(BaseModel):
    order = models.CharField(max_length=4, default=0, verbose_name="Порядок вопросов")
    question = models.CharField(max_length=500, verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")
    image = models.ImageField(upload_to="faq/", blank=True, null=True, verbose_name="Фото")

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ["order"]
        verbose_name = 'Часто задаваемый вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'

