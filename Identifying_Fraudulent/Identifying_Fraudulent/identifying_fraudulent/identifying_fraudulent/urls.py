"""netfense URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from Remote_User import views as remoteuser
from Service_Provider import views as serviceprovider
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', remoteuser.login, name="login"),
    path('Register1/', remoteuser.Register1, name="Register1"),
    path('Detection_Of_Fraudulent_CreditCard_Transactions/', remoteuser.Detection_Of_Fraudulent_CreditCard_Transactions,
         name="Detection_Of_Fraudulent_CreditCard_Transactions"),
    path('ViewYourProfile/', remoteuser.ViewYourProfile, name="ViewYourProfile"),

    path('serviceproviderlogin/', serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    path('View_Remote_Users/', serviceprovider.View_Remote_Users, name="View_Remote_Users"),

    re_path(r'^charts/(?P<chart_type>\w+)$', serviceprovider.charts, name="charts"),
    re_path(r'^charts1/(?P<chart_type>\w+)$', serviceprovider.charts1, name="charts1"),
    re_path(r'^likeschart/(?P<like_chart>\w+)$', serviceprovider.likeschart, name="likeschart"),
    path('View_Detected_Of_Fraudulent_CreditCard_Transactions_Type_Ratio/',
         serviceprovider.View_Detected_Of_Fraudulent_CreditCard_Transactions_Type_Ratio,
         name="View_Detected_Of_Fraudulent_CreditCard_Transactions_Type_Ratio"),

    re_path(r'^likeschart1/(?P<like_chart1>\w+)$', serviceprovider.likeschart1, name="likeschart1"),

    path('Train_Test_DataSets/', serviceprovider.Train_Test_DataSets, name="Train_Test_DataSets"),
    path('View_Detected_Of_Fraudulent_CreditCard_Transactions_Type/',
         serviceprovider.View_Detected_Of_Fraudulent_CreditCard_Transactions_Type,
         name="View_Detected_Of_Fraudulent_CreditCard_Transactions_Type"),

    path('Download_Predicted_DataSets/', serviceprovider.Download_Predicted_DataSets,
         name="Download_Predicted_DataSets"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

