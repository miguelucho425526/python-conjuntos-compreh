# 🐍 Talleres de Python: Conjuntos y Comprehensions

Este documento reúne dos talleres prácticos sobre **Conjuntos** y **Comprehensions** en Python, junto con una explicación teórica complementaria. Su objetivo es servir como guía de estudio y práctica.

---

## 🎯 Objetivos generales
- Comprender el funcionamiento de los **conjuntos** en Python y sus operaciones básicas.  
- Aplicar **list, dict y set comprehensions** para transformar datos de manera concisa y expresiva.  
- Identificar situaciones prácticas donde estas herramientas simplifican la programación.  

---

## 📌 Taller 1: Conjuntos en Python

### Objetivo
Crear un programa que utilice operaciones básicas con conjuntos para encontrar elementos comunes y únicos de estudiantes en distintas asignaturas.

### Descripción
Se definen tres conjuntos:
- `estudiantes_matematicas` (5 estudiantes)  
- `estudiantes_fisica` (5 estudiantes)  
- `estudiantes_programacion` (5 estudiantes)  

Algunos estudiantes deben estar en más de una asignatura. Con estos conjuntos se calculan:

1. Los estudiantes que cursan **las tres asignaturas**.  
2. Los que cursan **matemáticas y física pero no programación**.  
3. Los estudiantes que **solo cursan una asignatura**.  
4. El conjunto con **todos los estudiantes únicos**.  

## 📌 Taller 2: Comprehensions en Python


## Objetivo

Crear una lista, un diccionario y un conjunto usando comprehensions.

## Descripción

Dada la lista:

palabras = ["python", "programación", "comprehension", "python", "lista", "conjunto", "programación"]


Se debe:

Crear una list comprehension que convierta todas las palabras a mayúsculas.

Crear una dict comprehension donde las claves sean las palabras y los valores sus longitudes.

Crear una set comprehension con la primera letra de cada palabra (sin duplicados).


## 📖 Lección teórica: Conjuntos en Python

Los conjuntos (set) en Python son colecciones desordenadas de elementos únicos.

Características principales

No permiten duplicados.

No tienen un orden específico.

Están optimizados para operaciones como unión, intersección y diferencia.

Operadores principales

| → Unión

& → Intersección

- → Diferencia

^ → Diferencia simétrica

Ejemplo:

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # {1, 2, 3, 4, 5}
print(A & B)  # {3}
print(A - B)  # {1, 2}
print(A ^ B)  # {1, 2, 4, 5}

Usos comunes

Eliminar duplicados de una lista.

Encontrar elementos comunes o exclusivos entre conjuntos de datos.

Verificar pertenencia de un elemento de manera rápida y eficiente.

## ✅ Conclusiones

Los conjuntos son ideales para trabajar con datos únicos y operaciones matemáticas de pertenencia.

Las comprehensions (listas, diccionarios y conjuntos) permiten escribir código más conciso, expresivo y eficiente.

Ambas herramientas combinadas facilitan la resolución de problemas comunes en análisis de datos y programación en Python.