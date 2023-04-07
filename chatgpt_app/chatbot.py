import os
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "


@csrf_exempt
def chatingGPT(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        prompt = f"{restart_sequence}{message}{start_sequence}"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        answer = response.choices[0].text.strip()
        return JsonResponse({'answer': answer})
