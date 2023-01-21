from random import randint

test_list = [randint(-101, 101) for _ in range(100)]
print(test_list)

zero_list = [x if x>=0 else 0 for x in test_list]
print(zero_list)
