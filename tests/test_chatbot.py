from src.chatbot_deepseek import deepseek_chatbot


def test_chatbot_response_format():
    """测试返回格式是否符合预期（无论成功/失败）"""
    query = "什么是多模态大语言模型？"
    response = deepseek_chatbot(query)
    assert len(response) > 0, "回答不能为空"
    print("✅ 测试1：返回格式正确（非空字符串）")


def test_chatbot_error_handling():
    """测试错误API Key时的异常处理"""
    import os
    original_key = os.getenv("DEEPSEEK_API_KEY")
    os.environ["DEEPSEEK_API_KEY"] = "invalid_key"

    query = "测试错误Key"
    response = deepseek_chatbot(query)
    assert "调用失败" in response, "未正确处理错误"
    print("✅ 测试2：异常处理成功")

    os.environ["DEEPSEEK_API_KEY"] = original_key


if __name__ == "__main__":
    test_chatbot_response_format()
    test_chatbot_error_handling()
    print("\n🎉 所有测试通过！")