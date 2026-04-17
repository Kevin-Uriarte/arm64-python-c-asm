/*
 * Autor: Kevin Uriarte
 * Fecha: 2026-04-16
 * Descripción:
 * Implementación en C (compatible universalmente).
 * Preparado para integración con ARM64 Assembly.
 */

#include <stdint.h>

// Operaciones básicas
int64_t add(int64_t a, int64_t b) {
    return a + b;
}

int64_t sub(int64_t a, int64_t b) {
    return a - b;
}

int64_t mul(int64_t a, int64_t b) {
    return a * b;
}

int64_t max(int64_t a, int64_t b) {
    return (a > b) ? a : b;
}

int64_t min(int64_t a, int64_t b) {
    return (a < b) ? a : b;
}

// Arreglos
int64_t sum_array(int64_t* arr, int64_t n) {
    int64_t sum = 0;
    for (int64_t i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum;
}

int64_t count_even(int64_t* arr, int64_t n) {
    int64_t count = 0;
    for (int64_t i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) count++;
    }
    return count;
}

int64_t dot_product(int64_t* a, int64_t* b, int64_t n) {
    int64_t result = 0;
    for (int64_t i = 0; i < n; i++) {
        result += a[i] * b[i];
    }
    return result;
}
