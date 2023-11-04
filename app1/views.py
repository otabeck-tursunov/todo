from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Todo, Student


# Create your views here.

def plans(request):
    # if request.user.is_authenticated:
        if request.method == 'POST':
            Todo.objects.create(
                name = request.POST.get('s'),
                description = request.POST.get('b'),
                date = request.POST.get('date'),
                status = request.POST.get('st'),
                student = Student.objects.get(user = request.user)
            )
            return redirect('/plans/')
        data = {
            'todo':Todo.objects.filter(student__user = request.user),
            # 'user':Todo.objects.filter(user = request.user)[0].user
        }
        return render(request, 'todo.html', data)
    # else:
    #     return redirect('/')
def loginView(request):
    if request.method == 'POST':
        user = authenticate(username = request.POST.get('l'),
                            password = request.POST.get('p'))
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/plans/')
    return render(request, 'login.html')

def logOutView(request):
    return redirect('/')

def register(request):
    if request.method == 'POST':
        u = User.objects.create_user(
            username = request.POST.get('login'),
            password = request.POST.get('parol')
        )
        Student.objects.create(
            fullname = request.POST.get('fullname'),
            guruh = request.POST.get('guruh'),
            st_raqam = request.POST.get('st_raqam'),
            tel = request.POST.get('tel'),
            user = u
        )
        return redirect('/')
    return render(request, 'register.html')

def delete(request, num):
    p = Todo.objects.get(id = num)
    if request.user == p.student.user:
        p.delete
    return redirect('/plans/')


    # if Student.objects.filter(user = request.user):
    #     Todo.objects.filter(id = num).delete()
    # return redirect('/plans/')

































