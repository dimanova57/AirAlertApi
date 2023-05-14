region_dict = {
    "Волинська": "Lutsk",
    "Рівненська": "Rivne",
    "Житомирська": "Jitom",
    "Київська": "Kiiv",
    "Чернігівська": "Chernigiv",
    "Сумська": "Sumy",
    "Львівська": "Lviv",
    "Тернопільська": "Ternop",
    "Хмельницька": "Hmel",
    "Вінницька": "Vinn",
    "Черкаська": "Cherkasy",
    "Полтавська": "Poltava",
    "Харківська": "Harkiv",
    "Луганська": "Lugansk",
    "Закарпатська": "Ujgorod",
    "Івано-Франківська": "IvanFr",
    "Чернівецька": "Chernivci",
    "Кіровоградська": "Kirov",
    "Дніпропетровська": "Dnepr",
    "Донецька": "Donetsk",
    "Одеська": "Odesa",
    "Миколаївська": "Mykolaiv",
    "Херсонська": "Herson",
    "Запорізька": "Zapor",
    "Автономна Республіка Крим": "Simfer"
}

setInterval(() => {
  fetch('http://localhost:5000/all')
    .then(response => response.json())
    .then(data => {
      console.log(data)
      // Loop through the regions and change the color property of the corresponding XML tag
      Object.entries(data).forEach(([region, value]) => {
        const element = document.getElementById(region_dict[region]);
        if (element) {
          console.log(element)
          element.children[0].style.fill = value ? "#DC4758": "#8FCEEE"
        }
      });
    })
    .catch(error => console.error(error));
  }, 15000);