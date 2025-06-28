from django.urls import path
from .views import register_view, login_view, logout_view
from .views import dashboard_view,feedback_form,Cart_product
from .views import chatbox,dress
from .import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('feed/',views.feedback_form, name="feedback_form"),
    path('cart/', views.view_cart, name='view_cart'),
    path('add-to-cart/', views.Cart_product, name='cart_product'),  # Existing POST handler
    path('delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('chat/',views.chatbox, name="chatbox"),
    path('dress/',views.dress,name="dress"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
