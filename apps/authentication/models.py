import datetime
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, Group


class UserManager(BaseUserManager):
    def create_user(self, email, first_name=None, last_name=None, birthday=None, phone=None, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
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


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    # profile_picture = models.ImageField(default='profile_pics/default_pic.png', upload_to='profile_pics')
    # todo add rename function to uploaded pictures
    phone = models.CharField(max_length=20, blank=True, null=True)

    is_unregistered = models.BooleanField(
        default=False)  # if client will do an order without log in then django will create placeholder user

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # admin user; non super-user
    admin = models.BooleanField(default=False)  # superuser

    # Group.add_to_class('description', models.CharField(max_length=180, null=True, blank=True))

    # groups = models.ManyToManyField(
    #     Group,
    #     verbose_name='groups',
    #     blank=True,
    #     help_text=(
    #         'The groups this user belongs to. A user will get all permissions '
    #         'granted to each of their groups.'
    #     ),
    # )

    # fieldsets = (
    #     ('Permissions', {'fields': ('admin', 'staff', 'groups',)}),
    #     ('Group Permissions', {
    #         'fields': ('groups', 'user_permissions',)
    #     }),
    # )

    # notice the absence of a "Password field", that is built in.

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
        # ordering = ('-data_dodania',)
        verbose_name = "User"
        verbose_name_plural = "Users"

    objects = UserManager()
