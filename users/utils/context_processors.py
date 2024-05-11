from django.contrib.auth.models import User
from ..models import JobSeeker, Employer
from django.contrib.auth.decorators import login_required

from django.template import Context

def user_type(request):
    if request.user.is_authenticated:
        user_type = JobSeeker.objects.filter(user=request.user).first()
        if user_type == None:
            user_type = Employer.objects.filter(user=request.user).first()
        return {'user_type': user_type}
    return {}