#from django.shortcuts import render

# Create your views here.


def decode_student_response(encoded_response):
    return encoded_response.split("#")

def encode_student_response(decoded_response):
    return "#".join(decoded_response)

def decode_answerkey(encoded_key):
    return encoded_key.split("#")

def encode_answerkey(decoded_key):
    return "#".join(decoded_key)

def decode_marking_scheme(encoded_scheme):
    first=encoded_scheme.split("#")
    second=[]
    for i in first:
        second.append([int(x) for x in i.split("_")])
    return second

def encode_marking_scheme(decoded_scheme):
    first=[]
    for i in decoded_scheme:
        first.append("_".join(i))
    return "#".join(first)

def grade_answersheet(student_response,decoded_marking,decoded_answerkey):
    #decoded_answerkey=decoded_answerkey(answer_key)
    decoded_response=decode_student_response(student_response)
    #decoded_marking=decode_marking_scheme(marking_scheme)
    marks=0
    l=len(decoded_marking)
    for i in range(0,l):
        if decoded_answerkey[i]=="add":
            marks+=int(decoded_marking[i][0])
        elif decoded_response[i]=="":
            pass
        elif decoded_response[i] in decoded_answerkey[i]:
            marks+=int(decoded_marking[i][0])
        else:
            marks-=int(decoded_marking[i][1])
    return marks


def grade_exam(student_responses_dict,marking_scheme,answer_key):
    decoded_answerkey=decode_answerkey(answer_key)
    decoded_marking=decode_marking_scheme(marking_scheme)
    marks_dict=dict([])
    for i in student_responses_dict:
        response_list=student_responses_dict[i]
        marks_dict[i]=grade_answersheet(response_list,decoded_marking,decoded_answerkey)
    mark_rank_list=sort_marks(marks_dict)
    mark_rank_dict=dict([])
    for i in mark_rank_list:
        mark_rank_dict[i[0]]=[i[1],i[2]]
    return mark_rank_dict


def sort_marks(marks_dict):
    marks_list=[]
    for i in marks_dict:
        marks_list.append([i,marks_dict[i]])
    marks_list.sort(key = lambda x :x[1],reverse=True)
    mark_rank_list=[]
    rank=0
    marks=float('inf')
    for i in marks_list:
        if i[1]<marks:
            marks=i[1]
            rank=rank+1
        mark_rank_list.append([i[0],i[1],rank])
    return mark_rank_list


def calculate_totalmarks(marking_scheme):
    decoded_marking=marking_scheme
    marks=0
    for i in decoded_marking:
        marks+=int(i[0])
    return marks
