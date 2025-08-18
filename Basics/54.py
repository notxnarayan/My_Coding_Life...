class Numbers:
    def __init__(self):
        self.nums = [10, 20, 30]
        self.alpha = ['a', 'b']

    def __iter__(self):
        return iter(self.alpha)  # returns list iterator

obj = Numbers()
it = iter(obj)
print(next(it))  # ✅ Works, prints 'a'

# for i in obj:
#     print(i)
