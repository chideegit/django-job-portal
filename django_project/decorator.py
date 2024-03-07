from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

def check_company(view_func):
    def wrapper(request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        if user.has_company:
            messages.warning(request, 'Permission Denied. Seems you already have a company')
        response = view_func(request, *args, **kwargs) 
        return response
    return wrapper