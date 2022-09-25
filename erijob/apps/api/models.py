import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth=None, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth=None, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    """User model."""

    class Meta:
        db_table = 'tb_usuario'

    TIPO_PERFIL = [
        ('recrutador', 'Recrutador'), ('candidato', 'Candidato'),
    ]
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    username = None
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    email = models.EmailField(max_length=30, null=False, unique=True, blank=False)
    cpf = models.CharField(
        max_length=11,
        null=True,
        unique=True,
        blank=True)

    nome = models.CharField(
        max_length=100,
        null=True,
        blank=True)

    tipo = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        choices=TIPO_PERFIL)
    date_of_birth = models.DateField(
        null=True,
        blank=True)

    telefone = models.CharField(
        null=False,
        blank=False,
        max_length=11)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

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
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Empresa(models.Model):
    class Meta:
        db_table = 'tb_empresa'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False)

    cnpj = models.CharField(
        max_length=14,
        null=False,
        unique=True,
        blank=False)

    ramo = models.CharField(
        max_length=14,
        null=False,
        blank=False)

    sede = models.ForeignKey('Cidade', db_column='cod_cidade', on_delete=models.CASCADE)


class Curriculo(models.Model):
    class Meta:
        db_table = 'tb_curriculo'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    objetivo = models.TextField(
        max_length=4000,
        null=False,
        blank=False)

    contato = models.TextField(
        max_length=200,
        null=False,
        blank=False)

    dados_pessoais = models.TextField(
        null=False,
        blank=False,
        max_length=4000)

    sobre = models.TextField(
        null=False,
        blank=False,
        max_length=4000)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class InstituicaoEnsino(models.Model):
    class Meta:
        ordering = ('nome',)
        db_table = 'tb_instituicao'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False)

    sede = models.ForeignKey('Cidade', db_column='cod_cidade', on_delete=models.CASCADE)


class Formacao(models.Model):
    class Meta:
        ordering = ('inicio',)
        db_table = 'tb_formacao'

    TIPO_FORMACAO = [
        ('médio', 'Médio'), ('superior', 'Superior'), ('especialização', 'Especialização'), ('mestrado', 'Mestrado'),
        ('doutorado', 'doutorado'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    area = models.CharField(
        max_length=4000,
        null=False,
        blank=False)

    nivel = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=TIPO_FORMACAO)

    inicio = models.DateField(
        null=False,
        blank=False)

    previsao_termino = models.DateField(
        null=True,
        blank=True)

    em_andamento = models.BooleanField(
        null=True,
        blank=True,
    )

    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE)


class StatusEntrevista(models.Model):
    class Meta:
        ordering = ('valor',)
        db_table = 'tb_status_entrevista'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)
    valor = models.CharField(
        max_length=255,
        null=False,
        blank=False)


class StatusInscricao(models.Model):
    class Meta:
        ordering = ('valor',)
        db_table = 'tb_status_inscricao'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)
    valor = models.CharField(
        max_length=255,
        null=False,
        blank=False)


class Experiencia(models.Model):
    class Meta:
        ordering = ('inicio',)
        db_table = 'tb_experiencia'

    TIPO_FORMACAO = [
        ('médio', 'Médio'), ('superior', 'Superior'), ('especialização', 'Especialização'), ('mestrado', 'Mestrado'),
        ('doutorado', 'doutorado'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    area = models.CharField(
        max_length=4000,
        null=False,
        blank=False)

    cargo = models.CharField(
        max_length=4000,
        null=False,
        blank=False)

    local = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=TIPO_FORMACAO)

    inicio = models.DateField(
        null=False,
        blank=False)

    fim = models.DateField(
        null=True,
        blank=True)

    atual = models.BooleanField(
        null=False,
        blank=False,
    )

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE)


class Vaga(models.Model):
    class Meta:
        ordering = ('data_cadastro',)
        db_table = 'tb_vaga'

    TIPO_CONTRATO = [
        ('indeterminado', 'Indeterminado'), ('indeterminado', 'Determinado'), ('obra_certa', 'Obra certa'),
        ('intermitente', 'Intermitente'),
    ]
    TIPO_REGIME = [
        ('clt', 'CLT'), ('pj', 'PJ')
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    area = models.CharField(
        max_length=255,
        null=False,
        blank=False)

    cargo = models.CharField(
        max_length=255,
        null=False,
        blank=False)

    resposabilidades = models.TextField(
        max_length=4000,
        null=True,
        blank=True)

    requisitos = models.TextField(
        max_length=4000,
        null=True,
        blank=True)

    pcsc = models.TextField(
        max_length=4000,
        null=True,
        blank=True)

    remoto = models.BooleanField(
        null=False,
        blank=False,
    )

    local = models.CharField(
        max_length=255,
        null=False,
        blank=False)

    departamento = models.CharField(
        max_length=255,
        null=False,
        blank=False)

    faixa_salarial = models.CharField(
        max_length=255,
        null=False,
        blank=False)

    local = models.CharField(
        max_length=255,
        null=False,
        blank=False)

    cargo_horaria = models.CharField(
        max_length=255,
        null=False,
        blank=False)

    data_cadastro = models.DateField(
        null=False,
        blank=False,
        auto_now=True
    )

    data_fechamento = models.DateField(
        null=True,
        blank=True)

    tipo_contrato = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=TIPO_CONTRATO)

    contratacao = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=TIPO_REGIME)

    fim = models.DateField(
        null=False,
        blank=False)

    atual = models.BooleanField(
        null=False,
        blank=False,
    )

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)


class Inscricao(models.Model):
    class Meta:
        ordering = ('data_inscricao',)
        db_table = 'tb_inscricao'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    feedback = models.CharField(
        max_length=4000,
        null=True,
        blank=True, )

    data_inscricao = models.DateField(
        null=False,
        blank=False,
        auto_created=True
    )

    apto_entrevista = models.BooleanField(
        null=True,
        blank=True,
    )
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusInscricao, on_delete=models.CASCADE)


class Entrevista(models.Model):
    class Meta:
        ordering = ('data',)
        db_table = 'tb_entrevista'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    feedback = models.CharField(
        max_length=4000,
        null=True,
        blank=True, )

    data = models.DateField(
        null=False,
        blank=False,
        auto_created=True
    )
    status = models.ForeignKey(StatusEntrevista, on_delete=models.CASCADE)
    inscricao = models.ForeignKey(Inscricao, db_column='id_inscricao', on_delete=models.CASCADE)


class Pais(models.Model):
    class Meta:
        ordering = ('nom_pais',)
        db_table = 'tb_pais'

    cod_pais = models.IntegerField(primary_key=True, db_column='cod_pais')
    sgl_pais = models.CharField(max_length=2, db_column='sgl_pais')
    nom_pais = models.CharField(max_length=255, db_column='nom_pais')


class Estado(models.Model):
    class Meta:
        ordering = ('nom_estado',)
        db_table = 'tb_estado'

    cod_estado = models.IntegerField(primary_key=True, db_column='cod_estado')
    cod_pais = models.OneToOneField(Pais, db_column='cod_pais', on_delete=models.CASCADE)
    nom_estado = models.CharField(max_length=255, db_column='nom_estado')
    sgl_estado = models.CharField(max_length=2, db_column='sgl_estado')

    def __unicode__(self):
        return self.nom_estado

    def __str__(self):
        return self.nom_estado


class Cidade(models.Model):
    class Meta:
        ordering = ('nom_cidade',)
        db_table = 'tb_cidade'

    cod_cidade = models.IntegerField(primary_key=True, db_column='cod_cidade')
    cod_estado = models.OneToOneField(Estado, db_column='cod_estado', on_delete=models.CASCADE)
    nom_cidade = models.CharField(max_length=255, db_column='nom_cidade')

    def __unicode__(self):
        return self.nom_cidade

    def __str__(self):
        return self.nom_cidade
