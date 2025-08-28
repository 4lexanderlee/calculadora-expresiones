# calculadora_api/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from calculadoraexpresiones import evaluar_expresion # Asegúrate de que esta línea sea así

@csrf_exempt
def calcular_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            expresion = data.get('expresion', None)
            if not expresion:
                return JsonResponse({"error": "No se recibió ninguna expresión."}, status=400)
            resultado = evaluar_expresion(expresion)
            return JsonResponse({"resultado": resultado}, status=200)
        except (ValueError, ZeroDivisionError, IndexError, json.JSONDecodeError) as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método no permitido."}, status=405)