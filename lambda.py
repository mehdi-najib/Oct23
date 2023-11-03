# def add(a, b):
  #  return a+b
#print(add(10, 2))

add = lambda a,b: a + b
print(add(2, 6))


names = ['a', 'abc', 'ab', 'asewe']
n_sort = sorted(names, key= lambda x: len(x))
print(list(n_sort))