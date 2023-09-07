from datetime import datetime

"""
    Given a tree like data structure. Each node is a resource.
    
    A class Resource has fields: name, parent, and children

    You're going to implement the methods below for checking user access over the resource
    - grant_access():
    - revoke_access():
    - has_access():

    When you grant user access to a resource, you're also granting the user access to all resources under it. Same goes for revoke.
"""

"""
    1st approach:
    - put a hashtable into every resource node
    e.g. self.user_access = {} # {user: timestamp}
"""

"""
    2nd approach: a global cache table and use an integer to count the operations
    e.g. user_access_per_node = { node: { user: int } }
    - we can wrap the counte in a class, so make sure that only it wont be modified by the others
    
    Note: integer to simulate timestamp but to avoid the situation where >=2 requests coming at the same timestamp
"""

user_access_per_node = {}


class ResourceAccess:
    def __init__(self) -> None:
        self.__ops_count = 0
        self.user_access_per_node = {}

    def getOpsCount(self):
        self.__ops_count += 1
        return self.__ops_count


ra = ResourceAccess()
# print(ra.__ops_count) # Attempting to access the private variable directly (This will generate an AttributeError)


class Resource:

    def __init__(self, name='', data=None, parent=None) -> None:
        self.name = name
        self.data = data
        self.children = []
        self.parent = parent
        # 1st approach: hash table within every node
        # key: value = user: (boolean, timestamp) or a big integer; good thing about timestamp is we also know 'when'
        # self.user_access = {}

    # def _getTimestamp(self):
    #     dt = datetime.now()
    #     return datetime.timestamp(dt)

    def grant_access(self, user):
        # ts = self._getTimestamp()
        # self.user_access[user] = (True, ts)

        if self not in ra.user_access_per_node:
            ra.user_access_per_node[self] = {}
        ra.user_access_per_node[self][user] = (True, ra.getOpsCount())

        return True

    def revoke_access(self, user):
        # ts = self._getTimestamp()
        # self.user_access[user] = (False, ts)

        if self not in ra.user_access_per_node:
            ra.user_access_per_node[self] = {}
        ra.user_access_per_node[self][user] = (False, ra.getOpsCount())

        return True

    def has_access(self, user):
        latest_ops_cnt = 0
        latest_access_bool = False
        cur = self
        while cur != None:
            # if user in cur.user_access:
            #     access_bool, ts = cur.user_access[user]
            #     if ts > latest_ts:
            #         latest_ts = ts
            #         latest_access_bool = access_bool
            if cur in ra.user_access_per_node and user in ra.user_access_per_node[cur]:
                access_bool, ops_cnt = ra.user_access_per_node[cur][user]
                if ops_cnt > latest_ops_cnt:
                    latest_ops_cnt = ops_cnt
                    latest_access_bool = access_bool
            cur = cur.parent
        return latest_access_bool
