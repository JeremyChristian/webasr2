from django.conf.urls import url
from frontend import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from django.conf.urls import patterns, url

urlpatterns = format_suffix_patterns([
	url(r'^$', views.api_root),
    #  url(r'^uploads$',
    #     views.UploadList.as_view(),
    #     name='uploads'),
    # url(r'^upload/(?P<pk>[0-9]+)/$',
    #     views.UploadDetail.as_view(),
    #     name='upload'),
    url(r'^newupload$',
        views.CreateUpload.as_view(),
        name='newupload'),
    url(r'^systems$',
        views.CreateSystem.as_view(),
        name='systems'),
    # url(r'^system/(?P<pk>[0-9]+)/$',
    #     views.SystemDetail.as_view(),
    #     name='system'),
    url(r'^users$',
        views.ListUser.as_view(),
        name='users'),
    # url(r'^user/(?P<pk>[0-9]+)/$',
    #     views.UserDetail.as_view(),
    #     name='user'),
    url(r'^signup',
        views.Signup.as_view(),
        name='signup'),
  #   url(r'^api-auth/', 
  #   	include('rest_framework.urls',
		# namespace='rest_framework')),
        url(r'^login', 
        views.Login.as_view(),
        name='login'),
    url(r'^listuser', 
        views.ListUser.as_view(),
        name='listuser'),
    url(r'^uploadupdate', 
        views.UpdateUpload.as_view(),
        name='uploadupdate'),
    url(r'^authentication', 
    views.Authentication.as_view(),
    name='authentication'),
     url(r'^account', 
        views.Account.as_view(),
        name='account'),
      url(r'^signout', 
        views.Logout.as_view(),
        name='signout'),

      url(r'^about', 
        views.About.as_view(),
        name='about'),
      url(r'^news', 
        views.News.as_view(),
        name='news'),
      url(r'^conditions', 
        views.Conditions.as_view(),
        name='conditions'),
      url(r'^projects', 
        views.Projects.as_view(),
        name='projects'),
      url(r'^research', 
        views.Research.as_view(),
        name='research'),
      url(r'^publications', 
        views.Publications.as_view(),
        name='publications'),
])

# urlpatterns = [
#     url(r'^uploads/$', views.upload_list),
#     url(r'^uploads/(?P<pk>[0-9]+)/$', views.upload_detail),
#     url(r'^systems/$', views.system_list),
#     url(r'^systems/(?P<pk>[0-9]+)/$', views.system_detail),
# ]

