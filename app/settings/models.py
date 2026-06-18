from django.db import models

# BASE MODEL

class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["sort_order", "id"]



# ----------------------- О НАС -----------------------
class Director(models.Model):
    # Заголовок делает - frontend
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
        verbose_name = "Галерея руководителя"
        verbose_name_plural = "Галерея руководителей"

    def __str__(self):
        return f"Галерея {self.director.fio} - {self.order}"
    

class HistoryClinic(models.Model):
    year = models.CharField(max_length=9, verbose_name="Год")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="history_clinic/", verbose_name="Фото")
    order = models.CharField(max_length=10, default=0, verbose_name="Порядок")

    class Meta:
        ordering = ["order"]
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
    title = models.CharField(max_length=255, verbose_name="Заголовок", blank=True)
    video = models.FileField(upload_to="events/", verbose_name="Видео")

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        
    def __str__(self):
        return f"{self.title}"
    
# ----------------------- Советы для пациентов -----------------------

class PatientTip(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="patient_tips/")
    button_text = models.CharField(max_length=255, blank=True)
    button_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Совет для пациентов'
        verbose_name_plural = 'Советы для пациентов'

class VideoMaterial(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="video_materials/")
    video_url = models.URLField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Видео материал'
        verbose_name_plural = 'Видео материалы'


class RecommendedSpecialist(BaseModel):
    full_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="specialists/")
    profile_url = models.URLField(blank=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Рекомендуемый специалист'
        verbose_name_plural = 'Рекомендуемые специалисты'


class PreparationArticle(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()

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
    image = models.ImageField(upload_to="preparation_articles/")
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Изображение для статьи подготовки'
        verbose_name_plural = 'Изображения для статей подготовки'


class FAQ(BaseModel):
    question = models.CharField(max_length=500)
    answer = models.TextField()

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = 'Часто задаваемый вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'

