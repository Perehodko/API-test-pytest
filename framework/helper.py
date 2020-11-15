import requests


def get_title(num: int):
    title_d = {}
    for number in range(1, num):
        r = requests.get("https://jsonplaceholder.typicode.com/posts/" + str(number))
        title_d[number] = r.json()["title"]
        title_d[7], title_d[8] = "another title7", "another title8"
    return sorted(title_d.items())

# [(1, 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'), (2, 'qui est esse'),
#  (3, 'ea molestias quasi exercitationem repellat qui ipsa sit aut'), (4, 'eum et est occaecati'),
#  (5, 'nesciunt quas odio'), (6, 'dolorem eum magni eos aperiam quia'), (7, 'another title7'), (8, 'another title8')]
