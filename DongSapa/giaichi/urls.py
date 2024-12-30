from django.urls import include, path
from . import views

urlpatterns = [
    path("giaichi/", views.GiaiChiCreateAndUpdateView.as_view(), name="giaichi-list"),
    path('giaichi/<int:pk>/', views.GiaichiDetailView.as_view(),
         name='giaichi-detail'),

    path("giaichi/create/", views.GiaiChiCreateAndUpdateView.as_view(),
         name="giaichi_create"),

    path("ckeditor/", include("ckeditor_uploader.urls")),

    path(
        "giaichi/delete/<int:pk>/",
        views.GiaichiDeleteView.as_view(),
        name="giaichi_delete",
    ),

    path(
        "giaichi/update/<int:pk>/",
        views.GiaiChiCreateAndUpdateView.as_view(),
        name="giaichi_update",
    ),


    # path(
    #     "giaichi/success/<int:form_id>/",
    #     views.GiaiChiSuccessView.as_view(),
    #     name="giaichi-success",
    # ),
]
