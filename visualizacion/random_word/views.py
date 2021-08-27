from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def show_word(request):
    try:
        request.session['attempts'] += 1
    except KeyError:
        request.session['attempts'] = 1
    finally:
        context = {}

        word = generate_word()
        context["word"] = word

        return render(request, 'show_word.html', context)


def reset_attempts(request):
    request.session['attempts'] = 0

    return redirect('word_generator')


def generate_word():
    return get_random_string(length=14)
