import requests
import json
import cevir

sehir = input("Şehri giriniz: ")
sehirD = (sehir[0:1].replace("i","İ")+sehir[1:]).capitalize()

api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+sehir+"&appid=24bb5a00705b2420901490c95519ab0b")



result = json.loads(api_request.content)

hava_sozlu = {
    "Clouds" : "bulutlu",
    "Misty"  : "sisli",
    "Clear"  : "açık",
    "Rain"   : "yağmurlu"
}

print(sehirD + " sıcaklığı {} K".format(result["main"]["temp"]))
print(sehirD + " sıcaklığı {} C".format(round(cevir.kelvin_to_celcius(result["main"]["temp"]),2)))
print(sehirD + " sıcaklığı {} F".format(round(cevir.celcius_to_fahrenheit(cevir.kelvin_to_celcius(result["main"]["temp"])),2)))

print(sehirD + " havası",hava_sozlu[result["weather"][0]["main"]])
