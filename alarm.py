import requests
import datetime

webhook_url = ""
members = ["Aさん", "Bさん", "Cさん", "Dさん","Eさん","Qiaoさん"]
start_date = datetime.date(2025, 7, 7)  

today = datetime.date.today()
weeks_since_start = (today - start_date).days // 7
current_member = members[weeks_since_start % len(members)]
message = f"今週の掃除当番は⭐ *_{current_member}_* ⭐です！お願いしますね！"

payload = {"text": message}
res = requests.post(webhook_url, json=payload)

print("Status:", res.status_code)
print("Response:", res.text)