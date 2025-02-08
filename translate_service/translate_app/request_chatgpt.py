import requests
import json
from django.conf import settings

# create request function
def request_chatgpt(Translate, field, topic,  fromlangue, tolangue):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': settings.AUTHORIZATION,
        'Cookie': settings.COOKIE
    }
    data = {
        "model": "ft:gpt-4o-2024-08-06:personal::AyOtjnSS",
        "messages": [
            {
                "role": "system",
                "content": "GPT là một chatbot lịch sự và không sử dụng từ ngữ phân biệt chủng tộc và không khuyến khích bạo lực, không sử dụng nội dung khiêu dâm, không phân biệt vùng miền"
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Field: {field}, Topic: {topic}, Translate from {fromlangue} to {tolangue}: {Translate}, just return result, no need any description."
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

