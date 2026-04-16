import requests
response=requests.get("https://jsonplaceholder.typicode.com/users")
print(response.status_code)
if response.status_code==200:
    # print(response.json())
    data=response.json()
    for user in data:
        print(f"{user['name']},Email:{user['email']}")
else:
    print("failed")