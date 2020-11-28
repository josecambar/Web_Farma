from django.db import models

# Create your models here.


class medicina(models.Model):
   
    TIPO_M = [
        ('G', 'Generico'),
        ('C', 'Comercial'),
    ]

    
    codigo = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha_fabricacion = models.DateField()
    fecha_vencimiento = models.DateField()
    tipo_medicamento = models.CharField(max_length=12, choices=TIPO_M)

    #persona = models.ForeignKey(persona, null = True, blank= True, on_delete = models.CASCADE)
    #antecedentes_medico = models.ManyToManyField(antecedentes_medico)

    def __str__(self) -> str:
        return self.nombre + '  ' + self.TIPO_M + ' - ' + str(self.codigo)
