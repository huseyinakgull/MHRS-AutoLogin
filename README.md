# MHRS API Giriş Scripti

Bu proje, MHRS (Merkezi Hekim Randevu Sistemi) API'sine POST isteği göndererek kullanıcı girişini gerçekleştiren basit bir Python scriptidir. Kullanıcı adı (TC kimlik numarası) ve parola ile giriş yaparak başarılı veya başarısız sonuçları döndürür.

## İçindekiler
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)

## Kurulum

Projenin çalıştırılabilmesi için `requests` kütüphanesinin kurulu olması gerekmektedir. Eğer kurulu değilse, aşağıdaki komut ile yükleyebilirsiniz:

```bash
pip install requests
```
## Kullanım

1. Scripti bir Python dosyasına kaydedin. Örnek olarak, dosya adını mhrs_login.py olarak belirleyebilirsiniz.
2. kullaniciAdi ve parola alanlarını kendi MHRS bilgilerinize göre düzenleyin.
3. Python dosyasını aşağıdaki komut ile çalıştırın:

```bash
python mhrs_login.py
```
Eğer giriş başarılı olursa, JSON formatında bir yanıt alacaksınız. Aksi takdirde, giriş başarısız olduğuna dair bir mesaj ve durum kodu gösterilecektir.
