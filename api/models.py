from django.db import models
import uuid


class Usuario(models.Model):
    class Meta:
        db_table = 'tb_usuario'
    TIPO_PERFIL = [
        ('recrutador', 'Recrutador'), ('candidato', 'Candidato'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    cpf = models.CharField(
        max_length=11,
        null=False,
        unique=True,
        blank=False)

    tipo = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=TIPO_PERFIL)

    email = models.EmailField(
        null=False,
        blank=False)

    data_nascimento = models.DateField(
        null=False,
        blank=False)

    telefone = models.CharField(
        null=False,
        blank=False,
        max_length=11)


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

    sede = models.ForeignKey('Cidade', db_column='cod_cidade',on_delete=models.CASCADE)


class Curriculo(models.Model):
    class Meta:
        db_table = 'tb_curriculo'
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)

    objetivo = models.CharField(
        max_length=4000,
        null=False,
        blank=False)

    contato = models.CharField(
        max_length=200,
        null=False,
        blank=False)

    dados_pessoais = models.CharField(
        null=False,
        blank=False,
        max_length=4000)

    sobre = models.CharField(
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
        blank=True,)

    data_inscricao = models.DateField(
        null=False,
        blank=False,
        auto_created=True
    )

    apto_entrevista = models.BooleanField(
        null=True,
        blank=True,
    )

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
        ('indeterminado', 'Indeterminado'), ('indeterminado', 'Determinado'), ('obra_certa', 'Obra certa'), ('intermitente', 'Intermitente'),
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


class Cidade(models.Model):
    class Meta:
        ordering = ('nom_cidade',)
        db_table = 'tb_cidade'

    cod_cidade = models.IntegerField(primary_key=True, db_column='cod_cidade')
    cod_estado = models.OneToOneField(Estado, db_column='cod_estado', on_delete=models.CASCADE)
    nom_cidade = models.CharField(max_length=255, db_column='nom_cidade')

    def __unicode__(self):
        return self.nom_cidade
