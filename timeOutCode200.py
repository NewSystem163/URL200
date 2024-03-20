import requests

# 从文本文件中读取URL并添加到列表中
def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file]
    return urls

# 要检测的URL列表
file_path = 'urls.txt'
urls = read_urls_from_file(file_path)

# 遍历URL列表并发送请求以获取状态码为200的URL
for url in urls:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(url)
    except requests.exceptions.RequestException as e:
        pass
