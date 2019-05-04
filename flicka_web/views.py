from django.shortcuts import redirect


def main_view(request):
    return redirect('/static/index.html')