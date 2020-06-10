# web-request.py
import requests
import json
import statistics

print()
print("REQUESTING SOME DATA FROM THE INTERNET...")

# Requesting a Product:
request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
response = requests.get(request_url)
print(response.text)

# Requesting Products:
request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
response = requests.get(request_url)
parsed_response = json.loads(response.text)
for i in parsed_response:
    print(i["id"], i["name"])

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
response = requests.get(request_url)
parsed_response = json.loads(response.text)

student = parsed_response["students"]
grades = []
for i in student:
    grades.append(i["finalGrade"])
breakpoint()

Average = statistics.mean(grades)
Min = min(grades)
Max = max(grades)
print(f"Average score is {Average: .2f}")
print(f"Minimum score is {Min: .2f}")
print(f"Maximum score is {Max: .2f}")