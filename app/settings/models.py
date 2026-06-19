from django.db import models

# BASE MODEL

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["sort_order", "id"]



# ----------------------- О НАС -----------------------
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

