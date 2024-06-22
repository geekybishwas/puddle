from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm
app_name='core'

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name='login')
]

# When a user accesses /login/, the LoginView will be responsible for:

# Rendering a login form template (you'll need to create this template separately).
# Handling form submission, which involves validating the username and password against the database.
# Authenticating the user upon successful validation (logging them in).
# Redirecting the user to a specific page after successful login (you can configure this using the redirect_field_name or LOGIN_REDIRECT_URL settings).