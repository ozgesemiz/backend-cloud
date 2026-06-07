import base64
import io
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from PIL import Image
import json

@csrf_exempt
@require_http_methods(["POST"])
def get_resolution(request):
    try:
        data = json.loads(request.body)
        image_base64 = data.get('image', '')
        image_bytes = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_bytes))
        width, height = image.size
        return JsonResponse({
            'width': width,
            'height': height,
            'resolution': f'{width}x{height}'
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["POST"])
def convert_grayscale(request):
    try:
        data = json.loads(request.body)
        image_base64 = data.get('image', '')
        image_bytes = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_bytes))
        grayscale = image.convert('L')
        buffer = io.BytesIO()
        grayscale.save(buffer, format='PNG')
        buffer.seek(0)
        grayscale_base64 = base64.b64encode(buffer.read()).decode('utf-8')
        return JsonResponse({'image': grayscale_base64})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
