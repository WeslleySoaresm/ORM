from django.db import models

# Create your models here.
class ClinicaUser(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    endereco = models.TextField()
   
    

    def __str__(self):
        return self.username

    class Meta:
        auto_created = False # Indica que a tabela já existe no banco de dados false faz com que o Django não tente criar a tabela novamente
        db_table = 'clinica_user'
        verbose_name = 'Clinica User'
        verbose_name_plural = 'Clinica Users'
