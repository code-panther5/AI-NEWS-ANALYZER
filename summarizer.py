import requests

system_prompt = """
You are a professional NEWS ANALYST.
Analyze the news article and produce a structured NEWS INTELLIGENCE REPORT in the exact format below:

📰 NEWS INTELLIGENCE REPORT
Headline:
Source:
Date (if available):
Region/Country:

Summary (3-5 bullet points):

Who is Affected:
Key Stakeholders:

Main Issue:
Reason Behind It:

Short-Term Impact:
Long-Term Impact:

Risk Level: Low / Medium / High
Bias Check: Neutral / Mild Bias / Strong Bias

Important Facts Extracted:
- 
- 
- 

Final Takeaway (1 paragraph):
"""

def fetch_website_contents(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text

def messages_for(article_text):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Analyze the following news article:\n\n" + article_text}
    ]

def analyze_news(url):
    article_content = fetch_website_contents(url)

    resp = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "gemma3:1b",
            "messages": messages_for(article_content),
            "stream": False
        },
        timeout=60
    )

    return resp.json()["message"]["content"]

if __name__ == "__main__":
    test_url = "https://www.bbc.com/news/world"
    print(analyze_news(test_url))
