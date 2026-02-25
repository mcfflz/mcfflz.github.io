#!/usr/bin/env python3
"""
Web Search Script for Claude Code Skill
支持多个搜索引擎：DuckDuckGo、Bing、Google、SearXNG
"""

import argparse
import json
import os
import re
import sys
from typing import List, Dict, Optional
from urllib.parse import quote_plus, urlparse

# 尝试导入可选依赖
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError as e:
    print(f"错误：缺少必要的依赖包。请运行：pip install requests beautifulsoup4")
    sys.exit(1)


def search_duckduckgo(query: str, num_results: int = 5) -> List[Dict]:
    """
    使用 DuckDuckGo 搜索（无需 API Key）
    """
    try:
        from duckduckgo_search import DDGS
    except ImportError:
        print("警告：未安装 duckduckgo-search，尝试使用备用方法...")
        return search_duckduckgo_fallback(query, num_results)

    results = []
    try:
        with DDGS() as ddgs:
            ddg_results = ddgs.text(query, max_results=num_results)
            for r in ddg_results:
                results.append({
                    "title": r.get("title", ""),
                    "url": r.get("href", ""),
                    "snippet": r.get("body", ""),
                    "source": "DuckDuckGo"
                })
    except Exception as e:
        print(f"DuckDuckGo 搜索失败: {e}")
        return search_duckduckgo_fallback(query, num_results)

    return results


def search_duckduckgo_fallback(query: str, num_results: int = 5) -> List[Dict]:
    """
    DuckDuckGo 备用搜索方法（HTML 解析）
    """
    results = []
    try:
        # DuckDuckGo HTML 端点
        url = f"https://html.duckduckgo.com/html/?q={quote_plus(query)}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=30)
        soup = BeautifulSoup(response.content, 'html.parser')

        # 解析搜索结果
        result_divs = soup.find_all('div', class_='result')[:num_results]

        for div in result_divs:
            try:
                title_elem = div.find('a', class_='result__a')
                snippet_elem = div.find('a', class_='result__snippet')

                if title_elem and snippet_elem:
                    results.append({
                        "title": title_elem.get_text(strip=True),
                        "url": title_elem.get('href', ''),
                        "snippet": snippet_elem.get_text(strip=True),
                        "source": "DuckDuckGo"
                    })
            except Exception:
                continue

    except Exception as e:
        print(f"备用搜索方法也失败了: {e}")

    return results


def search_bing(query: str, num_results: int = 5, api_key: Optional[str] = None) -> List[Dict]:
    """
    使用 Bing Search API（需要 API Key）
    """
    api_key = api_key or os.getenv("BING_API_KEY")
    if not api_key:
        print("错误：使用 Bing 搜索需要提供 BING_API_KEY")
        return []

    results = []
    try:
        endpoint = "https://api.bing.microsoft.com/v7.0/search"
        headers = {"Ocp-Apim-Subscription-Key": api_key}
        params = {
            "q": query,
            "count": num_results,
            "textDecorations": False,
            "textFormat": "HTML"
        }

        response = requests.get(endpoint, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        for item in data.get("webPages", {}).get("value", []):
            results.append({
                "title": item.get("name", ""),
                "url": item.get("url", ""),
                "snippet": item.get("snippet", ""),
                "source": "Bing"
            })

    except Exception as e:
        print(f"Bing 搜索失败: {e}")

    return results


def search_google(query: str, num_results: int = 5, api_key: Optional[str] = None,
                  cse_id: Optional[str] = None) -> List[Dict]:
    """
    使用 Google Custom Search API（需要 API Key 和 CSE ID）
    """
    api_key = api_key or os.getenv("GOOGLE_API_KEY")
    cse_id = cse_id or os.getenv("GOOGLE_CSE_ID")

    if not api_key or not cse_id:
        print("错误：使用 Google 搜索需要提供 GOOGLE_API_KEY 和 GOOGLE_CSE_ID")
        return []

    results = []
    try:
        from googleapiclient.discovery import build

        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=query, cx=cse_id, num=num_results).execute()

        for item in res.get("items", []):
            results.append({
                "title": item.get("title", ""),
                "url": item.get("link", ""),
                "snippet": item.get("snippet", ""),
                "source": "Google"
            })

    except ImportError:
        print("错误：使用 Google 搜索需要安装 google-api-python-client")
    except Exception as e:
        print(f"Google 搜索失败: {e}")

    return results


def fetch_webpage_content(url: str, timeout: int = 30) -> Optional[str]:
    """
    获取网页的完整文本内容
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        }

        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
        response.raise_for_status()

        # 检测编码
        if response.encoding == 'ISO-8859-1':
            response.encoding = response.apparent_encoding

        soup = BeautifulSoup(response.content, 'html.parser')

        # 移除不需要的元素
        for elem in soup(['script', 'style', 'nav', 'header', 'footer', 'aside', 'advertisement']):
            elem.decompose()

        # 尝试找到主要内容区域
        content_selectors = [
            'main', 'article', '[role="main"]',
            '.content', '.post-content', '.article-content',
            '#content', '#main-content',
            '.entry-content', '.post'
        ]

        main_content = None
        for selector in content_selectors:
            main_content = soup.select_one(selector)
            if main_content:
                break

        if main_content:
            text = main_content.get_text(separator='\n', strip=True)
        else:
            # 回退到 body
            body = soup.find('body')
            text = body.get_text(separator='\n', strip=True) if body else ""

        # 清理文本
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        text = '\n'.join(lines)

        # 限制长度
        max_length = 10000
        if len(text) > max_length:
            text = text[:max_length] + "...\n[内容已截断]"

        return text

    except Exception as e:
        return f"[无法获取内容: {e}]"


def summarize_content(content: str, max_chars: int = 200) -> str:
    """
    生成内容的简短摘要
    """
    if not content:
        return ""

    # 移除多余空白
    content = ' '.join(content.split())

    # 如果内容较短，直接返回
    if len(content) <= max_chars:
        return content

    # 尝试在句子边界截断
    truncated = content[:max_chars]
    last_period = max(truncated.rfind('.'), truncated.rfind('。'), truncated.rfind('!'), truncated.rfind('！'))

    if last_period > max_chars * 0.5:
        return truncated[:last_period + 1]
    else:
        return truncated + "..."


def main():
    parser = argparse.ArgumentParser(description='Web Search Tool for Claude Code')
    parser.add_argument('--query', '-q', required=True, help='搜索关键词')
    parser.add_argument('--engine', '-e', default='duckduckgo',
                        choices=['duckduckgo', 'bing', 'google'],
                        help='搜索引擎 (默认: duckduckgo)')
    parser.add_argument('--num-results', '-n', type=int, default=5,
                        help='结果数量 (默认: 5)')
    parser.add_argument('--fetch-content', '-f', action='store_true',
                        help='是否获取完整网页内容')
    parser.add_argument('--output', '-o', default=None,
                        help='输出文件路径 (默认输出到 stdout)')
    parser.add_argument('--json', '-j', action='store_true',
                        help='以 JSON 格式输出')

    args = parser.parse_args()

    # 执行搜索
    print(f"正在使用 {args.engine} 搜索: {args.query}", file=sys.stderr)

    if args.engine == 'duckduckgo':
        results = search_duckduckgo(args.query, args.num_results)
    elif args.engine == 'bing':
        results = search_bing(args.query, args.num_results)
    elif args.engine == 'google':
        results = search_google(args.query, args.num_results)
    else:
        results = []

    if not results:
        print("未找到搜索结果", file=sys.stderr)
        sys.exit(1)

    # 获取完整内容（如果需要）
    if args.fetch_content:
        print("正在获取网页内容...", file=sys.stderr)
        for i, result in enumerate(results):
            print(f"  [{i+1}/{len(results)}] {result['url']}", file=sys.stderr)
            content = fetch_webpage_content(result['url'])
            result['content'] = content
            result['summary'] = summarize_content(content, 300)

    # 格式化输出
    output_data = {
        "query": args.query,
        "engine": args.engine,
        "num_results": len(results),
        "results": results
    }

    if args.json:
        output = json.dumps(output_data, ensure_ascii=False, indent=2)
    else:
        # Markdown 格式
        lines = [
            f"## 搜索结果: {args.query}",
            "",
            f"**搜索引擎**: {args.engine}",
            f"**结果数量**: {len(results)} 条",
            "",
            "---",
            ""
        ]

        for i, r in enumerate(results, 1):
            lines.extend([
                f"### {i}. {r['title']}",
                f"**来源**: [{urlparse(r['url']).netloc}]({r['url']})",
                "",
                f"**摘要**: {r['snippet']}",
                ""
            ])

            if 'summary' in r:
                lines.extend([
                    f"**内容总结**: {r['summary']}",
                    ""
                ])

            if 'content' in r and r['content']:
                content_preview = r['content'][:500] + "..." if len(r['content']) > 500 else r['content']
                lines.extend([
                    "<details>",
                    "<summary>查看完整内容</summary>",
                    "",
                    "```",
                    content_preview,
                    "```",
                    "</details>",
                    ""
                ])

            lines.append("---")
            lines.append("")

        output = '\n'.join(lines)

    # 输出结果
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"结果已保存到: {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == '__main__':
    main()
