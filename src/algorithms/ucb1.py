"""
Module: algorithms/ucb1.py
Description: Implementación del algoritmo ucb1 para el problema de los k-brazos.

Author: Iván Martínez Cuevas
Email: ivan.martinezc@um.es
Date: 2025/02/24

This software is licensed under the GNU General Public License v3.0 (GPL-3.0),
with the additional restriction that it may not be used for commercial purposes.

For more details about GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.html
"""

import numpy as np

from algorithms.algorithm import Algorithm

class UCB1(Algorithm):

    def __init__(self, k: int):
        """
        Inicializa el algoritmo UCB1.

        :param k: Número de brazos.
        """

        super().__init__(k)
        self.total_counts = 0 # Contador de pasos totales (t)

    def select_arm(self) -> int:
        """
        Selecciona un brazo basado en la política UCB1.
        :return: índice del brazo seleccionado.
        """
        # Incrementar el número total de pasos
        self.total_counts += 1

        # Si no se ha seleccionado un brazo, seleccionamos cada brazo una vez
        if 0 in self.counts:
            return np.argmin(self.counts)

        # Calcular la UCB para cada brazo
        ucb_values = self.values + np.sqrt((2 * np.log(self.total_counts))/ self.counts)

        # Seleccionar el brazo con el valor UCB más alto
        chosen_arm = np.argmax(ucb_values)

        return chosen_arm




