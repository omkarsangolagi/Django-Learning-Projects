from django.urls import path
from accounts.views import home,register,login_view,admin_dashboard,staff_dashboard,logout_view,manage_staff,add_staff,edit_staff,delete_staff

urlpatterns=[
    path('home/',home,name="home"),
    path('register/',register,name="register"),
    path('login/',login_view,name="login"),
    path('admin_dashboard/',admin_dashboard,name="admin_dashboard"),
    path('staff_dashboard',staff_dashboard,name="staff_dashboard"),
    path('logout/',logout_view,name="logout_view"),
    path('manage_staff/',manage_staff,name="manage_staff"),
    path('add_staff/',add_staff,name="add_staff"),
    path('edit_staff/<int:id>/',edit_staff,name='edit_staff'),
    path('delete_staff/<int:id>/',delete_staff,name='delete_staff'),
]