from django.urls import path
from leave.views import apply_leave
urlpatterns=[
    path('apply_leave/',apply_leave,name='apply_leave')
]