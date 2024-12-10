from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),            # Admin panel route
    path('questions/', include('questions.urls')),  # Include question management URLs
]
