from re import T
from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class FooterInfo(SingletonModel):
    name = models.CharField(verbose_name='Address', max_length=255, )

    class Meta:
        verbose_name = 'Footer Info'
        verbose_name_plural = 'Footer Info'


class ResidentJia(SingletonModel):
    file = models.FileField(upload_to='file', verbose_name='PDF')

    class Meta:
        verbose_name = 'Резиденты Jia'
        verbose_name_plural = 'Резиденты Jia'


class FooterPhoneNumber(models.Model):
    number = models.CharField(max_length=255, verbose_name="Номер")
    footer_info = models.ForeignKey(
        FooterInfo, on_delete=models.CASCADE,
        related_name='phones',
    )

    class Meta:
        verbose_name = 'Footer Info'
        verbose_name_plural = 'Footer Info'


class FooterEmail(models.Model):
    email = models.EmailField(verbose_name='Email')
    footer_info = models.ForeignKey(
        FooterInfo, on_delete=models.CASCADE,
        related_name='emails',
    )

    class Meta:
        verbose_name = 'Footer Info'
        verbose_name_plural = 'Footer Info'


class Report(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    file = models.FileField(upload_to="reports",
                            null=True, verbose_name="Файл")
    date = models.DateField(default=timezone.now, verbose_name="Дата")

    class Meta:
        verbose_name = "Отчет"
        verbose_name_plural = "Отчеты"
        ordering = ('-date',)

    def __str__(self):
        return f'{self.date} -- {self.name}'


class BusinessSupport(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    created = models.DateField(
        default=timezone.now, verbose_name="Дата создания")
    link = models.URLField(
        verbose_name="Ссылка на официальный источник", null=True)
    banner = models.ImageField(
        upload_to="business_support", null=True, verbose_name="Баннер"
    )

    class Meta:
        verbose_name = "Поддержка бизнеса"
        verbose_name_plural = "Поддержка бизнеса"

    def __str__(self):
        return self.title


class MemberShip(models.Model):
    class Category(models.TextChoices):
        A = "A", "A"
        B = "B", "B"
        C = 'C', 'C'

    category = models.CharField(
        max_length=1,
        verbose_name="Категория",
        choices=Category.choices,
        default=Category.A,
    )
    price = models.PositiveIntegerField(
        default=0, verbose_name='Цена за резиденство',
    )
    district_price = models.PositiveIntegerField(
        default=0, verbose_name='Цена за резиденствие в регионах'
    )
    logo = models.ImageField(
        upload_to='logo', verbose_name='Логотип',
    )
    pdf_file = models.FileField(
        upload_to='pdf', verbose_name='PDF'
    )

    def __str__(self):
        return f'{self.category} -- {self.price}'

    class Meta:
        verbose_name = 'Cтать резидентом'
        verbose_name_plural = 'Cтать резидентом'


class MemberShipPrivileges(models.Model):
    membership = models.ForeignKey(
        MemberShip, related_name='priveleges',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=255, verbose_name='Название',
    )

    class Meta:
        verbose_name = 'Привилегии для резидента'
        verbose_name_plural = 'Привилегии для резидента'


class Contact(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Название',
    )
    logo = models.ImageField(
        upload_to='contact', verbose_name='Логотип'
    )
    address = models.CharField(
        max_length=255, verbose_name='Адрес',
    )

    def __str__(self):
        return f'{self.title} -- {self.address}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class ContactPhone(models.Model):
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE,
        related_name='contact_phone'
    )
    phone = models.CharField(
        max_length=255, verbose_name='Телефон',
    )

    def __str__(self):
        return f"{self.contact.title} -- {self.phone}"


class ContactCellular(models.Model):
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE,
        related_name='contact_cellular'
    )
    phone = models.CharField(
        max_length=255, verbose_name='Сотовые',
    )

    def __str__(self):
        return f"{self.contact.title} -- {self.phone}"


class ContactEmail(models.Model):
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE,
        related_name='contact_email'
    )
    email = models.EmailField(
        max_length=255, verbose_name='Email',
    )

    def __str__(self):
        return f"{self.contact.title} -- {self.email}"


class MainPageBanner(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Название',
    )
    description = models.TextField(verbose_name="Описание")
    banner = models.ImageField(
        upload_to="business_support", null=True, verbose_name="Баннер"
    )
    link = models.URLField(
        verbose_name="Ссылка на официальный сайт", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Main Page'
        verbose_name_plural = 'Main Page'


class ActionPlane(models.Model):
    image = models.ImageField(upload_to='action_plane',
                              verbose_name='Изображение')

    class Meta:
        verbose_name = 'План мероприятий'
        verbose_name_plural = 'План мероприятий'
        ordering = ('-id',)


class Advertising(models.Model):
    image = models.ImageField(
        upload_to='advertising', verbose_name='Изображение'
    )
    link = models.URLField(
        verbose_name='Ссылка на официальный рекламу'
    )

    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Рекламы'

    def __str__(self) -> str:
        return self.link


class Situation(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    file = models.FileField(upload_to='documents', verbose_name="Документ")
    image = models.ImageField(
        upload_to='document_images', verbose_name="Изображение")
    description = models.CharField(max_length=255, verbose_name="Комментарий")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Положение'
        verbose_name_plural = 'Положения'


class Organization(models.Model):
    class Category(models.TextChoices):
        club = "CLUB", "Клуб"
        committee = "COMMITTEE", "Комитет"

    category = models.CharField(
        max_length=10,
        verbose_name="Категория",
        choices=Category.choices,
    )
    title = models.CharField(max_length=255, verbose_name="Имя организации")
    description = RichTextField(verbose_name="Информация об организации")
    image = models.ImageField(upload_to='organization/',
                              verbose_name='Картинка организации')
    icon = models.CharField(
        max_length=127, verbose_name="Иконка (https://remixicon.com)")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
