from django.urls import path
from apps.registro_hora_extra.views import (
    HoraExtraList,
    HoraExtraEdit,
    HoraExtraDelete,
    HoraExtraNew
)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo/', HoraExtraNew.as_view(), name='create_hora_extra'),
    path('editar/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),

]
