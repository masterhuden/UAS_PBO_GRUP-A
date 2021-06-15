from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def masuk(request):
    return render(request, "masuk.html")


def error(request):
    return render(request, "error.html")


def kumpulform(request):
    return render(request, "kumpulform.html")


def konsultasi(request):
    return render(request, "konsul.html")


def jadwal(request):
    return render(request, "jadwal.html")
