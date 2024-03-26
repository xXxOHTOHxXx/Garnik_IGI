import numpy as np

def find_min_antidiagonal(matrix):
  """
  Функция для поиска наименьшего элемента на побочной диагонали.

  Args:
      matrix: Матрица NumPy.

  Returns:
      Наименьший элемент на побочной диагонали.
  """
  min_value = None
  n = matrix.shape[0]
  for i in range(n):
    j = n - i - 1
    if min_value is None or matrix[i, j] < min_value:
      min_value = matrix[i, j]
  return min_value

# Пример использования
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# min_value = find_min_antidiagonal(matrix)
# print(f"Наименьший элемент на побочной диагонали: {min_value}")
def calculate_dispersion_antidiagonal(matrix):
  """
  Функция для вычисления дисперсии элементов на побочной диагонали.

  Args:
      matrix: Матрица NumPy.

  Returns:
      Дисперсия элементов на побочной диагонали.
  """
  n = matrix.shape[0]
  antidiagonal = matrix[np.arange(n), np.arange(n, 0, -1)]
  return np.var(antidiagonal)

# Пример использования
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# dispersion = calculate_dispersion_antidiagonal(matrix)
# print(f"Дисперсия элементов на побочной диагонали: {dispersion:.2f}")

def calculate_dispersion_antidiagonal_formula(matrix):
  """
  Функция для вычисления дисперсии элементов на побочной диагонали
  через программирование формулы.

  Args:
      matrix: Матрица NumPy.

  Returns:
      Дисперсия элементов на побочной диагонали.
  """
  n = matrix.shape[0]
  antidiagonal = matrix[np.arange(n), np.arange(n, 0, -1)]
  mean = np.mean(antidiagonal)
  squared_differences = [(x - mean)**2 for x in antidiagonal]
  return np.sum(squared_differences) / (n - 1)

# Пример использования
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# dispersion = calculate_dispersion_antidiagonal_formula(matrix)
# print(f"Дисперсия элементов на побочной диагонали: {dispersion:.2f}")
