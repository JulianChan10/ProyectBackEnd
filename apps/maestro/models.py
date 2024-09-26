from django.db import models

# Create your models here.
class m_maestro(models.Model):
    name= 'app.maestro'
    id_maestro = models.AutoField(primary_key=True, db_column='id_maestro')

    clave = models.CharField(max_length=150, null=True )