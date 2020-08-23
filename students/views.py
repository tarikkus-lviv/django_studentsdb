# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for students

def students_list(request):
    students =(
        {'id':1,
        'first_name':'Тарас',
        'last_name':'Куцяба',
        'ticket':'234',
        'image':'img/021A6492_SGarvas.jpg'},
        {'id':2,
        'first_name':'Оксанка',
        'last_name':'Насаляк',
        'ticket':'987',
        'image':'img/DSC05605.jpg'},
        {'id':3,
        'first_name':'Олег',
        'last_name':'Куцяба',
        'ticket':'456',
        'image':'img/DSC05699.jpg'}
    )
    return render(request, 'students/students_list.html', {'students':students})

def students_add(request):
    return HttpResponse('<h1>Add a student</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit a student %s</h1>' %sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete a student %s</h1>' %sid)



# Views for groups
def groups_list(request):
    return render(request, 'students/groups_list.html')

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
