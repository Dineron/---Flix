import json
FileR="""
[
	{
		"Avengers Infinity War":{
			"Description": "Не знаючий страху і поразки могутній титан Танос завдяки двом Каменям вічності став наймогутнішою істотою у Всесвіті. Він захоплює планети, після чого знищує їх мешканців. Однак його основне завдання — роздобути інші Камені вічності. Оскільки це артефакти колосальної сили, з їх допомогою Танос зможе в одну секунду знищувати цілі світи. У Месників немає права на помилку: від трагедії вселенського масштабу їх відділяє одне клацання пальців. Месники разом зі своїми союзниками у що б то не стало повинні зупинити Таноса.",
			"Mark": 8.4
		},
		"Fallout":{
			"Description":"“Фолаут” розповідає історію, що відбувається в постапокаліптичному світі, де цивілізація була знищена після ядерної війни. Головний герой, який вижив після ядерної катастрофи, вирушає в небезпечну подорож через спустошені землі, стикаючись із мутантами, радіоактивним забрудненням та іншими небезпеками.",
			"Mark": "Серіал ще не випущений"
		},
		"It":{
			"Description":"Для школяра на ім’я Біллі літо 1989-го року починається зовсім погано - його молодший брат, який пішов в дощ запускати кораблики безслідно зник. Для містечка, де живе Білл, зникнення людей, звичайна справа, але підліток не збирається опускати руки, навіть коли припиняють пошуки. Разом з друзями він продовжує шукати брата в каналізаційній системі, куди хлопчика, судячи з усього, змило потоками води. Пошуки приводять шибеників до висновку, що всьому виною стародавнє і могутнє зло, яке втілює найгірші кошмари своїх жертв і мешкає в водостоках під містом…",
			"Mark": 7.3
		},
		"The Lord of the Rings The Return of the King":{
			"Description":"Фродо продовжує свою вкрай небезпечну мандрівку, а його друзі, спадкоємець гондорского трону Арагорн з ельфом Леголасом, гномом Гімлі та чарівником Гендальфом, намагаються врятувати старовинну твердиню, місто Мінас-Тіріт. В цьому їм допомагають хоббіти Меррі та Піппін, король Рохана Теоден та його відважна племінниця…",
			"Mark": 9.0
		},
		"Programmers":{
			"Description":"У світі, де кодери стали новими героями, група талановитих програмістів об'єднується, щоб врятувати світ від катастрофи, спричиненої небезпечним хакерським альянсом. Ця команда з різних куточків світу використовує свої навички в програмуванні, щоб розкрити інтриги, розгадати головоломки і зупинити атаку на глобальних рівнях. ",
			"Mark": "Фільм у стадії розробки"
		},
		"Ghost Rider Spirit of Vengeance":{
			"Description": "байкер-каскадер Джонні Блейз, що вночі перетворюється на пекельного гонщика, відправляється до Східної Європи де намагається позбутись прокляття та розірвати угоду з дияволом. Але натомість він потрапляє в середовище релігійних фанатиків, які разом зі священником намагаються врятувати душу юного хлопця від демонів з пекла...",
			"Mark": 4.3
		},
		"Wendnesday":{
			"Description":"Венздей — старша дочка ексцентричної родини Аддамс, яка через свої шокуючі витівки поміняла вісім шкіл за п'ять років. Після чергового скандального інциденту вона змушена перевестися до «Невермора» — академії для ізгоїв, яку колись відвідували її батьки. Навчальним закладом залізною хваткою керує Ларисса Вімс — заклятий ворог її матері Мортіші. У «Неверморі» дівчинка розвиває свої екстрасенсорні здібності, що нещодавно відкрилися, і береться зупинити монстра, який полює на людей в окрузі...",
			"Mark": 8.1
		},
		"World War Z":{
			"Description":"У центрі сюжету виявляється чоловік на ім'я Джеррі Лейн, життя якого в один прекрасний день кардинальним чином змінюється. Справа в тому, що головний герой разом зі своєю сім'єю виявився несподівано в самому епіцентрі жахливого і страшного вірусу, який стрімким чином поширювався. Виявилося, що через вірус люди всі стали перетворюватися на кровожерних і жорстоких монстрів. Але не тільки їх місто виявилося охопленим жахливою хворобою, в усьому світі панував жахливий вірус. Тепер мета Джеррі будь-якою ціною врятувати свою сім'ю...",
			"Mark": 7.0
		}
	}
]"""

data = json.loads(FileR)