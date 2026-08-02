# 📚 DDYA (Diseño de Datos y Algoritmos)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-Editor-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Estado](https://img.shields.io/badge/Estado-En%20Desarrollo-success?style=for-the-badge)

Repositorio académico dedicado a la materia de **Diseño de Datos y Algoritmos (DDYA)**. Aquí se organizan las prácticas, talleres, ejercicios y evaluaciones semanales desarrollados a lo largo del semestre, enfocándose en estructuras de datos, complejidad computacional y resolución algorítmica de problemas.

---

## 📅 Contenido del Curso por Semanas

### 📁 [SEMANA_01](./SEMANA_01) — *Introducción y Conceptos Básicos*
* **Descripción:** Introducción al curso, repaso de fundamentos de programación en Python, análisis preliminar y primeros ejercicios prácticos.
* **Puntos y actividades clave:**
  * Configuración del entorno de desarrollo y pruebas de diagnóstico.
  * [`prueba_tecnica.py`](./SEMANA_01/prueba_tecnica.py): Resolución de ejercicio introductorio de evaluación diagnóstica (manipulación básica de estructuras simples).
  * [`ejercicio_repaso.py`](./SEMANA_01/ejercicio_repaso.py): Práctica enfocada en funciones y manejo de flujo de control.

---

### 📁 [SEMANA_02](./SEMANA_02) — *Análisis de Complejidad (Notación Big-O)*
* **Descripción:** Estudio de la complejidad temporal y espacial en algoritmos. Casos mejor, peor y promedio mediante notación asintótica.
* **Puntos y actividades clave:**
  * Comparación empírica y teórica de tiempos de ejecución.
  * [`medicion_tiempo.py`](./SEMANA_02/medicion_tiempo.py): Script para medir y comparar experimentalmente el rendimiento de diferentes bloques de código.
  * [`ejercicios_big_o.py`](./SEMANA_02/ejercicios_big_o.py): Ejercicios de clasificación de complejidad asintótica ($O(1)$, $O(n)$, $O(n^2)$).

---

### 📁 [SEMANA_03](./SEMANA_03) — *Arreglos y Listas Lineales*
* **Descripción:** Manejo profundo de arreglos estáticos y dinámicos, búsquedas elementales y operaciones en memoria.
* **Puntos y actividades clave:**
  * Implementación de operaciones CRUD en estructuras lineales.
  * [`busqueda_lineal_binaria.py`](./SEMANA_03/busqueda_lineal_binaria.py): Implementación y comparativa entre búsqueda lineal y búsqueda binaria.
  * [`manipulacion_listas.py`](./SEMANA_03/manipulacion_listas.py): Operaciones personalizadas de inserción y eliminación sin uso de métodos nativos avanzados.

---

### 📁 [SEMANA_04](./SEMANA_04) — *Algoritmos de Ordenamiento Básicos*
* **Descripción:** Algoritmos elementales de ordenamiento polinomial y análisis de su eficiencia.
* **Puntos y actividades clave:**
  * Comprensión del intercambio de elementos (*swapping*) e invariantes de ciclo.
  * [`burbuja_seleccion.py`](./SEMANA_04/burbuja_seleccion.py): Implementación detallada del ordenamiento de Burbuja (*Bubble Sort*) y Selección (*Selection Sort*).
  * [`insercion.py`](./SEMANA_04/insercion.py): Implementación del ordenamiento por Inserción (*Insertion Sort*) en casos casi ordenados.

---

### 📁 [SEMANA_05](./SEMANA_05) — *Recursividad y Divide y Vencerás*
* **Descripción:** Fundamentos de diseño recursivo, pila de llamadas y técnica de "Divide y Vencerás".
* **Puntos y actividades clave:**
  * Identificación de casos base y relación de recurrencia.
  * [`recursividad_basica.py`](./SEMANA_05/recursividad_basica.py): Resolución recursiva de factoriales, Fibonacci y torres de Hanói.
  * [`merge_sort.py`](./SEMANA_05/merge_sort.py): Implementación clásica del algoritmo de ordenamiento por mezcla (*Merge Sort*).

---

### 📁 [SEMANA_06](./SEMANA_06) — *Algoritmos de Ordenamiento Eficientes*
* **Descripción:** Algoritmos de ordenamiento de complejidad $O(n \log n)$ y ordenamientos no comparativos.
* **Puntos y actividades clave:**
  * Estrategias de particionado y selección de pivote.
  * [`quick_sort.py`](./SEMANA_06/quick_sort.py): Implementación de *Quick Sort* analizando el impacto de diferentes pivotes.
  * [`counting_sort.py`](./SEMANA_06/counting_sort.py): Algoritmo de ordenamiento en tiempo lineal para enteros en rangos acotados.

---

### 📁 [SEMANA_07](./SEMANA_07) — *Listas Enlazadas (Simples y Dobles)*
* **Descripción:** Estructuras de datos dinámicas con punteros/referencias de nodo, gestión de memoria e iteración no contigua.
* **Puntos y actividades clave:**
  * Conexión y desconexión segura de referencias en nodos.
  * [`lista_simple.py`](./SEMANA_07/lista_simple.py): Implementación desde cero de una lista simplemente enlazada con métodos de búsqueda e inserción.
  * [`lista_doble.py`](./SEMANA_07/lista_doble.py): Implementación de una lista doblemente enlazada para recorridos bidireccionales.

---

### 📁 [SEMANA_08](./SEMANA_08) — *Pilas (Stacks) y Colas (Queues)*
* **Descripción:** Estructuras abstractas de datos lineales y sus comportamientos característicos: **LIFO** (Last In, First Out) y **FIFO** (First In, First Out).
* **Puntos y actividades clave:**
  * Modelado de procesos secuenciales y gestión de estados.
  * [`pila_parentesis.py`](./SEMANA_08/pila_parentesis.py): Algoritmo para verificar balanceo de paréntesis y llaves en expresiones lógicas.
  * [`cola_turnos.py`](./SEMANA_08/cola_turnos.py): Simulación de una cola de atención o procesamiento de tareas (incluyendo *Deque*).

---

### 📁 [SEMANA_09](./SEMANA_09) — *Tablas Hash (Diccionarios y Mapeos)*
* **Descripción:** Funciones de dispersión (*hash functions*), manejo de colisiones y búsqueda eficiente en promedio $O(1)$.
* **Puntos y actividades clave:**
  * Comprensión del factor de carga y estrategias de resolución de colisiones.
  * [`tabla_hash.py`](./SEMANA_09/tabla_hash.py): Implementación elemental de una tabla hash usando encadenamiento (*chaining*).
  * [`frecuencia_palabras.py`](./SEMANA_09/frecuencia_palabras.py): Aplicación práctica para conteo y frecuencia de elementos utilizando estructuras tipo *hash*.

---

### 📁 [SEMANA_10](./SEMANA_10) — *Árboles Generales y Árboles Binarios*
* **Descripción:** Estructuras jerárquicas no lineales, conceptos fundamentales de raíz, hojas, altura y profundidad.
* **Puntos y actividades clave:**
  * Recorridos en profundidad (Inorden, Preorden, Postorden) y en anchura (Por niveles).
  * [`arbol_binario.py`](./SEMANA_10/arbol_binario.py): Creación y recorrido recursivo de un árbol binario.
  * [`recorrido_niveles.py`](./SEMANA_10/recorrido_niveles.py): Implementación de recorrido iterativo en amplitud (*BFS*) con colas.

---

### 📁 [SEMANA_11](./SEMANA_11) — *Árboles Binarios de Búsqueda (BST)*
* **Descripción:** Propiedad de ordenamiento en árboles para inserción, búsqueda y eliminación logarítmica.
* **Puntos y actividades clave:**
  * Mantenimiento de la invariante del BST al modificar nodos.
  * [`bst_operaciones.py`](./SEMANA_11/bst_operaciones.py): Inserción, búsqueda de mínimos/máximos y eliminación de nodos con dos hijos.
  * [`validacion_bst.py`](./SEMANA_11/validacion_bst.py): Script para verificar si un árbol binario general cumple la propiedad de búsqueda.

---

### 📁 [SEMANA_12](./SEMANA_12) — *Montículos (Heaps) y Colas de Prioridad*
* **Descripción:** Árboles binarios completos con propiedad de *Heap* (Min-Heap / Max-Heap) y su uso en colas de prioridad.
* **Puntos y actividades clave:**
  * Operaciones de flotación y hundimiento (*heapify*).
  * [`min_heap.py`](./SEMANA_12/min_heap.py): Implementación de un Min-Heap basado en arreglos para extracción del mínimo en tiempo constante.
  * [`heap_sort.py`](./SEMANA_12/heap_sort.py): Algoritmo de ordenamiento *Heap Sort*.

---

### 📁 [SEMANA_13](./SEMANA_13) — *Grafos: Representación y Recorridos Básicos*
* **Descripción:** Modelado de redes mediante vértices y aristas; representaciones en memoria (matriz vs. lista de adyacencia).
* **Puntos y actividades clave:**
  * Comparación de consumo de memoria entre grafos densos y dispersos.
  * [`representacion_grafos.py`](./SEMANA_13/representacion_grafos.py): Construcción de grafos dirigidos y no dirigidos utilizando listas de adyacencia.
  * [`bfs_dfs_grafos.py`](./SEMANA_13/bfs_dfs_grafos.py): Implementación de búsqueda en anchura (*BFS*) y búsqueda en profundidad (*DFS*).

---

### 📁 [SEMANA_14](./SEMANA_14) — *Algoritmos en Grafos (Caminos Mínimos)*
* **Descripción:** Algoritmos clásicos para rutas óptimas en grafos ponderados.
* **Puntos y actividades clave:**
  * Identificación de caminos mínimos desde un origen y detección de ciclos.
  * [`dijkstra.py`](./SEMANA_14/dijkstra.py): Implementación del algoritmo de Dijkstra utilizando una cola de prioridad para aristas con peso no negativo.
  * [`arbol_expansion.py`](./SEMANA_14/arbol_expansion.py): Cálculo del Árbol de Expansión Mínima (algoritmo de Prim o Kruskal).

---

### 📁 [SEMANA_15](./SEMANA_15) — *Proyecto Final y Temas Avanzados*
* **Descripción:** Integración global de los aprendizajes del semestre, aplicación de diseño algorítmico en un problema integral y presentación del proyecto final.
* **Puntos y actividades clave:**
  * Evaluación de compensaciones (*trade-offs*) entre tiempo y memoria al combinar estructuras.
  * [`proyecto_final.py`](./SEMANA_15/proyecto_final.py): Módulo principal con la solución al problema integrador del semestre.
  * [`optimizar_solucion.py`](./SEMANA_15/optimizar_solucion.py): Refactorización e implementación de técnicas avanzadas (como Programación Dinámica o Algoritmos Ávidos) para mejorar la eficiencia.

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Icono | Descripción y Uso en el Curso |
| :--- | :---: | :--- |
| **Python** | 🐍 | Lenguaje de programación principal empleado para el modelado e implementación de algoritmos y estructuras de datos. |
| **Visual Studio Code** | 💻 | Entorno de desarrollo integrado (IDE) principal utilizado para escribir, depurar (*debug*) y ejecutar scripts. |
| **Git & GitHub** | 🐙 | Control de versiones para el seguimiento de cambios y publicación organizada de trabajos por semana. |
| **Markdown** | 📝 | Lenguaje de marcado ligero para la documentación técnica de las soluciones y elaboración de este `README.md`. |
| **Librerías Estándar** | 📦 | Uso de herramientas internas de Python (`time`, `sys`, `collections.deque`, `heapq`, `math`) para pruebas de rendimiento y optimización. |

---

*Desarrollado como registro académico para la materia de Diseño de Datos y Algoritmos (DDYA).*
