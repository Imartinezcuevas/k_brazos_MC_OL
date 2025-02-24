"""
Module: arms/armbernoulli.py
Description: Contains the implementation of the ArmBernoulli class for the Bernoulli distribution arm.

Author: Iván Martínez Cuevas
Email: ivan.martinezc@um.es
Date: 2025/02/24

Se ha utilizado como referencia: 
https://github.com/xbeat/Machine-Learning/blob/main/Bernoulli%20Distribution%20Explained%20with%20Python.md
Donde se explica la distribución de Bernoulli y se proporciona un ejemplo de implementación en Python.

This software is licensed under the GNU General Public License v3.0 (GPL-3.0),
with the additional restriction that it may not be used for commercial purposes.

For more details about GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.html
"""


import numpy as np

from arms import Arm


class ArmBernoulli(Arm):
    def __init__(self, p: float):
        """
        Inicializa el brazo con distribución Bernoulli.

        :param p: Probabilidad de éxito (0 <= p <= 1).
        """
        assert 0 <= p <= 1, "La probabilidad p debe estar en el rango [0,1]."

        self.p = p

    def pull(self):
        """
        Genera una recompensa siguiendo una distribución de Bernoulli.

        :return: Recompensa obtenida del brazo.
        """
        reward = np.random.binomial(n=1, p=self.p)
        return reward

    def get_expected_value(self) -> float:
        """
        Devuelve el valor esperado de la distribución bernoulli.

        :return: Valor esperado de la distribución.
        """

        return self.p

    def __str__(self):
        """
        Representación en cadena del brazo bernoulli.

        :return: Descripción detallada del brazo bernoulli.
        """
        return f"ArmBernoulli(p={self.p})"

    @classmethod
    def generate_arms(cls, k: int):
        """
        Genera k brazos con medias únicas en el rango [0, 1].

        Evitamos valores extremos p=0 y p=1 porque en la mayoria de los casos reales, 
        los eventos no son completamente seguros o improbables.

        :param k: Número de brazos a generar.
        :return: Lista de brazos generados.
        """
        assert k > 0, "El número de brazos k debe ser mayor que 0."

        # Generar k- valores únicos de mu con decimales
        p_values = set()
        while len(p_values) < k:
            p = round(np.random.uniform(0.1, 0.9), 2)  # Evitar extremos 0 y 1
            p_values.add(p)

        p_values = list(p_values)
        arms = [ArmBernoulli(p) for p in p_values]

        return arms


