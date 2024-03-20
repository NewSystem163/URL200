import requests

# 从文本文件中读取URL并添加到列表中
def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file]
    return urls

# 检查URL格式，如果没有http://则添加，然后发送请求以获取状态码为200的URL
def check_and_request_urls(urls):
    for url in urls:
        if not url.startswith('http'):
            url = 'http://' + url
        try:
            response = requests.get(url, timeout=5)  # 设置超时时间为5秒
            if response.status_code == 200:
                print(url)
        except (requests.exceptions.RequestException, requests.exceptions.SSLError, requests.exceptions.ConnectTimeout) as e:
            pass

# 要检测的URL列表
file_path = '/Users/newsystem/Desktop/ip.txt'
urls = read_urls_from_file(file_path)

# 检查URL格式并发送请求以获取状态码为200的URL
check_and_request_urls(urls)
