from django.db import models
from django.utils import timezone


class GoverningBody(models.Model):
    fullname = models.CharField(max_length=255, verbose_name="ФИО")
    position = models.CharField(max_length=255, verbose_name="Должность")
    work_place = models.CharField(
        max_length=255, verbose_name='Компания')
    region = models.CharField(
        max_length=255, verbose_name='Регион')
    order = models.PositiveIntegerField(
        null=True, blank=True)

    class Meta:
        verbose_name = 'Правление'
        verbose_name_plural = 'Правление'
        ordering = ('order',)

    def __str__(self):
        return f"{self.fullname} -- {self.position}"


class TeamMember(models.Model):
    class Category(models.TextChoices):
        director = "director", "Директор"
        hr = "hr", "Менеджер"
        empl = 'empl', 'Другие'

    fullname = models.CharField(max_length=255, verbose_name="ФИО")
    position = models.CharField(max_length=255, verbose_name="Должность")
    image = models.ImageField(upload_to='team')
    choice = models.CharField(
        max_length=255,
        choices=Category.choices, verbose_name='Выбор Должности в jia',
        default=Category.empl)
    branch = models.ForeignKey("Branch", verbose_name="Филиал",
                               on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
    facebook = models.URLField(verbose_name='Facebook', blank=True, null=True)
    description = models.TextField(
        verbose_name="Описание", blank=True, null=True, default=' ')

    class Meta:
        verbose_name = "Дирекция"
        verbose_name_plural = "Дирекция"

    def __str__(self):
        return self.fullname


class Branch(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    place = models.PositiveIntegerField(default=0, blank=True, null=True,)
    logo = models.ImageField(
        upload_to='contact', verbose_name='Логотип'
    )

    class Meta:
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"
        ordering = ('place',)

    def __str__(self):
        return self.title


class BranchPhone(models.Model):
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE,
        related_name='phones'
    )
    phone = models.CharField(
        max_length=255, verbose_name='Телефон',
    )

    def __str__(self):
        return f"{self.branch.title} -- {self.phone}"


class BranchCellular(models.Model):
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE,
        related_name='cellulars'
    )
    phone = models.CharField(
        max_length=255, verbose_name='Сотовые',
    )

    def __str__(self):
        return f"{self.branch.title} -- {self.phone}"


class BranchEmail(models.Model):
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE,
        related_name='emails'
    )
    email = models.EmailField(
        max_length=255, verbose_name='Email',
    )

    def __str__(self):
        return f"{self.branch.title} -- {self.email}"


class State(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    logo = models.ImageField(upload_to="logos", verbose_name="Логотип")
    link = models.URLField(
        verbose_name="Ссылка на официальный сайт", null=True)

    class Meta:
        verbose_name = "Совет"
        verbose_name_plural = "Советы"

    def __str__(self):
        return self.title


class Partnership(models.Model):
    company_name = models.CharField(
        max_length=200, verbose_name="Название компании")
    description = models.TextField(verbose_name='Информация о компании')
    image = models.ImageField(upload_to='partners/',
                              verbose_name='Логотип компании')
    memorandum = models.FileField(
        upload_to='memorandums/', verbose_name='Меморандум')
    link = models.URLField(verbose_name='Ссылка на сайт')

    class Meta:
        verbose_name = 'Меморендум'
        verbose_name_plural = 'Меморендумы'

    def __str__(self):
        return self.company_name


class Journal(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='jurnal', verbose_name="Баннер")
    file = models.FileField(upload_to="journals",
                            null=True, verbose_name="Файл")
    date = models.DateField(default=timezone.now, verbose_name="Дата")

    class Meta:
        verbose_name = "Журнал"
        verbose_name_plural = "Журналы"
        ordering = ('-id',)

    def __str__(self):
        return f"{self.date} -- {self.id}"
