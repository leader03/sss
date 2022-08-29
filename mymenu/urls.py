
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views

urlpatterns = [
        path('', HomeView, name="home"),
        path('exclusive', ExclusiveView, name="exclusive"),
        path('special', SpecialView, name="special"),
        path('qrupdate_item/', updateItem, name = "qrupdateItem"),
        path('search', SearchView.as_view(), name="search"),
        path('dashboard', Dashboard, name="dashboard"),
        path('add_product', AddProduct, name="addproduct"),
        path('edit_product/<str:pk>', EditProduct, name="editproduct"),
        path('add_category', AddCategory, name="addcategory"),
        path('edit_category/<str:pk>', EditCategory, name="editcategory"),
        path('product_list/<str:pk>', CategoryDetail, name="categorydetail"),
        path('add_exclusive', AddExclusive, name="addexclusive"),
        path('add_special', AddSpecial, name="addspecial"),
        path('delete_special/<str:pk>', DeleteSpecial, name="delete-special"),
        path('delete_exclusive/<str:pk>', DeleteExclusive, name="delete-exclusive"),
        path('edit_exclusive/<str:pk>', EditExclusive, name="edit-exclusive"),
        path('deleteproduct/<str:pk>', DeleteProduct, name="deleteproduct"),
        path('deletecategory/<str:pk>', DeleteCategory, name="deletecategory"),

        path('register', RegistrationView.as_view(), name="register"),
]
if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

