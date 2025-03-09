# Práctica 1: Problema del Bandido de k-Brazos

# Título del Trabajo
## Información
- **Alumnos:** Martínez Cuevas, Iván; Orenes Lucas, Antonio; ...
- **Asignatura:** Extensiones de Machine Learning
- **Curso:** 2024/2025
- **Grupo:** MC_OL

## Descripción
La motivación para este estudio es entender cómo diferentes algoritmos equilibran \textbf{exploración con explotación} en entornos con distribuciones heterogéneas (Normal, Binomial, Bernoulli). Estudiar variantes de **Epsilon-Greedy**, **UCB** y métodos basados en **Ascenso del Gradiente** permite identificar **ventajas y limitaciones** de cada algoritmo para después poder usarlos de manera adecuada en entornos reales.

Los objetivos son los siguientes:
*  **Comprar el rendimiento** de epsilon-Greedy, UCB1, UCB2 y metodos de ascenso del gradiente (Softmax, Gradiente de Preferencias) en distribuciones discretas y continuas.
* Analizar el **impacto de hiperparámetros** como alpha (UCB2), epsilon (epsilon-Greedy) y tau (Softmax) en la convergencia.
* **Evaluar la escalabilidad** con distintos números de brazos.

## Estructura
- **`src/algorithms/`**: Implementaciones de los algoritmos estudiados.
- **`src/arms/`**: Contiene las implementaciones de los distintos tipos de brazos.
- **`src/plotting/`**: Funciones para la visualización de resultados.
- **`main.ipynb`**: Notebook principal que describe el problema y tiene enlaces a los distintos experimentos.
- **`bandit_experiment_*.ipynb`**: Notebooks donde se estudian los distintos algoritmos.
- **`requirements.txt`**: Dependencias necesarias para la ejecución del proyecto.


## Instalación y Uso
No se necesita de instalación. 

Desde el notebook `main` se puede navegar a los distintos experimentos. Al inicio de cada notebook se hace una copia del repositorio e instalación de todos los paquetes necesarios. 
