class User:
    def __init__(self, username, fullname, email) -> None:
        self.username = username
        self.fullname = fullname
        self.email = email

    def __repr__(self) -> str:
        return "User - username: {}, fullname: {}, email: {}".format(self.username, self.fullname, self.email)

    def __str__(self) -> str:
        return self.__repr__()


class Database:
    def __init__(self) -> None:
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            else:
                i += 1
        self.users.insert(i, user)

    def find(self, username):
        for i in range(len(self.users)):
            if self.users[i].username == username:
                return self.users[i]

    def update(self, user):
        for i in range(len(self.users)):
            target = self.find(user.username)
            target.fullname, target.email = user.fullname, user.email

    def list_all(self):
        return self.users


ikayh = User("ikayh", "Ikechukwu Ejiofor", "Ikechukwu1998@gmail.com")
uju = User("uju", "Uju Ejiofor", "Uju@gmail.com")
nneka = User("nneka", "Nneka Ejiofor", "Nneka@gmail.com")

db = Database()
db.insert(ikayh)
db.insert(uju)
db.insert(nneka)
db.update(User("ikayh", "Ikechukwu Money", "I@gmail.com"))
# db.insert()

# print(db.find("ikayh"))


# word break
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        """
        memo = {leetcode: , code: leet:T  }
        currs = lo
        lo
         ^
        """
        wordSet = set(wordDict)
        memo = {}
        return self.dfs(s, memo, wordSet)

    def dfs(self, s, memo, wordSet):
        if s in memo:
            return memo[s]
        if not s:
            return True
        for i in range(len(s)):
            prefix = s[:i+1]
            suffix = s[i+1:]

            if prefix in wordSet:
                memo[s] = self.dfs(suffix, memo, wordSet)
                if memo[s]:
                    return True
        return False


s = [1, 3, 2, 3, 4]
for i in range(len(s)-1, -1, -1):
    if s[i] == 3:
        s.pop(i)
        break
print(s)
