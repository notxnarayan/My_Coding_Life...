from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('subadmin', 'Subadmin'),
        ('client', 'Client'),
    )
    email = models.EmailField(unique=True)
    username = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    address = models.TextField(null=True)
    contact_info = models.CharField(max_length=100, null=True)
    registration_number = models.CharField(max_length=50, unique=True, null=True)
    tax_identification_number = models.CharField(max_length=50, null=True)
    website = models.URLField(max_length=200, null=True)
    membership_date = models.DateField(null=True)
    password = models.CharField(max_length=128)
    approval_status = models.CharField(max_length=50, default='Pending')  # Added approval_status

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def _str_(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Simplistic implementation, you can customize this based on your permissions logic
        return True

    def has_module_perms(self, app_label):
        # Simplistic implementation, allows access to all apps
        return True


class category(models.Model):
    categoryname = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/',null=True)

    def __str__(self):
        return self.categoryname

class Product(models.Model):
    productname = models.CharField(max_length=100)
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    qty = models.CharField(max_length=5)
    description= models.TextField(max_length=15,unique=True,null=True)
    available= models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.productname