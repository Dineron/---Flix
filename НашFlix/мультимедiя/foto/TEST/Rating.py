import json
Js = """
[
	{
		"Фалаут":{
			"Оцінка": 10
		},
		"Сімпсони":{
			"Оцінка": 9
		}
	}
]"""


items = json.loads(Js)
