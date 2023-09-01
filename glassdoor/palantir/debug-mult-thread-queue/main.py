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
