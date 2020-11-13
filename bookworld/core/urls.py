from django.urls import path

from .import views
urlpatterns = [
    path('signup/',views.sign_up,name="signup"),
    path('login/',views.user_login,name="login"),
    path('dashboard/',views.user_dashboard,name="dashboard"),
    path('logout/',views.user_logout,name="logout"),
    path('deleteuser/<int:id>/',views.delete_user,name="deleteuser"),
    path('<int:id>/',views.edit_user,name="updateuser"),
    path('bookcategory/',views.book_category_admin_panel,name="adminbookcategory"),
    path('deletebookcategory/<int:id>/',views.delete_book_category,name="deletebookcategory"),
    path('updatebookcategory/<int:id>/',views.edit_book_category,name="updatebookcategory"),
    path('addbookcategory/',views.add_book_category,name="addbookcategory"),
    path('availablebook/',views.available_book_function,name="availablebook"),
    path('deleteavailablebook/<int:id>/',views.delete_available_book,name="deleteavailablebook"),
    path('editavailablebook/<int:id>/',views.edit_available_book,name="editavailablebook"),
    path('addbook/',views.add_book,name="addbook"),
    path('buybook/<int:id>/',views.buy_book_function,name="buybook"),
    path('showbook/',views.show_ordered_book,name="showbook"),
    path('deleterequest/<int:id>/',views.delete_request,name="deleterequest"),
    path('assignrequest/<int:id>/',views.assign_request,name="assignrequest"),
    path('selecetedcategory/<str:category>/',views.select_category,name="selectedcategory"),
    path('searchresult/',views.user_dashboard,name="searchresult"),
    path('contact/',views.contact_us,name="contact"),
]
