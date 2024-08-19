_id, _lv = input().split()

class User:
    def __init__(self, _id = "codetree", _lv = "10"):
        self.user_id = _id
        self.user_lv = _lv


user1 = User()
print(f"user {user1.user_id} lv {user1.user_lv}")

user1.user_id = _id
user1.user_lv = _lv
print(f"user {user1.user_id} lv {user1.user_lv}")