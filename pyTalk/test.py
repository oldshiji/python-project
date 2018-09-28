import view.profile


o = view.profile.profile
logout = hasattr(view.profile.profile,'logout')
print(logout)
u = view.profile.profile
logout = getattr(u,'logout')
print(logout(u))


a = {"a":1,"b":2}
print(a)
del a['a']
print(a)