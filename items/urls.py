from django.urls import path


from . import views

urlpatterns = [
    path('get_items/', views.ItemsList.as_view()),
    path('get/<int:id>', views.GetItem.as_view()),
    path('item_create/', views.CreateItem.as_view())
]