import os
import tarfile as tar
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

content = MIMEMultipart()  #建立MIMEMultipart物件
content["subject"] = "Mail title"  #郵件標題
content["from"] = "xxxx@gmail.com"  #寄件者
content["to"] = "xxxx@gmail.com" #收件者

# 壓縮log檔案
tar = tar.open("file name", "w:gz")
for root,dir,files in os.walk("/var/log"):
    for file in files:
        if "secure" in file:
            fullpath = os.path.join(root,file)
            tar.add(fullpath)
tar.close()

# 文字內容
content.attach(MIMEText("hdfs-overcomer.ddns.net secure log files."))  #郵件內容

# 附加檔案
att = MIMEText(open('compress file name', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="compress file name"'

content.attach(att)  #郵件內容

import smtplib

with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login("xxxxx@gmail.com", "gmail app key")  # 登入寄件者gmail
        smtp.send_message(content)  # 寄送郵件
        smtp.quit()
        print("[INFO] Complete!")
    except Exception as e:
        print("[ERROR] Error message: ", e)