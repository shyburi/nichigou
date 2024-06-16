from openai import OpenAI
#OpenAI APIキーの設定
# client = OpenAI(api_key='')

#OpenAI API
response1 = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "入力された言葉を表す漢字一字を出力してください。漢字一字以外は何も出力しないでください。"},
    #以下に質問を入力
    {"role": "user", "content": input("今日の予定を教えてください。")}
  ]
)

response2 = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "入力された言葉を表す漢字一字を出力してください"},
    #以下に質問を入力
    {"role": "user", "content": input("今日の雰囲気を教えてください。")}
  ]
)

answer1 = response1.choices[0].message.content
answer2 = response2.choices[0].message.content
answer3 = str(answer1 + answer2)
print("今日の日号は" + answer3 + "です。")