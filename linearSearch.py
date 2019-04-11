import timeit
start_time = timeit.default_timer()

def linear_search(lst, target):
    for i, value in enumerate(lst):
        if value == target:
            # found it!
            return i
    
    # if the loop ends, target was not found
    return -1

ls = [1,2,3,4,5,6,7,8,9]

print(linear_search(ls,5))
elapsed = timeit.default_timer() - start_time
print(elapsed)
