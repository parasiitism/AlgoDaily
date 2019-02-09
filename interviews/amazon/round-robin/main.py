"""
    Round Robin Scheduling
    - https://www.youtube.com/watch?v=aWlQYllBZDs
    - https://wdxtub.com/interview/14520850399861.html

    Detail:
    - each task has one arrival time and one execution time, arrivals & executions are paired up already in a correct order for you
    - the input arrival times are sorted
    - return the average waiting time for each task

    Caution:
    - cant use priority queue, because if one item's arrival time is the same is another one item's remain, priority might mess up
"""


def roundRobin1(arrivals, executions, quantum):
    """
        1st approach
        - use a queue
        - put the first item first
    """
    if len(arrivals) == 0 or len(executions) == 0 or len(arrivals) != len(executions) or quantum == 0:
        return 0
    q = []
    curTime = 0
    totalWait = 0
    # put the first item in the queue
    q.append((arrivals[0], executions[0]))
    i = 1
    # process the queue
    while len(q) > 0:
        # pop the item from the queue with minimum arr
        arr, exc = q.pop(0)
        # if the item arr > curTime, update the cur time
        if arr > curTime:
            curTime = arr
        # current time - arr is the waiting time of this item
        totalWait += curTime - arr
        # task got done, update the current time
        curTime += min(quantum, exc)
        # put the tasks to the queue which the arrival time <= current time
        while i < len(arrivals) and arrivals[i] <= curTime:
            q.append((arrivals[i], executions[i]))
            i += 1
        # determin if we need to execute this item in the next round
        remain = exc-quantum
        if remain > 0:
            q.append((curTime, remain))

    return totalWait, float(totalWait)/len(arrivals)


def roundRobin2(arrivals, executions, quantum):
    """
        2nd approach
        - use a queue
        - put the items in the loop
    """
    if len(arrivals) == 0 or len(executions) == 0 or len(arrivals) != len(executions) or quantum == 0:
        return 0
    q = []
    curTime = 0
    totalWait = 0
    i = 0
    # process the queue
    while len(q) > 0 or i < len(arrivals):
        if len(q) > 0:
            # pop the item from the queue with minimum arr
            arr, exc = q.pop(0)
            # current time - arr is the waiting time of this item
            totalWait += curTime - arr
            # task got done, update the current time
            curTime += min(quantum, exc)
            # put the tasks to the queue which the arrival time < current time
            while i < len(arrivals) and arrivals[i] <= curTime:
                q.append((arrivals[i], executions[i]))
                i += 1
            # determin if we need to execute this item in the next round
            remain = exc-quantum
            if remain > 0:
                q.append((curTime, remain))
        else:
            # if nothing in the queue and there are still some tasks, put the first task in the queue
            # and update the curTime such that we can execute it in the next iteration
            q.append((arrivals[i], executions[i]))
            curTime = arrivals[i]
            i += 1

    return totalWait, float(totalWait)/len(arrivals)


# 6.4
print(roundRobin2([0, 1, 3, 5, 6], [5, 3, 6, 1, 4], 3))
# 8.5
print(roundRobin2([0, 1, 2, 3], [5, 3, 8, 6], 3))
# 2.3333333
print(roundRobin2([0, 1, 4], [5, 2, 3], 3))

# start from 1s, 7.2
print(roundRobin2([1, 1, 3, 5, 6], [5, 3, 6, 1, 4], 3))
