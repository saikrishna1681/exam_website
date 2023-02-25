#from views import *
from django.urls import path
from  . import views
from django.views.generic import TemplateView


urlpatterns=[

    path("logout",views.logout_view,name="logout"),
    path("login_page",views.login_page,name="login_page"),
    path("login",views.login_view,name="login_function"),
    path("home", views.home,name="home"),
    path("hello", views.hello,name="hello"),
    
    path("login_to_exam",views.login_to_exam,name="login_to_exam"),
    path("login_to_exam_page",views.login_to_exam_page,name="login_to_exam_page"),
    path("save_answer",views.save_answer,name="save_answer"),
    path("get_question_statements",views.get_question_statements,name="get_question_statements"),
    path("view_question/<int:question_no>", views.view_question,name="view_question"),
    path("my_exams",views.my_exams,name="my_exams"),
    path('view_myexam_responses/<int:exam_id>',views.myexam_responses,name="myexam_responses"),


    path("staff/grade_exam/<int:exam_id>",views.grade_exam_view,name="grade_exam_view"),
    path("staff/upload_answerkey",views.upload_answerkey,name="upload_answerkey"),
    path("staff/view_examquestions/<int:exam_id>",views.view_examquestions,name="view_examquestions"),
    path("staff/add_examquestion/<int:exam_id>",views.add_examquestion,name="add_examquestion"),
    path("staff/update_examquestion/<int:exam_id>",views.update_examquestion,name="update_examquestion"),
    path("staff/viewall_exams",views.viewall_exams,name="viewall_exams"),
    path("staff/update_examdata/<int:exam_id>",views.update_examdata,name="update_examdata"),
    path("staff/view_examresult/<int:exam_id>",views.view_examresult,name="view_examresult"),
    path("staff/delete_examquestion/<int:exam_id>/<int:question_id>",views.delete_examquestion,name="delete_examquestion"),

    path("staff/logout",views.staff_logout_view,name="logout"),
    path("staff/login_page",views.staff_login_page,name="login_page"),
    path("staff/login",views.staff_login_view,name="login_function"),
    path("staff/home", views.staff_home,name="home"),


    path('frontend/', TemplateView.as_view(template_name="index.html")),
    path('static/<str:extra>', TemplateView.as_view(template_name="index.html")),
    path("manifest.json", TemplateView.as_view(template_name="index.html"))



]