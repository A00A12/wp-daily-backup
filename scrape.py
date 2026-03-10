import requests
import os
import time

# 🎯 需要备份的网页清单
PAGES_TO_BACKUP = {
    "homepage.html": "https://pt5china.com/",
}

def main():
    # 伪装成正常的电脑浏览器访问网站
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    
    # 创建 backups 文件夹
    backup_dir = "backups"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # 循环抓取清单里的页面
    for filename, url in PAGES_TO_BACKUP.items():
        print(f"正在抓取: {filename} <- {url}")
        try:
            # 发起请求
            response = requests.get(url, headers=headers)
            response.raise_for_status() 
            
            # 存入 backups 文件夹
            filepath = os.path.join(backup_dir, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(response.text)
                
            print(f"✅ 成功! 保存为 {filepath}")
            time.sleep(2) 
            
        except Exception as e:
            print(f"❌ 抓取失败 {filename}: {e}")

if __name__ == "__main__":
    main()

