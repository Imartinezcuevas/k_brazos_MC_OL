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
        self.epoch_counts = np.zeros(self.k, dtype=int)

        self.remaining_pulls = 0  # Número de veces restantes para devolver el brazo
        self.current_arm = None # Brazo seleccionado actualmente

    def select_arm(self):
        """
        Selecciona un brazo basado en la política UCB2.
        :return: índice del brazo seleccionado.
        """
        # Incrementar el número total de pasos
        self.total_counts += 1

        # Si no se ha seleccionado un brazo, seleccionamos cada brazo una vez
        if 0 in self.counts:
            return np.argmin(self.counts)
        
        if self.remaining_pulls > 0:
            self.remaining_pulls -= 1
            return self.current_arm

        #Para cada brazo calculamos su valor UCB2
        ucb_values = self.values + np.sqrt(((1 + self.alpha) * np.log(self.total_counts / self.counts)) / (2 * self.counts))
        chosen_arm = np.argmax(ucb_values) # Selecciona el brazo con el valor UCB2 más alto

        tau = self.epoch_counts[chosen_arm] # Obtiene el número de veces que se seleccionó el brazo en la época anterior
        if tau == 0:
            tau = 1 # Si es la primera vez, tau es 1

        self.epoch_counts = self.counts.copy() # Actualiza el contador de la época anterior con los conteos actuales
        self.current_arm = chosen_arm
        self.remaining_pulls = tau - 1 # Actualiza el número de veces restantes para devolver el brazo
        return chosen_arm # Devolvemos tau para saber cuantas veces tengo que tirar del brazo

    def reset(self):
        self.counts = np.zeros(self.k, dtype=int)
        self.values = np.zeros(self.k, dtype=float)
        self.epoch_counts = np.zeros(self.k, dtype=int)
        self.total_counts = 0
        self.remaining_pulls = 0
        self.current_arm = None

        




