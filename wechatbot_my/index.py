from wxpy import *

bot = Bot()


"""
bot.self.add()
bot.self.accept()

bot.self.send("给我自己发条消息")

#myself = bot.self

#bot.file_helper.send("hello");

#myself.add()
#myself.accept()

# 进入 Python 命令行、让程序保持运行
#embed()

print(bot.friends())
print(bot.groups())
print(bot.mps())
print(bot.chats())
friend = bot.friends().search('小胡')
print(friend)

friend_one = ensure_one(friend)
print(bot.groups())
group = bot.groups().search('微信社群管理工具')
print(group)
groups = bot.groups().search('微信社群管理工具')
print(groups)

group1 = groups[0]
print(group1.search(pro))

user_or_users='小迷妹'
print(Bot.user_details(user_or_users, chunk_size=50))
print(bot.upload_file("index.html"))
print(bot.user_details('小迷妹'))
"""

friend = bot.friends().search('小胡')[0]

friend.send("hello")
friend.send_msg("3cai.png")