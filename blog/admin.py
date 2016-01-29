from django.contrib import admin
from .models import Post,Biographie  #on import le modele Post

# Register your models here.


admin.site.register(Post)
admin.site.register(Biographie)
