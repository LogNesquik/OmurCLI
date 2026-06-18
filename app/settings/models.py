from django.db import models
from app.settings.enum import TYPE

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
        verbose_name = "Совет пациенту"
        verbose_name_plural = "Советы пациентам"

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

##################### HOME PAGE #################################

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

##################### TEAM #################################


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

##################### service #################################
