# from datetime import datetime
# from time import strptime

# d = "2022-09-25T07:00:00-0400"


# date_str = d[:10]


# date = strptime(date_str,'%Y-%m-%d')


# print(type(date.now()))


# split = lambda x, n: [x[:n]] + [split(x[-(len(x) - n) :] if -(len(x) - n) else [], n)][0] if x else x


# arr = list(range(13))
# print(split(arr,2))


from turtle import pensize


x = 57

res = "More" if 30 <= x >= 56 else "Nop"

print(res)