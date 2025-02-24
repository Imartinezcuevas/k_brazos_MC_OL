"""
Module: algorithms/gradiente_preferencias.py
Description: Implementación del algoritmo gradiente_preferencias para el problema de los k-brazos.

Author: Iván Martínez Cuevas
Email: ivan.martinezc@um.es
Date: 2025/02/24

This software is licensed under the GNU General Public License v3.0 (GPL-3.0),
with the additional restriction that it may not be used for commercial purposes.

For more details about GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.html
"""

import numpy as np

from algorithms.algorithm import Algorithm

class GradientePreferencias(Algorithm):

    def __init__(self, k: int, alpha: float, initial_preference: float):
        """
        Inicializa el algoritmo Gradiente de Preferencias.

        :param k: Número de brazos.
        :param alpha: Tasa de aprendizaje
        :param initial_preference: Valor inicial de preferencia para todos los brazos.
        """
        super().__init__(k)

        self.alpha = alpha
        self.initial_preference = initial_preference
        
        # En lugar de valores, mantenemos preferencias para cada acción
        # Redefinimos values para representar las preferencias H_t(a)
        self.values = np.ones(k) * self.initial_preference

        # Probabilidades de selección para cada brazo
        self.probabilities = np.ones(k) / k

        # Mantenemos un registro de la recompensa media
        self.average_reward = 0.0
        self.total_reward = 0.0
        self.total_counts = 0

    def _compute_probabilities(self):
        """
        Calcula las probabilidades de selección de cada brazo usando la funcion softmax sobre las preferencias.
        """
        # Calculamos exponenciales de preferencias, con truco numérico para evitar overflow
        exp_preferences = np.exp(self.values - np.max(self.values))
        # Normalizamos para obtener probabilidades
        self.probabilities = exp_preferences / np.sum(exp_preferences)

    def select_arm(self) -> int:
        """
        Selecciona un brazo basado en las probabilidades.
        :return: índice del brazo seleccionado.
        """
        # Calculamos las probabilidades actualizadas
        self._compute_probabilities()
        
        # Seleccionar un brazo basado en las probabilidades
        chosen_arm = np.random.choice(self.k, p=self.probabilities)

        return chosen_arm
    
    def update(self, chosen_arm: int, reward: float):
        """
        Actualiza las preferencias usando el método de ascenso de gradiente.
        :param chosen_arm: Índice del brazo seleccionado.
        :param reward: Recompensa obtenida.
        """
        # Incrementamos el contador general y el del brazo elegido
        self.total_counts += 1
        self.counts[chosen_arm] += 1

        # Calculamos el error de recompensa
        self.total_reward += reward
        self.average_reward = self.total_reward / self.total_counts
        reward_error = reward - self.average_reward

        # Actualizamos la preferencia del brazo elegido usando la primera ecuación:
        # H_{t+1}(A_t) = H_t(A_t) + α(R_t - R̄_t)(1 - π_t(A_t))
        self.values[chosen_arm] += self.alpha * reward_error * (1 - self.probabilities[chosen_arm])
        
        # Actualizamos las preferencias de los brazos no elegidos usando la segunda ecuación:
        # H_{t+1}(a) = H_t(a) - α(R_t - R̄_t)π_t(a), para todo a ≠ A_t
        for arm in range(self.k):
            if arm != chosen_arm:
                self.values[arm] -= self.alpha * reward_error * self.probabilities[arm]

    def reset(self):
        """
        Reinicia el estado del algoritmo.
        """
        super().reset()
        self.probabilities = np.ones(self.k) / self.k
        self.average_reward = 0.0
        self.total_reward = 0.0
        self.total_counts = 0



