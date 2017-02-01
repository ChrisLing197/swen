from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'system'
urlpatterns = [
        url(r'^accounts/new/$', views.UserCreate.as_view(), name='register'),
        url(r'^accounts/edit/$', views.register, name='user_edit'),
        url(r'^accounts/', include('django.contrib.auth.urls')),

        url(r'^dashboard/$', views.dashboard, name='dashboard'),

        url(r'^manage/accounts/$', views.UserList.as_view(), name='user_list'),
        url(r'^manage/accounts/new$', views.StaffCreate.as_view(), name='staff_register'),
        url(r'^manage/accounts/delete/(?P<pk>[0-9]+)/', views.UserDelete.as_view(), name='user_del'),
        url(r'^manage/accounts/(?P<pk>[0-9]+)/', views.UserDetail.as_view(), name='user_detail'),

        url(r'^records/$', views.PatientList.as_view(), name='rec_list'),
        url(r'^records/new/$', views.RecordCreate.as_view(), name='rec_new'),
        url(r'^records/mine/$', views.view_records, name='rec_pt'),
        url(r'^records/list/(?P<pk>[0-9]+)/$', views.view_records, name='rec_dr'),
        url(r'^records/update/(?P<pk>[0-9]+)$', views.RecordUpdate.as_view(), name='rec_dr_update'),
        url(r'^records/export/(?P<pk>[0-9]+)$', views.export_record, name='rec_exp'),

        url(r'^appointments/new/$', views.create_appt, name='appt_new'),
        url(r'^appointments/(?P<pk>[0-9]+)/', views.update_appt, name='appt_upd'),
        url(r'^appointments/delete/(?P<pk>[0-9]+)/', views.delete_appt, name='appt_del'),

        url(r'^hospitals/new/$', views.HospitalCreate.as_view(), name='hosp_new'),
        url(r'^hospitals/update/(?P<pk>[0-9]+)/', views.HospitalCreate.as_view(), name='hosp_new'),
        url(r'^hospitals/admit/(?P<pk>[0-9]+)/', views.admit_patient, name='admit_ptnt'),
        url(r'^hospitals/discharge/(?P<pk>[0-9]+)/', views.discharge_patient, name='dsch_ptnt'),
        url(r'^hospitals/transfer/(?P<pk>[0-9]+)/', views.TransferPatient.as_view(), name='transf_hosp'),
        url(r'^messages/new/', views.SendMessage.as_view(), name='send_msg'),

        url(r'^$', views.index, name='home'),
        url(r'^logout/$', views.logout_view, name='logout')
    ]