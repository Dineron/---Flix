import json
from Rating import items
from Rating import Js
import Rating

from MovieInfo import FileR
from MovieInfo import data

print(items[0], end = "\n")

ite = json.loads(Js)

print(ite[0]['Фалаут']["Оцінка"], end = "\n")

imp = json.loads(Rating.Js)

print(imp[0]["Сімпсони"]["Оцінка"], end = "\n")

MovieInfo = f"C:/Users/roma_/OneDrive/Рабочий стол/НашFlix/мультимедiя/foto/DataBase/MovieInfo.json"

print("Опис:", data[0]["Fallout"]["Description"], "\nОцінка:", data[0]["Fallout"]["Mark"])

import tkinter as tk

root = tk.Tk()

# Створення Text віджету
text_widget = tk.Text(root, wrap="word")
text_widget.pack(expand=True, fill="both")

# Додавання довгого тексту
long_text = "краї́на (МФА: [ʊkrɐˈjɪn̪ɐ] ( прослухати)) — держава, розташована у Східній та частково у Центральній Європі, охоплює південний захід Східноєвропейської рівнини, частину Східних Карпат і Кримські гори. Межує з Румунією і Молдовою на південному заході, з Угорщиною, Словаччиною та Польщею на заході, з Білоруссю на півночі та з Росією на сході й північному сході. На півдні омивається Чорним та Азовським морями. Площа становить 603 700 км²[7]. Найбільша за площею країна серед повністю розташованих у Європі[8].\n\nСтаном на останній перепис (2001), населення України становило 48,4 мільйона осіб[9]. Основне й корінне населення України — це українці[10][11] (77,8 % населення на 2001 рік[9]). Також офіційно корінними народами України є кримські татари, караїми та кримчаки[12]. Крім того, значною меншиною є росіяни (17,3 % населення на 2001 рік[9]). Історично однією з найбільших меншин в Україні були також українські євреї.[13]"

text_widget.insert("1.0", long_text)
text_widget.config(state="disabled")

root.mainloop()
