import datetime
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, Group


class UserManager(BaseUserManager):
    def create_user(self, email, first_name=None, last_name=None, phone=None, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class Address(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.address}, {self.city} {self.postal_code}, {self.country}"

    class Meta:
        # ordering = ('-data_dodania',)
        verbose_name = "Address"
        verbose_name_plural = "Addresses"


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    last_used_address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='user_last_used_address', blank=True, null=True)
    addresses = models.ManyToManyField(Address, through='User_Address')

    is_unregistered = models.BooleanField(
        default=False)  # if client will do an order without log in then django will create placeholder user

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # admin user; non super-user
    admin = models.BooleanField(default=False)  # superuser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    objects = UserManager()


class User_Address(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='user_address_address', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_address_user', blank=True, null=True)


class Unregistered_User(models.Model):
    email = models.EmailField(verbose_name='email', max_length=255)

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='unregistered_User_address', blank=True, null=True)

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Unregistered User"
        verbose_name_plural = "Unregistered Users"

