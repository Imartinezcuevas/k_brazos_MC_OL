"""
Module: algorithms/softmax.py
Description: Implementación del algoritmo softmax para el problema de los k-brazos.

Author: Iván Martínez Cuevas
Email: ivan.martinezc@um.es
Date: 2025/02/24

This software is licensed under the GNU General Public License v3.0 (GPL-3.0),
with the additional restriction that it may not be used for commercial purposes.

For more details about GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.html
"""

import numpy as np

from algorithms.algorithm import Algorithm

class Softmax(Algorithm):

    def __init__(self, k: int, tau: float):
        """
        Inicializa el algoritmo Softmax.

        :param k: Número de brazos.
        :param tau: Parámetro que controla el grado de exploración.
        :raises ValueError: Si el valor de tau es menor o igual a 0.
        """
        assert tau > 0, "El valor de tau debe ser mayor que 0."

        super().__init__(k)
        self.tau = tau

    def select_arm(self) -> int:
        """
        Selecciona un brazo basado en la política Softmax.
        :return: índice del brazo seleccionado.
        """
        
        # Calcular las probabilidades de selección de cada brazo
        probabilities = np.exp(self.values / self.tau) / np.sum(np.exp(self.values / self.tau))
        
        # Seleccionar un brazo basado en las probabilidades
        chosen_arm = np.random.choice(self.k, p=probabilities)

        return chosen_arm




