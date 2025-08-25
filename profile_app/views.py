from django.shortcuts import render
import random


def profile(request):
    context = {
        'name': 'Habiba Tamer',
        'age': 19,
        'hobbies': ['Reading', 'Coding', 'Traveling']
    }
    return render(request, 'profile_app/profile.html', context)

def todo_list(request):
    tasks = [
        {'title': 'Learn Django', 'done': True},
        {'title': 'Build project', 'done': False},
        {'title': 'Deploy website', 'done': False}
    ]
    return render(request, 'profile_app/todo.html', {'tasks': tasks})

def guess_number(request):
    number = random.randint(1, 10)
    user_guess = request.GET.get('guess')
    message = ''
    if user_guess:
        if int(user_guess) == number:
            message = '🎉 Correct!'
        else:
            message = f'❌ Wrong! The number was {number}'
    return render(request, 'profile_app/game.html', {'message': message})



