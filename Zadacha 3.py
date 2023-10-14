def solve_quadratic(a, b, c):
  """
  Решава квадратно уравнение от вида ax^2 + bx + c = 0.

  Args:
    a: Коефициентът при квадрата.
    b: Коефициентът при линейната част.
    c: Постоянният член.

  Returns:
    Двете корена на уравнението.
  """

  delta = b ** 2 - 4 * a * c
  if delta < 0:
    return None
  elif delta == 0:
    return (-b / (2 * a))
  else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2


def main():
  """
  Точка на влизане в програмата.
  """

  a, b, c = float(input("Въведете коефициентите a, b, c: ")), float(input()), float(input())
  roots = solve_quadratic(a, b, c)
  if roots is None:
    print("Уравнението няма реални корени.")
  else:
    print(f"Корените на уравнението са {roots[0]}, {roots[1]}.")


if __name__ == "__main__":
  main()