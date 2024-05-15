from django.urls import path

from .views import SignInView, ProfileView, ApplicationsView, ApplicationView, JobListingsView, JobListingView, WorkplacesView, WorkplaceView

from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.listings, name='listings-page'),
    path("sign-in/", SignInView.as_view(), name="sign-in"),
    path('sign-out/', auth_views.LogoutView.as_view(template_name='users/sign-out.html'), name='sign-out'),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/applications/', ApplicationsView.as_view(), name='sent-applications'),
    path('profile/applications/<str:application>/', ApplicationView.as_view(), name='sent-applications'),

    path('profile/job-listings/', JobListingsView.as_view(), name='my-job-listings'),
    path('profile/job-listings/<str:job_listing>/', JobListingView.as_view(), name='my-job-listings'),

    path('workplaces/', WorkplacesView.as_view(), name='workplaces'),
    path('workplaces/<str:workplace>/', WorkplaceView.as_view(), name='workplaces'),
]
