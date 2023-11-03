from tortoise.models import Model
from tortoise.fields import IntField, CharField, BooleanField, DatetimeField
from tortoise.exceptions import ValidationError, DoesNotExist


class HabilidadesCandidato(Model):

    id = IntField(pk=True)
    candidatoId = IntField()
    habilidadesId = IntField()
    
    async def save(self, *args, **kwargs):
        await super().save(*args, **kwargs)
    


