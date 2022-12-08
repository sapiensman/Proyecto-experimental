
from django.shortcuts import render
# el request es un diccionario que continuamente se va pasando entre el navegador y el servidor

def Home(request):

	return render(request, 't_home.html')

def Nosotros(request):

	# el request es un diccionario que se va pasando entre el navegador y el servidor

	return render(request, 't_nosotros.html')


def somos(request):

	# el request es un diccionario que se va pasando entre el navegador y el servidor

	return render(request, 't_quienes_somos.html')
