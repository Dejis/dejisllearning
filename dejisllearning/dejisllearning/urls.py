from django.contrib import admin
from django.urls import path
# imported views
from dejisllearning import views

urlpatterns = [
	path('admin/', admin.site.urls),
    # configured the url
    path('',views.index, name="homepage")
]