import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 初始化 DeepSeek 客户端
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL"),
)

def chat_with_deepseek(user_input: str) -> str:
    """调用 DeepSeek 模型，返回回答"""
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个乐于助人的AI助手，回答简洁清晰。"},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("=== DeepSeek Chatbot 已启动 ===")
    print("输入 'quit' 或 'exit' 退出对话\n")
    while True:
        user_input = input("你: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Bot: 再见！")
            break
        answer = chat_with_deepseek(user_input)
        print(f"Bot: {answer}\n")