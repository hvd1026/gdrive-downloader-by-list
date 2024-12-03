import gdown
from time import sleep
import os
try:
    os.remove('fail.txt')
except:
    pass

def read_urls(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
    urls = [url.strip() for url in urls]  
    return urls

if __name__ == "__main__":
    file_path = 'list.txt'  
    sleep_time = int(input("Sleep time: "))
    print()
    proxy = input("Proxy?: ").strip()
    urls = read_urls(file_path)
    for url in urls:
        try:
            if (proxy == ''):
                gdown.download_folder(url=url, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36", quiet=True)
            else:
                gdown.download_folder(url=url, proxy=proxy, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36", quiet=True)
            print(f"Success: {url}")
        except Exception as e:
            print(f"Failed: {url}", e)
            fail = open('fail.txt', 'a')
            fail.write(url + '\n')
            fail.close()
        sleep(sleep_time)