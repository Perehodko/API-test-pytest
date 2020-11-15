import requests

title_d = {}

for number in range(1, 25):
    r = requests.get("https://jsonplaceholder.typicode.com/posts/"+str(number))
    title_d[number] = r.json()["title"]
    # print(r.status_code, r.json()["title"])
print(title_d)