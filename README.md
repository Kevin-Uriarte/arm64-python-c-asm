# Proyecto: Integración Python + C + ARM64 Assembly

## Autor

Kevin Ernesto Uriarte Parra

## Descripción

ste proyecto implementa una librería de alto rendimiento orientada a bajo nivel, integrando:

- Python (interfaz y pruebas)
- C (puente de integración)
- Conceptos de ARM64 Assembly (AArch64)

La comunicación se realiza mediante librerías compartidas (`.so`) y el uso de `ctypes`.

## Objetivo

Demostrar la interoperabilidad entre lenguajes de alto y bajo nivel, así como analizar el rendimiento.

## Tecnologías

* Python 3
* C (clang)
* ARM64 Assembly (AArch64)
* Termux / Raspberry Pi OS

## Funcionalidades

- Suma  
- Resta  
- Multiplicación  
- Máximo y mínimo  
- Suma de arreglo  
- Conteo de pares  
- Producto punto  

## Compilación

```bash
make
```

## Ejecución

```bash
python app.py
```

## Resultados esperados

Comparación de rendimiento entre:

* Python
* C
* Assembly

## Conclusiones

El proyecto demuestra cómo combinar facilidad de uso (Python) con eficiencia (C y bajo nivel), logrando mejoras significativas en rendimiento.

## Autorreflexión

[Qué mejorarías]

Como mejora futura, se podría:

Implementar correctamente ASM en un entorno ARM64 nativo (Raspberry Pi)
Incorporar vectorización (NEON)
Realizar benchmarks más detallados
