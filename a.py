import json
from openai import OpenAI
from tenacity import retry, wait_random_exponential, stop_after_attempt
from termcolor import colored  


client = OpenAI(api_key="")


messages = [{"role": "system", "content": "니 이름은 pepper이고 너는 경남대학교 1공학관 8층에 위치해있다."},#""이걸로 줄 바꿔도 한줄로 인식 가능
            {"role": "assistant", "content": "중앙계단은 컴퓨터 응용실습실 맞은편에 위치해있다."}]

msg = "중앙계단"
#받은 메시지 GPT한테 전달
content = msg
messages.append({"role":"user", "content":content})
completion = client.chat.completions.create(
    model="gpt-3.5-turbo", messages=messages
    # model="gpt-4o", messages=messages
)
chat_response = completion.choices[0].message
print('GPT msg: {chat_response}')
msg2 = chat_response 
print(msg2.content)