def h():
  n1 = int(input("Введіть перше число: "))
  n2 = int(input("Введіть друге число: "))

  def f(a, b):
      while b != 0:
          a, b = b, a % b
      return a

  d = f(n1, n2)
  print("Найбільший спільний дільник:", d)

h()