import requests
from bs4 import BeautifulSoup

# 尝试获取网页内容
try:
    response = requests.get("https://docs.openclaw.ai/zh-CN/concepts/architecture")
    soup = BeautifulSoup(response.content, 'html.parser')
    print("成功获取网页内容")
    # 查找主要内容
    content = soup.get_text()
    # 截取部分内容显示
    print(content[:1000])
except Exception as e:
    print(f"获取网页内容失败: {e}")
    # 使用默认的架构信息
    print("将使用默认的OpenClaw架构信息")
