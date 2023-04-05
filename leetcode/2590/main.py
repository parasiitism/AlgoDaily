"""
    hashtables + hashset

    Time
    - addTask           O(tag)
    - getAllTasks       O(NlogN) N: number of tasks per user
    - getTasksForTag    O(NlogN)
    - completeTask      O(1)
"""


class TodoList:

    def __init__(self):
        self.tasks = defaultdict(tuple)
        self.user2ids = defaultdict(set)
        self.tag2ids = defaultdict(set)
        self.completeds = set()

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        task_ID = len(self.tasks)+1
        self.tasks[task_ID] = (taskDescription, dueDate)
        self.user2ids[userId].add(task_ID)
        for tag in tags:
            self.tag2ids[tag].add(task_ID)
        return task_ID

    def getAllTasks(self, userId: int) -> List[str]:
        A = self.user2ids[userId]
        res = []
        for tid in A:
            task_date = self.tasks[tid]
            if tid not in self.completeds:
                res.append(task_date)
        res.sort(key=lambda x: x[1])
        return [x[0] for x in res]

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        A = self.user2ids[userId]
        res = []
        for tid in A:
            task_date = self.tasks[tid]
            if tid not in self.completeds and tid in self.tag2ids[tag]:
                res.append(task_date)
        res.sort(key=lambda x: x[1])
        return [x[0] for x in res]

    def completeTask(self, userId: int, taskId: int) -> None:
        if taskId not in self.user2ids[userId]:
            return
        self.completeds.add(taskId)


# Your TodoList object will be instantiated and called as such:
# obj = TodoList()
# param_1 = obj.addTask(userId,taskDescription,dueDate,tags)
# param_2 = obj.getAllTasks(userId)
# param_3 = obj.getTasksForTag(userId,tag)
# obj.completeTask(userId,taskId)
