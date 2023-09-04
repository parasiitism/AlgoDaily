"""
for repository in self.repositories:
    try:
        packageFuture: Future[Package] = self.__getPackageFuture(respository, packageName)
        return packageFuture.result()
    except Exception:
        continue
    raise Exception("Package not found")
This was the original code. Calling result() is blocking. So instead of waiting for every repository to respond before trying the next repository, you append the packageFutures to a queue.
And then iterate and see there's any thats complete
you'd modify the code above to, instead of calling result() on packageFuture, you'd do queue.append(packageFuture)
You'd then iterate through the que and call result() on each of them.
"""
import time
from concurrent.futures import ThreadPoolExecutor, wait, as_completed


def worker(n):
    time.sleep(2)
    res = 2**n
    if n == 3:
        raise Exception("Package not found")
    print(f"worker at {n}")
    return res


# with ThreadPoolExecutor(2) as executor:
executor = ThreadPoolExecutor(2)
futures = []
for i in range(1, 10):
    f = executor.submit(worker, i)
    futures.append(f)

print('Waiting for tasks to complete...')
wait(futures)
print('All tasks are done!')

# note: the results are not in order
for f in as_completed(futures):
    try:
        result = f.result()
        print(result)
    except Exception as err:
        print(err)
