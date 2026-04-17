"""
Autor: Kevin Uriarte
Fecha: 2026-04-16
Descripción:
Interfaz en Python para probar la librería ARM64.
Incluye benchmarking.
"""

import ctypes
import time
import random

lib = ctypes.CDLL("./build/libops.so")

# Configuración de tipos
lib.add.argtypes = [ctypes.c_long, ctypes.c_long]
lib.add.restype = ctypes.c_long

lib.sum_array.argtypes = [ctypes.POINTER(ctypes.c_long), ctypes.c_long]
lib.sum_array.restype = ctypes.c_long

# Datos de prueba
N = 100000
data = [random.randint(1,100) for _ in range(N)]
arr = (ctypes.c_long * N)(*data)

# ----------- PRUEBAS FUNCIONALES -----------
print("Add ASM:", lib.add(10,5))
print("Sum ASM:", lib.sum_array(arr, N))

# ----------- BENCHMARK -----------

def python_sum(arr):
    return sum(arr)

def c_sum(arr):
    return lib.sum_array(arr, N)

# Python
start = time.time()
python_sum(data)
py_time = time.time() - start

# ASM
start = time.time()
c_sum(arr)
asm_time = time.time() - start

print("\n--- RESULTADOS ---")
print("Python:", py_time)
print("ASM:", asm_time)
print("Speedup:", py_time / asm_time)
