from django.urls import path

from .views import SignInView, ProfileView, ApplicationsView, JobListingsView, JobListingView, WorkplacesView, WorkplaceView, EditProfileView, JobListingApplicationView, SignUpView, UsernameCheckView, EmailCheckView

from listings.views import ApplicationView

from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.listings, name='listings-page'),
    path("sign-in/", SignInView.as_view(), name="sign-in"),
    path("sign-up/", SignUpView.as_view(), name="sign-up"),
    path("sign-up/user/<str:username>/", UsernameCheckView.as_view(), name="username-check"),
    path("sign-up/email/<str:email>/", EmailCheckView.as_view(), name="email-check"),
    path('sign-out/', auth_views.LogoutView.as_view(template_name='users/sign-out.html'), name='sign-out'),

    path('profile/', ProfileView.as_view(), name='profile'),
    path("profile/edit", EditProfileView.as_view(), name="edit-profile"),
    path('profile/applications/', ApplicationsView.as_view(), name='sent-applications'),
    path('profile/applications/<str:application>/', ApplicationView.as_view(), name='sent-applications'),
    

    path('profile/job-listings/', JobListingsView.as_view(), name='my-job-listings'),
    path('profile/job-listings/<str:job_listing>/', JobListingView.as_view(), name='my-job-listings'),
    path('profile/job-listings/<str:job_listing>/<str:application>/', JobListingApplicationView.as_view(), name='my-job-listings'),
    path('profile/job-listings/<str:job_listing>/<str:application>/<str:decision>/', JobListingApplicationView.as_view(), name='my-job-listings'),
    path('delete/job-listing/<str:job_listing>/', JobListingView.as_view(), name='delete-job-listing'),

    path('workplaces/', WorkplacesView.as_view(), name='workplaces'),
    path('workplaces/<str:workplace>/', WorkplaceView.as_view(), name='workplaces'),

    # path('workplaces/<int:id>/', WorkplaceView.as_view(), name='workplace-detail'),

]
