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


class Resource:

    def __init__(self, name='', data=None, parent=None) -> None:
        self.name = name
        self.data = data
        self.children = []
        self.parent = parent
        # key: value = user: (boolean, timestamp) or a big integer; good thing about timestamp is we also know 'when'
        self.user_access = {}

    def _getTimestamp(self):
        dt = datetime.now()
        return datetime.timestamp(dt)

    def grant_access(self, user):
        ts = self._getTimestamp()
        self.user_access[user] = (True, ts)
        return True

    def revoke_access(self, user):
        ts = self._getTimestamp()
        self.user_access[user] = (False, ts)
        return True

    def has_access(self, user):
        latest_ts = 0
        latest_access_bool = False
        cur = self
        while cur != None:
            if user in cur.user_access:
                access_bool, ts = cur.user_access[user]
                if ts > latest_ts:
                    latest_ts = ts
                    latest_access_bool = access_bool
            cur = cur.parent
        return latest_access_bool
