from django.contrib import admin
from .models import Escola, User, Bloco, Setor, Aviso, Mensagem

admin.site.register(Escola)
admin.site.register(User)
admin.site.register(Bloco)
admin.site.register(Setor)
admin.site.register(Aviso)
admin.site.register(Mensagem)