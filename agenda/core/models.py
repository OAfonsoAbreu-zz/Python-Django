from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Criar arquivo de migração antes de enviar para BD (pasta migrations):
# --> python manage.py makemigrations core
#Criar comando SQL antes de enviar para BD:
# --> python manage.py sqlmigrate core 0001
#Migrar models para o BD (de um módulo especifico e uma model especifica):
# --> python manage.py migrate core 0001

#Python cria a primary key automaticamente
#Se não for especificado um nome pra tabela, o Python cria o nome padrão 'modulo_model'

#Para importar no Admin, ir para arquivo admin.py

class Evento(models.Model):
    titulo = models.CharField(max_length=100) #string com no maximo 100 caracteres
    descricao = models.TextField(blank=True, null=True) #campo de texto que pode ser vazio ou nulo
    data_evento = models.DateTimeField(verbose_name= 'Data do Evento') #Campo de data que não pode ser nulo.
                                        #verbose_name --> nome personalizado para o portal Admin
    data_criacao = models.DateTimeField(auto_now=True) #Campo de data com datatime atual como default
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #Criar foreignkey e ativar Delete on Cascade

    class Meta: #Forçar metadados da tabela
        db_table = 'evento' #Mudar nome da tabela para 'evento'

    def __str__(self): #Nome que irá aparecer para cada registro na tabela no Admin
        return self.titulo