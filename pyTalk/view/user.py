import view.db as db

class user():
    def __init__(self,username,qq,client):
        self.username = username
        self.qq       = qq
        self.clientInfo = {}
        self.client = client
    def register(self):
        profile = self.username + "-" + self.qq
        if self.clientInfo.get(profile):
            return {
                "status":0,
                "info":"您注册的账号已经存在了"
            }

        #保存用户注册的信息
        model = db.Model()
        userid = model.table("user").save({
            "name":self.username,
            "qq":self.qq,
            "add_time":str(model.getTime()),
            "login_time":str(model.getTime()),
            "login_count":"1"
        })

        self.clientInfo[profile] = self.client
        if userid>=1:
            return {
                "status": 1,
                "info": "注册成功！您的账号是:%s" % (self.username)
            }


    def logout(self):
        print("退出了")
    def update(self):
        pass