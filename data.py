import requests

parameters = {
    "amount": 10,  #10 questions
    "type": "boolean",  #True or False questions only
}
response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean", params=parameters)
question_data = response.json()['results'] #loads the results into question_data