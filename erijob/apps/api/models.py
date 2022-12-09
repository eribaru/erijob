import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from select import select


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


STATE_CHOICES = (
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
    ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
    ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
)


class Cidade(models.Model):
    class Meta:
        ordering = ('nom_cidade',)
        db_table = 'tb_cidade'

    cod_cidade = models.IntegerField(primary_key=True, db_column='cod_cidade')
    cod_estado = models.CharField(max_length=2, choices=STATE_CHOICES)
    nom_cidade = models.CharField(max_length=255, db_column='nom_cidade')

    def __unicode__(self):
        return self.nom_cidade

    def __str__(self):
        return self.nom_cidade


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

    sede = models.ForeignKey(Cidade, db_column='cod_cidade', on_delete=models.CASCADE, blank=True, null=True,
                             parent_link=True)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    class Meta:
        db_table = 'tb_endereco'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    apelido = models.CharField(
        max_length=255,
        null=True,
        unique=False,
        blank=True)

    rua = models.CharField(
        max_length=255,
        null=False,
        blank=False)

    complemento = models.CharField(
        max_length=255,
        null=True,
        blank=True)

    numero = models.CharField(
        max_length=25,
        null=False,
        blank=False)

    bairro = models.CharField(
        max_length=255,
        null=False,
        unique=False,
        blank=False)

    cidade = models.ForeignKey(Cidade, db_column='cod_cidade', on_delete=models.CASCADE, blank=True, null=True,
                               parent_link=True)

    cep = models.CharField(
        max_length=8,
        null=False,
        blank=False)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True,
                                blank=True)

    tipo = models.CharField(
        max_length=25,
        null=False,
        unique=False,
        blank=False)

    principal = models.BooleanField(
        null=False,
        unique=False,
        blank=False)

    def __unicode__(self):
        return self.apelido

    def __str__(self):
        return self.apelido

    def get_cidade(self):
        cidade: Cidade
        return cidade

    def resumo(self):
        resumo = self.rua + " " + self.numero
        if self.complemento is not None:
            resumo = resumo + ", " + self.complemento
        cep_formatado = '{}-{}'.format(self.cep[0:5], self.cep[5:7])
        # cidade = Cidade.objects.get()
        resumo = resumo + " " + self.bairro + "\ncep " + cep_formatado
        if self.cidade is not None:
            resumo = resumo + " " + self.cidade.nom_cidade + "/" + self.cidade.cod_estado
        return resumo


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

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome


class Formacao(models.Model):
    class Meta:
        ordering = ('inicio',)
        db_table = 'tb_formacao'

    TIPO_FORMACAO = [
        ('medio', 'Médio'), ('superior', 'Superior'), ('especializacao', 'Especialização'), ('mestrado', 'Mestrado'),
        ('doutorado', 'Doutorado'),
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

    def __unicode__(self):
        return self.valor

    def __str__(self):
        return self.valor


class Experiencia(models.Model):
    class Meta:
        ordering = ('inicio',)
        db_table = 'tb_experiencia'

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

    def __str__(self):
        return self.cargo


class Vaga(models.Model):
    class Meta:
        ordering = ('data_cadastro',)
        db_table = 'tb_vaga'

    TIPO_CONTRATO = [
        ('indeterminado', 'Indeterminado'), ('determinado', 'Determinado'), ('obra_certa', 'Obra certa'),
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

    local = models.TextField(
        max_length=255,
        null=True,
        blank=True)
    faixa_salarial = models.CharField(
        max_length=255,
        null=False,
        blank=False)

    carga_horaria = models.CharField(
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

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.cargo


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
        null=True,
        blank=True,
        auto_created=True,
        auto_now_add=True
    )

    apto_entrevista = models.BooleanField(
        null=True,
        blank=True,
    )
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusInscricao, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario + '/' + self.vaga

    def status_nome(self):
        return self.status.valor

    def vaga_nome(self):
        return self.vaga.cargo

    def usuario_nome(self):
        return self.usuario.nome

    def esta_apto(self):
        return self.usuario.nome


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
