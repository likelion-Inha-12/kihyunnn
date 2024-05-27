from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, userId, email, name, password=None, generation=None, gender=None):

        user = self.model(
            userId=userId,
            email=self.normalize_email(email),
            name=name,
            generation=generation,
            gender=gender
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userId, email, name, password, generation=None, gender=None):
        user = self.create_user(
            userId=userId,
            email=email,
            name=name,
            password=password,
            generation=generation,
            gender=gender
        )

        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=100,
        unique=True,
    )
    userId = models.CharField(max_length=30, unique=True) # 사용자 아이디
    generation = models.IntegerField(null=True) # 사용자 기수
    gender = models.CharField(max_length=10, null=True) # 사용자 성별 (남or여)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'userId'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.userId

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        db_table = 'user' # 테이블명을 user로 설정