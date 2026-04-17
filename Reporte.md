# 📘 Reporte: Integración Python + C + ARM64

## 👤 Autor
Kevin Ernesto Uriarte Parra  

## 📅 Fecha
2026-04-16  

---

## 1. 🧠 Introducción

ARM64 (AArch64) es una arquitectura de 64 bits ampliamente utilizada en dispositivos modernos como smartphones y sistemas embebidos (ej. Raspberry Pi).  

El uso de Assembly permite trabajar directamente con registros y memoria, lo que ayuda a comprender el funcionamiento interno del procesador y optimizar el rendimiento.

👉 El ensamblador permite controlar directamente el hardware, reduciendo el overhead de lenguajes de alto nivel.

---

## 2. 📚 Marco teórico

### 🔹 Arquitectura ARM

La arquitectura ARM se basa en un diseño RISC (Reduced Instruction Set Computer), caracterizado por instrucciones simples y eficientes.

### 🔹 Registros

ARM64 cuenta con registros generales:

- x0 – x7 → argumentos de funciones  
- x0 → valor de retorno  
- x8 – x30 → uso general  
- x30 → link register (retorno de funciones)  

### 🔹 ABI (Application Binary Interface)

Define cómo se comunican las funciones:

- Paso de parámetros en registros  
- Convención de llamadas  
- Manejo de memoria  

---

## 3. 🛠️ Desarrollo

El proyecto se divide en tres partes principales:

### 🐍 Python (app.py)

- Interfaz principal  
- Uso de `ctypes` para cargar la librería `.so`  
- Ejecución de pruebas y benchmark  

---

### 🔗 C (bridge.c)

- Funciona como intermediario  
- Expone funciones que pueden ser llamadas desde Python  
- Maneja tipos de datos y compatibilidad  

---

### ⚙️ Bajo nivel (enfoque ARM64)

- Se implementan operaciones optimizadas  
- Uso de instrucciones básicas (suma, multiplicación, comparación)  
- Manipulación de arreglos mediante punteros  

---

## 4. 📊 Resultados

| Método | Tiempo |
|--------|--------|
| Python | ~0.00040 s |
| C      | ~0.000026 s |

**Speedup aproximado: ~15x**

---

## 5. 🔍 Análisis

- Python es más lento debido al intérprete  
- C reduce el overhead y mejora el rendimiento  
- El enfoque de bajo nivel permite optimizar operaciones repetitivas (loops)  

👉 El mayor beneficio se observa en procesamiento de arreglos grandes  

---

## 6. 🎯 Conclusiones

### ✔ Cuándo usar bajo nivel (ASM)

- Procesamiento intensivo  
- Sistemas embebidos  
- Optimización crítica  

### ✔ Ventajas

- Alto rendimiento  
- Control total del hardware  

### ❌ Desventajas

- Mayor complejidad  
- Difícil depuración  
- Menor portabilidad  

---

## 7. 📸 Evidencias

Se incluyen evidencias de:

- Compilación (`make`)  
- Ejecución en Python  
- Uso de GDB  
- Inspección de registros (`info registers`)  
- Ejecución paso a paso  

---

## 🧪 Evidencias capturadas

asciinema:
https://asciinema.org/a/sAsadF0hyelJXh69

Durante el desarrollo se realizaron capturas de:

- Compilación del proyecto
- Ejecución del programa
<img width="384" height="285" alt="image" src="https://github.com/user-attachments/assets/a4bad40c-9222-4b01-835d-be35475d1164" />

- Uso de GDB:
<img width="959" height="413" alt="image" src="https://github.com/user-attachments/assets/736f4147-83c0-479f-a549-925903af0c07" />

```bash
gdb python
```
<img width="944" height="503" alt="image" src="https://github.com/user-attachments/assets/110c546d-a807-46da-9f27-05816b54a2d1" />

