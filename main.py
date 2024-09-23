import requests
login_url = "https://prd.mhrs.gov.tr/api/vatandas/login"
payload = {
    "kullaniciAdi": "TC",
    "parola": "SIFRE",
    "islemKanali": "VATANDAS_WEB",
    "girisTipi": "PAROLA",
    "captchaKey": None
}
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://mhrs.gov.tr",
    "Referer": "https://mhrs.gov.tr/",
}
response = requests.post(login_url, json=payload, headers=headers)

if response.status_code == 200:
    print("Giriş başarılı!")
    print("Yanıt:", response.json())
else:
    print(f"Giriş başarısız! Durum kodu: {response.status_code}")
    print(response.text)
