import requests

question_data = []

parameters = {
       "amount":10,
       "category":18,
       "type":"boolean"
 
}

res = requests.get("https://opentdb.com/api.php" , params=parameters)
for obj in res.json()['results']:
  question_data.append(obj)       

print(question_data)


