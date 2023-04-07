
from django.shortcuts import render
from django.http import JsonResponse
# chatgpt_app/chatbot.py
from chatgpt_app.chatbot import chatingGPT

def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        prompt = f"{restart_sequence}{message}{start_sequence}"
        answer = chatingGPT(prompt)
        return JsonResponse({'answer': answer})
    return render(request, 'chatgpt_app/chat.html')
