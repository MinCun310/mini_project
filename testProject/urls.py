from django.urls import include, path

from testProject.views import ImportCSVFile, FilterView, UpdateView


urlpatterns = [
    path("csv/", include([path("test", ImportCSVFile.as_view(), name='testing')])),
    path("filter/", FilterView.as_view(), name='filter'),
    path("update/", UpdateView.as_view(), name='update')
    
]
