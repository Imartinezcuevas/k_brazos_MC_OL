"""
Module: algorithms/ucb2.py
Description: Implementación del algoritmo UCB2 para el problema de los k-brazos.

Author: Iván Martínez Cuevas
Email: ivan.martinezc@um.es
Date: 2025/02/24

This software is licensed under the GNU General Public License v3.0 (GPL-3.0),
with the additional restriction that it may not be used for commercial purposes.

For more details about GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.html
"""

import numpy as np
import math

from algorithms.algorithm import Algorithm

class UCB2(Algorithm):

    def __init__(self, k: int, alpha: float):
        """
        Inicializa el algoritmo UCB2.

        :param k: Número de brazos.
        :param alpha: Parámetro que controla el grado de exploración.
        """
        super().__init__(k)
        self.alpha = alpha
        self.total_counts = 0 # Contador de pasos totales (t)

        # En ucb2 necesitamos guardar las epocas de cada brazo
        self.epocas = np.zeros(k, dtype=int)

    def _ka_to_tau(self, ka: int):
        """
        Convierte una epoca ka a τ(ka), que es el número de veces que un brazo debe ser jugado en la epoca ka.

        :param ka: Epoca ka.
        :return τ(ka): Número de veces que un brazo debe ser jugado en la epoca ka.
        """
        return int(math.ceil((1 + self.alpha) ** ka))

    def select_arm(self) -> int:
        """
        Selecciona un brazo basado en la política UCB2.
        :return: índice del brazo seleccionado.
        """
        # Incrementar el número total de pasos
        self.total_counts += 1

        # Si no se ha seleccionado un brazo, seleccionamos cada brazo una vez
        if 0 in self.counts:
            return np.argmin(self.counts)

        #Para cada brazo calculamos su valor UCB2
        ucb_values = np.zeros(self.k)

        for arm in range(self.k):
            # Calcular el valor ucb2 para este brazo
            tau_k = self._ka_to_tau(self.epocas[arm])

            # Si el brazo ya ha sido jugado τ(ka) veces, calculamos el valor UCB2
            # Usamos la formula de clase
            uk = math.sqrt((1 + self.alpha) * math.log(math.e * self.total_counts / tau_k) / (2 * tau_k))
            ucb_values[arm] = self.values[arm] + uk

        # Seleccionar el brazo con el valor UCB2 más alto
        chosen_arm = np.argmax(ucb_values)

        # Actualizamos las epocas
        epoca_actual = self.epocas[chosen_arm]
        tau_actual = self._ka_to_tau(epoca_actual)

        # Si el brazo ha sido jugado τ(ka) veces, incrementamos la epoca
        if self.counts[chosen_arm] >= tau_actual:
            self.epocas[chosen_arm] += 1

        return chosen_arm




