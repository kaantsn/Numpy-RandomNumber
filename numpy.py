import numpy as np

# 0 ile 1 arasında rastgele ondalık sayı üretme
random_float = np.random.random()
print("Rastgele ondalık sayı:", random_float)

# Belirli bir aralıkta rastgele ondalık sayı üretme
random_float_range = np.random.uniform(1.0, 5.0)  # 1.0 ile 5.0 arasında rastgele bir sayı üretir
print("1.0 ile 5.0 arasında rastgele ondalık sayı:", random_float_range)

# Belirli bir aralıkta rastgele tam sayı üretme
random_integer = np.random.randint(1, 10)  # 1 ile 10 arasında rastgele bir tam sayı üretir
print("1 ile 10 arasında rastgele tam sayı:", random_integer)

# Belli bir şekle sahip rastgele sayılar üretme
random_array = np.random.random((3, 3))  # 3x3 boyutunda rastgele bir dizi üretir
print("Rastgele dizi:\n", random_array)
