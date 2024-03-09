import FindWay

findway = FindWay.auth(id=10, token='vQo2mk855e9CsRQRdDTtAw')

"""чекаем нашу библиотеку"""

post = {
    
  "discribe": "ооооооооооооооооооооооооооооооооооооооооооооооооооочень длиииииииииииииииииииииииииииииииииииииииинный поооооооооооооооооооооооооооооооост",
  "image": "fwwdqwdqw qwd qwd",
  "title": "Тестовый пост"

}
print(findway.user.edit_post(0, post))