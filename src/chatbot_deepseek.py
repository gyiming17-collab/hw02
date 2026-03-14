import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载环境变量（从.env文件读取API Key）
load_dotenv()

# 初始化DeepSeek客户端
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
)

def deepseek_chatbot(user_query: str) -> str:
    """
    调用DeepSeek模型实现Chatbot功能
    :param user_query: 用户输入的文本问题
    :return: 模型生成的回答
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",  # DeepSeek通用对话模型
            messages=[
                {"role": "system", "content": "你是专业的AI助手，擅长解答技术问题，回答简洁准确"},
                {"role": "user", "content": user_query}
            ],
            temperature=0.6,  # 控制回答随机性
            max_tokens=1024    # 最大生成长度
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"调用失败：{str(e)}（请检查API Key是否正确，网络是否通畅）"

if __name__ == "__main__":
    print("=== DeepSeek Chatbot 启动成功（输入'quit'退出）===")
    while True:
        user_input = input("\n你：")
        if user_input.lower() == "quit":
            print("Bot：再见！")
            break
        result = deepseek_chatbot(user_input)
        print(f"Bot：{result}")