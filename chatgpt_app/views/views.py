from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from ..chatgpt import generate_text

def home(request):
    template_name = 'chatgpt_app/index.html'
    return render(request, template_name)


def generate_text_view(request):
    prompt = request.GET.get('prompt', '')
    bot_generate_text = generate_text(prompt)
    return JsonResponse({'text': bot_generate_text})
