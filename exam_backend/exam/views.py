from django.shortcuts import render, redirect
from .models import *
from .useful_functions import *
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from .decorators import *
# Create your views here.

def decode_json(s):
    return json.loads(s.decode('utf-8'))

def hello(request):
    # print(request.COOKIES,'cokkies')
    # print(request.session.__dict__,'session')
    #request.session["test_cookie"]='12'
    response=HttpResponse("done")
    #response.set_cookie("aa","bb")
    return response

def home(request):
    return render(request,"Student/Home.html")

def login_page(request):
    return render(request,"Student/Login.html")

def login_view(request):

    # print(request.COOKIES,'cookies')
    # print(request.session["test_cookie"],'test_cookie')
    # print(request.session.__dict__,'session_dict')
    # username=decode_json(request.body)["username"]
    # password=decode_json(request.body)["password"]
    # username='sai'
    # password='sai'
    username=request.POST["username"]
    password=request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None and user.user_data.is_student==True:
        login(request, user)
        request.session["is_student"]=True
        messages.success(request,"successfully logged in")
        return render(request,"Student/Home.html")
        
    else:
        messages.success(request,"invalid credentials")
        return render(request,"Home.html")
        
    
    response=HttpResponse("done")
    #request.session["name"]="12"
    #return render(request,"index.html")
    return response
        

def logout_view(request):
    logout(request)
    return render(request,"Student/Home.html")


def staff_home(request):
    return render(request,"Staff/Home.html")


def staff_login_page(request):
    return render(request,"Staff/Login.html")

def staff_login_view(request):

    username=request.POST["username"]
    password=request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None and user.user_data.is_admin==True:
        login(request, user)
        request.session["is_student"]=False
        messages.success(request,"successfully logged in")
        return render(request,"Staff/Home.html")
        
    else:
        messages.success(request,"invalid credentials")
        return render(request,"Staff/Home.html")
        

def staff_logout_view(request):
    logout(request)
    return render(request,"Staff/Home.html")

@login_required
@is_student
def login_to_exam_page(request):
    return render(request,"Student/Login_to_Exam.html")


@login_required
@is_student
def login_to_exam(request):

    # exam_id=int(decode_json(request.body)["id"])
    # password=decode_json(request.body)["password"]
    exam_id=int(request.POST["exam_id"])
    password=request.POST["password"]
    student_id=request.user.id
    # exam_id=1
    # password="exam1"
    # student_id=1
    # if exam_id is None or password is None:
    #     messages.error(request,"invalid credentials")
    #     return render(request,"Login_to_Exam.html")
    
    exam=Exam.objects.filter(id=exam_id,password=password)
    if len(exam)==0:
        messages.error(request,"invalid credentials")
        return render(request,"Student/Login_to_Exam.html")
    
    exam=exam[0]
    request.session['exam_id']=exam_id
    no_of_questions=exam.no_of_questions
    student_response=Student_Response.objects.filter(student_id=student_id,exam_id=exam.id)
    if len(student_response)==0:
        obj=Student_Response(student_id=student_id,exam_id=exam.id)
        obj.student_response=encode_student_response(["na"]*no_of_questions)
        obj.save()
    # else:
    #     answers_list=decode_student_response(student_response[0].student_response)
    #return render(request,"Exam_page.html",{"exam_id":exam.id,"answers_list":answers_list})
    return render(request,"Student/Exam_startpage.html")

@login_required
@is_student
@is_exam_time
def get_question_statements(request):

    exam_id=1
    student_id=2
    exam_id=request.session["exam_id"]
    student_id=request.user.id
    exam=Exam.objects.get(id=exam_id)
    no_of_questions=exam.no_of_questions
    questions=exam.question_set.all()
    questions_list=[]
    for i in questions:
        questions_list.append([i.question_number,i.statement])
    questions_list.sort(key = lambda x : x[0])

    answer_list=[]
    student_response=Student_Response.objects.get(student_id=student_id,exam_id=exam_id)
    answer_list=decode_student_response(student_response.student_response)

    return JsonResponse({"questions_list":questions_list, "answer_list":answer_list, 
            "no_of_questions":no_of_questions})


@login_required
@is_student
@is_exam_time
def save_answer(request):

    # answer=decode_json(request.body)["answer"]
    exam_id=request.session["exam_id"]
    student_id=request.user.id
    # exam_id=1
    # student_id=2
    question_no=decode_json(request.body)["question_number"]
    answer=decode_json(request.body)["answer"]
    #answer=["a","b","na","c","na","na"]
    #exam_id=1
    student_response=Student_Response.objects.get(student_id=student_id,exam_id=exam_id)
    decoded=decode_student_response(student_response.student_response)
    decoded[question_no-1]=answer
    encoded=encode_student_response(decoded)
    student_response.student_response=encoded
    student_response.save()
    #messages.success(request,"answer saved succesfully")
    return HttpResponse("success")

@login_required
@is_student
def myexam_responses(request,exam_id):

    exam=Exam.objects.get(id=exam_id)
    user_id=request.user.id
    student_response=Student_Response.objects.get(student_id=user_id,exam_id=exam_id)
    my_answers=decode_student_response(student_response.student_response)
    answer_key=decode_answerkey(exam.answer_key)
    questions=exam.question_set.all()
    questions_list=[]
    for i in questions:
        questions_list.append([i.question_number,i.statement])
    questions_list.sort(key = lambda x : x[0])
    print(questions_list,answer_key,my_answers)
    data_list=[]
    for i in range(0,len(questions_list)):
        data_list.append([questions_list[i][0],questions_list[i][1],answer_key[i],my_answers[i]])
    return render(request,"Student/View_my_exam.html",{"data_list":data_list,"exam_name":exam.name,
                "student_marks":student_response.student_marks,"student_rank":student_response.student_marks})


@login_required
@is_student
@is_exam_time
def view_question(request,question_no):

    #question_no=decode_json(request.body)["question_no"]
    exam_id=request.session["exam_id"]
    question=Question.objects.get(exam_id=exam_id,question_number=question_no)
    return HttpResponse(question.statement)

@login_required
@is_student
@is_exam_time
def submit_exam(request):

    exam_id=request.session["exam_id"]
    student_response=Student_Response(student_id=request.user.id,exam_id=exam_id)
    student_response.is_submitted=True
    student_response.save()

@login_required
@is_student
def my_exams(request):

    user_id=request.user.id
    exams=Student_Response.objects.filter(student_id=user_id)
    # ["exam", "marks", "totalmarks","rank"]
    my_examdata=[]
    for exam in exams:
        my_examdata.append([exam.exam.name,exam.student_marks,exam.exam.total_marks,
            exam.student_rank,exam.exam.id])
    return render(request,"Student/My_exams.html",{'exam_list':my_examdata})

@login_required
@is_staff
def grade_exam_view(request,exam_id):

    #exam_id=decode_json(request.body)["exam_id"]
    student_responses=Student_Response.objects.filter(exam_id=exam_id)
    exam=Exam.objects.get(id=exam_id)
    answer_key=exam.answer_key
    marking_scheme=exam.marking_scheme
    student_responses_dict=dict([])
    for i in student_responses:
        student_responses_dict[i.student.id]=i.student_response
    graded_result=grade_exam(student_responses_dict,marking_scheme,answer_key)
    for i in student_responses:
        i.student_marks=graded_result[i.student.id][0]
        i.student_rank=graded_result[i.student.id][1]
        i.save()
    messages.success(request, "grading successful")
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
@is_staff
def upload_answerkey(request):

    # answer_key=decode_json(request.body)["answer_key"]
    # marking_scheme=decode_json(request.body)["marking_scheme"]
    exam_id=int(decode_json(request.body)["exam_id"])
    answer_key=["a","b","ab","add","abc","c"]
    marking_scheme=[['2','1'],['3','0'],['4','1'],['6','3'],['7','8'],['6','1']]
    encoded_marking=encode_marking_scheme(marking_scheme)
    encoded_answerkey=encode_answerkey(answer_key)
    marks=calculate_totalmarks(marking_scheme)
    exam=Exam.objects.get(id=exam_id)
    exam.marking_scheme=encoded_marking
    exam.total_marks=marks
    exam.answer_key=encoded_answerkey
    exam.save()
    return HttpResponse("done")


@login_required
@is_staff
def view_examquestions(request,exam_id):

    exam=Exam.objects.get(id=exam_id)
    # no_of_questions=exam.no_of_questions
    # answer_key=decode_answerkey(exam.answer_key)
    questions=exam.question_set.all()
    questions_list=[]
    for i in questions:
        questions_list.append([i.question_number,i.statement,i.positivemarks,i.negativemarks,i.answer])
    questions_list.sort(key = lambda x : x[0])
    # marking_scheme=decode_marking_scheme(exam.marking_scheme)
    # data=[]
    # l=len(questions_list)
    # for i in range(0,l):
    #   data.append([questions_list[i][0],questions_list[i][1],marking_scheme[i][0],marking_scheme[i][1],answer_key[i]])
    return JsonResponse({"data":questions_list, "no_of_questions":len(questions_list)})

@login_required
@is_staff
def update_examquestion(request,exam_id):

    data=decode_json(request.body)["data"]
    question=Question.objects.get(exam_id=exam_id,question_number=int(data[0]))
    question.statement=data[1]
    question.positivemarks=int(data[2])
    question.negativemarks=int(data[3])
    question.answer=data[4]
    question.save()
    return HttpResponse("success")

@login_required
@is_staff
def add_examquestion(request,exam_id):
    
    data=decode_json(request.body)["data"]
    question=Question(exam_id=exam_id,statement=data[1],positivemarks=int(data[2]),negativemarks=int(data[3]),
                      answer=data[4], question_number=int(data[0])+1)
    question.save()
    return HttpResponse("success")

@login_required
@is_staff
def delete_examquestion(request,exam_id,question_id):

    question=Question.objects.get(exam_id=exam_id,question_number=question_id)
    question.delete()
    return HttpResponse("success")

@login_required
@is_staff
def viewall_exams(request):

    exams=Exam.objects.all()
    exams_data=[]
    for i in exams:
        exams_data.append([i.id,i.name])
    return render(request , "Staff/All_examslist.html", {"exam_data":exams_data})

@login_required
@is_staff
def update_examdata(request,exam_id):

    questions=Question.objects.filter(exam_id=exam_id).order_by('question_number')
    exam=Exam.objects.get(id=exam_id)
    encoded_answerkey=''
    decoded_answerkey=[]
    marking_scheme=[]
    exam.no_of_questions=len(questions)
    maxmarks=0
    for i in questions:
        maxmarks+=i.positivemarks
        decoded_answerkey.append(i.answer)
        marking_scheme.append([str(i.positivemarks),str(i.negativemarks)])
    for i in range(0,len(questions)):
        if questions[i].question_number!=i+1:
            questions[i].question_number=i+1
            questions[i].save()
    encoded_answerkey=encode_answerkey(decoded_answerkey)
    exam.answer_key=encoded_answerkey
    exam.marking_scheme=encode_marking_scheme(marking_scheme)
    exam.save()
    messages.success(request, "updated successfully")
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
@is_staff
def view_examresult(request,exam_id):

    students=Student_Response.objects.filter(exam_id=exam_id)
    exam=Exam.objects.get(id=exam_id)
    name=exam.name
    student_data=[]
    for student in students:
        student_data.append([student.student.id,student.student.username,student.student_marks,student.student_rank])
    student_data.sort(key = lambda x :x[3])
    return render(request,"Staff/Exam_Result.html",{"student_data":student_data, "exam_id":exam_id, "exam_name":name})



