# get_data.py

print("REQUESTING SOME DATA FROM THE INTERNET...")

# Write a Python program which issues a GET request for this product.json data, then prints the product's "name".

import requests
import json

request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
response = requests.get(request_url)
# print(response.status_code)
parsed_response = json.loads(response.text)
print(parsed_response["name"])
# print(type(parsed_response["name"]))

# Write a Python program which issues a GET request for this products.json data, then loop through each product and print its "name" and "id" attributes.
request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
response = requests.get(request_url)
# print(response.status_code)
parsed_response2 = json.loads(response.text)
for p in parsed_response2:
    print(p["id"], p["name"])
# print(type(parsed_response["name"]))


# Write a Python program which issues a GET request for this gradebook.json data, then calculate and print the average, min, and max grades.
request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
response = requests.get(request_url)
#print(response.status_code)
parsed_response3 = json.loads(response.text)
#print(parsed_response3)
grades = []
students = parsed_response3["students"]
for x in students:
    grades.append(x["finalGrade"])

print(min(grades))
print(max(grades))

average = sum(grades) / len(grades)
print(average)