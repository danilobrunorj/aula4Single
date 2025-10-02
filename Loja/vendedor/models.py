from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    idade = models.IntegerField()
    ativo = models.BooleanField(default=True)

    # Novos campos
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    
    # Campo sexo com opções
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True, null=True)
    
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome
