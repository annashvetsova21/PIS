import requests
s_city = "London" #назва міста
appid = "59dc6dad483ce59e72e782f5441009bb" #Api key
#запит погоди по назві міста
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'q': s_city, 'units': 'metric', 'lang': 'ua', 'APPID': appid})
    #отримуємо результати у форматі json
    data = res.json()
    #виводимо дані на екран
    print(data['name'],"Поточна дата 23.05.2024", "Довгота:", data['coord']['lon'], "Широта:",data['coord']['lat'])
    print("Умови:", data['weather'][0]['description'])
    print("Температура:", data['main']['temp'],"градуси по Цельсію")
    print("Відчувається як:", data['main']['feels_like'], "градуси по Цельсію")
    print("Вітер:", data['wind']['speed'], "м/с")
except Exception as e:
    print("Exception (weather):", e)
    pass
