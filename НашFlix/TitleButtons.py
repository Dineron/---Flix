import json
FileR="""
[
	{
		"0":{
			"Name": "Film",
			"Selected": 0,
			"CWidth": 60
		},
		"1":{
			"Name": "Cartoon",
			"Selected": 0,
			"CWidth": 85
		},
		"2":{
			"Name": "Serial",
			"Selected": 0,
			"CWidth": 50
		},
		"S":{
			"Text": "Виберiть a category..."
		}
	}
]"""

ButtonsData = json.loads(FileR)