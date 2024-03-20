from openai import OpenAI

# 輸入API_KEY
client = OpenAI(
    api_key="YOUR_API_KEY"
)

# 將新聞內文儲存至 /content/NewsContent.txt 並讀取
with open("/content/NewsContent.txt", "r") as file:
    file_content = file.read()

# 要求ChatGPT總結所有收到的文章並發送request
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "總結所有你接收到的文章"},
        {"role": "user", "content": file_content}
    ]
)

# 印出ChatGPT的Response
print(response.choices[0].message.content)

# -----參考資料-----
# OpenAI官方文件: https://platform.openai.com/docs/introduction
# ChatGPT
