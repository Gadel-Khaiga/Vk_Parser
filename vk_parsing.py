import requests
import csv


dom = input()

def vk():
    token = 'ваш токен'
    version = 5.131
    domain = dom
    global all_posts
    all_posts = []
    response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'domain': domain,
                                'count': 100
                            }
                            )

    data = response.json()['response']['items']
    all_posts.extend(data)
    return all_posts
all_posts = vk()
def file_writer(all_posts):
    with open('kzngo.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('likes', 'body', 'url'))
        for post in all_posts:
            try:
                if post['attachments'][0]['type']:
                    img = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                pass
            a_pen.writerow((post['likes']['count'], post['text']))
file_writer(all_posts)
