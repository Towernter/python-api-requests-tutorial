import requests
import json


def get_joke():
	api_end_point = "https://official-joke-api.appspot.com/jokes/random"
	joke = requests.get(api_end_point)
	json_data = json.loads(joke.text)	
	joke_id = json_data["id"]
	joke_type = json_data["type"]
	joke_setup = json_data["setup"]
	joke_punchline = json_data["punchline"]
	print(joke_id)
	print(joke_type)
	print(joke_setup)
	print(joke_punchline)


def get_joke_by_category(category):
	api_end_point = "https://official-joke-api.appspot.com/jokes/"+category+"/random"
	joke = requests.get(api_end_point)
	json_data = json.loads(joke.text)
	joke_setup = json_data[0]["setup"]
	joke_punchline = json_data[0]["punchline"]
	print(joke_setup)
	print(joke_punchline)
	

if __name__ == "__main__":
	get_joke_by_category("programming")
	#get_joke

	
