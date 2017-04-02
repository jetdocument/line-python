import requests,json
from urlparse import urlparse
import urllib

LINE_ACCESS_TOKEN="dNgrSoWFrJmMwMlYuV3kH1ZwpwstHqaYCsX4fOz4Yx1"
url = "https://notify-api.line.me/api/notify"

message ="ทดสอบ สวัสดีชาวโลก" # ข้อความที่ต้องการส่ง
msg = urllib.urlencode(({"message":message}))
LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
session = requests.Session()
a=session.post(url, headers=LINE_HEADERS, data=msg)
print(a.text)