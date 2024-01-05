# Написать класс Twitter, в котором есть следующие методы:
# 1) __init__(self), который инициализирует класс
# 2) post_tweet(self, user_id, tweet_id), который создает новый твит с идентификатором tweet_Id по идентификатору пользователя user_id. Каждый вызов этой функции будет осуществляться с уникальным идентификатором твита. Желательно, чтобы впоследствии твиты можно было бы быстро получить по user_id.
# 3) get_news_feed(self, user_id), который получает 10 последних идентификаторов твитов в ленте новостей пользователя. Каждый элемент в ленте новостей должен быть опубликован пользователями, на которых подписан пользователь. Твиты должны быть упорядочены от самого позднего до самого раннего. Подумайте, как организовать упорядочивание твитов по времени:
# возможно для этого лучше записывать в структуру данных с твитами
# информацию о твите (то есть tweet_id)
# какое то число, отвечающее за время (например какой нибудь счетчик)
# и это например завернуть в кортеж

# 4) follow(self, follower_id, followee_id), в котором пользователь с идентификатором follower_id подписался на пользователя с идентификатором followee_id. Желательно, чтобы впоследствии подписки можно было бы быстро получить по follower_id.
# %) unfollow(self, follower_id, followee_id), в котором пользователь с идентификатором follower_id отписался от пользователя с идентификатором followee_id.
from typing import List
from collections import defaultdict, deque

class Twitter:
    def __init__(self):
        self.tweets = defaultdict(deque)
        self.followers = defaultdict(set)

        # счетчик времени для твитов
        self.time = 0

    def post_tweet(self, user_id, tweet_id):
        self.tweets[user_id].appendleft((tweet_id, self.time)) #добавляем новые твиты в начало
        self.time += 1

    def get_news_feed(self, user_id) -> List[int]:
        # получаем все твиты пользователей, на которых подписаны
        users = self.followers[user_id]
        tweets = []
        for user in users:
            tweets.extend(list(self.tweets[user]))

            # Сортируем твиты по времени и выбираем последние 10
        tweets.sort(key=lambda x: x[1], reverse=True)
        return [tweet[0] for tweet in tweets[:10]]


    def follow(self, follower_id, followee_id):
        self.followers[follower_id].add(followee_id)
    def unfollow(self, follower_id, followee_id):
        if followee_id in self.followers[follower_id]:
            self.followers[follower_id].remove(followee_id)


code = []
while data:= input():
    code.append(data)
code = "\n".join(code)
exec(code)
