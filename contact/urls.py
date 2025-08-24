from django.urls import path
from contact import views

app_name='contact'

urlpatterns = [

    # Contacts Urls
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'), 
    path('contact/<int:contact_id>/update/', views.update, name='update'), 
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'), 
    path('contact/create/', views.create, name='create'),

    # Users Urls
    path('user/create/', views.register, name='create'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),

    path('search/', views.search, name='search'),
    path('', views.index, name='index' ),
]
    # path('contact/create/', views.contact, name='contact'),
    # path('contact/<int:contact_id>/update/', views.contact, name='contact'),
    # path('contact/<int:contact_id>/delete/', views.contact, name='contact'),
