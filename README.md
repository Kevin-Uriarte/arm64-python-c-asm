# Proyecto ARM64 + Python + C + ASM

## Autor
Kevin Uriarte

## Fecha
2026-04-16

## Descripción
Este proyecto implementa una librería de alto rendimiento en ARM64 Assembly,
integrada con C y accesible desde Python mediante ctypes.

Incluye operaciones básicas:
- Suma
- Resta
- Multiplicación
- Máximo y mínimo
- Suma de arreglo
- Conteo de pares
- Producto punto

## Estructura
- app.py → pruebas en Python
- bridge.c → interfaz C
- ops.s → funciones en Assembly ARM64
- Makefile → compilación
- build/ → librería compartida (.so)

## Compilación
```bash
make
