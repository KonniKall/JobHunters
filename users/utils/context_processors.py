from django.contrib.auth.models import User
from ..models import JobSeeker, Employer
from django.contrib.auth.decorators import login_required

@login_required
def user_type(request):  
    user_type = JobSeeker.objects.filter(user=request.user).first()
    if user_type == None:
        user_type = Employer.objects.filter(user=request.user).first()
    return {'user_type': user_type}