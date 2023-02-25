import functools
from django.shortcuts import redirect
from django.contrib import messages
from .models import Exam,Student_Response
from datetime import datetime
from django.core.exceptions import PermissionDenied

def is_valid_time(exam):

    current_time=datetime.now().timestamp()
    exam_time=exam.starttime.timestamp()
    duration=exam.duration*60
    print(current_time,exam_time,duration)
    if current_time>=exam_time and current_time< duration + exam_time:
        return True
    else:
        return False
    
def is_submitted(exam_id,user_id):
    
    obj=Student_Response.objects.get(exam_id=exam_id,user_id=user_id)
    return obj.is_submitted


def is_staff(view_func):
    """
        this decorator ensures that a user is not logged in,
        if a user is logged in, the user will get redirected to 
        the url whose view name was passed to the redirect_url parameter
    """
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session["is_student"]:
            return view_func(request,*args, **kwargs)
        messages.error(request, "must be logged in as staff")
        raise PermissionDenied

    return wrapper


def is_student(view_func):
    """
        this decorator ensures that a user is not logged in,
        if a user is logged in, the user will get redirected to 
        the url whose view name was passed to the redirect_url parameter
    """
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.session["is_student"]:
            return view_func(request,*args, **kwargs)
        messages.error(request, "must be logged in as student")
        raise PermissionDenied

    return wrapper


def is_exam_time(view_func):
    """
        this decorator ensures that a user is not logged in,
        if a user is logged in, the user will get redirected to 
        the url whose view name was passed to the redirect_url parameter
    """
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        exam_id=request.session["exam_id"]
        exam=Exam.objects.get(id=exam_id)
        if is_valid_time(exam) and not is_submitted(exam.id,request.user.id):
            return view_func(request,*args, **kwargs)
        else:
            raise PermissionDenied
    return wrapper

