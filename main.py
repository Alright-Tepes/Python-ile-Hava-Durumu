# Made by Erdem Galibov

import requests

api="a4ef8841202e4d6fcb33370bc9716185" # Normalde OpenWeather'dan kendi API'nizi oluşturmanız gerekiyor, şimdilik size kıyağım olsun ;)
sehir=input("Herhangi bir şehir seçiniz(Sadece Türkiye'nin illeri): ")

def havadurumu(api,sehir):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    tam_url = f"{base_url}q={sehir}&appid={api}&units=metric"

    cevap=requests.get(tam_url)
    data=cevap.json()
    
    if data["cod"] != "404":
        ana_veri = data["main"]
        sicaklik = ana_veri["temp"]
        nem = ana_veri["humidity"]
        hava_durumu = data["weather"][0]["description"]
    
        print(f"Şehir: {sehir}")
        print(f"Sıcaklık: {sicaklik}")
        print(f"Nem: {nem}")
        print(f"Hava Durumu: {hava_durumu}")
    else:
        print("Üzgünüz, böyle bir şehir bulunamadı ve ya API'de sorun çıktı. Eğer ")




havadurumu(api, sehir)
