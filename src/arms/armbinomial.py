"""
Module: arms/armbernoulli.py
Description: Contains the implementation of the ArmBinomial class for the Binomial distribution arm.

Author: Iván Martínez Cuevas
Email: ivan.martinezc@um.es
Date: 2025/02/24

This software is licensed under the GNU General Public License v3.0 (GPL-3.0),
with the additional restriction that it may not be used for commercial purposes.

For more details about GPL-3.0: https://www.gnu.org/licenses/gpl-3.0.html
"""


import numpy as np

from arms import Arm


class ArmBinomial(Arm):
    def __init__(self, n: int, p: float):
        """
        Inicializa el brazo con distribución binomial.

        :param n: Número de ensayos.
        :param p: Probabilidad de éxito (0 <= p <= 1).
        """
        assert n > 0, "El número de ensayos n debe ser mayor que 0."
        assert 0 <= p <= 1, "La probabilidad p debe estar en el rango [0,1]."
        self.n = n
        self.p = p

    def pull(self):
        """
        Genera una recompensa siguiendo una distribución de binomial.

        :return: Recompensa obtenida del brazo.
        """
        reward = np.random.binomial(n=self.n, p=self.p)
        return reward

    def get_expected_value(self) -> float:
        """
        Devuelve el valor esperado de la distribución binomial.

        :return: Valor esperado de la distribución.
        """

        return self.n * self.p

    def __str__(self):
        """
        Representación en cadena del brazo binomial.

        :return: Descripción detallada del brazo binomial.
        """
        return f"ArmBinomial(n={self.n}, p={self.p})"

    @classmethod
    def generate_arms(cls, k: int, n: int):
        """
        Genera k brazos con medias únicas en el rango [0, 1].

        Evitamos valores extremos p=0 y p=1 porque en la mayoria de los casos reales, 
        los eventos no son completamente seguros o improbables.

        :param k: Número de brazos a generar.
        :return: Lista de brazos generados.
        """
        assert k > 0, "El número de brazos k debe ser mayor que 0."
        assert n > 0, "El número de ensayos n debe ser mayor que 0."

        # Generar k- valores únicos de mu con decimales
        p_values = set()
        while len(p_values) < k:
            p = round(np.random.uniform(0.1, 0.9), 2)  # Evitar extremos 0 y 1
            p_values.add(p)

        p_values = list(p_values)
        arms = [ArmBinomial(n, p) for p in p_values]

        return arms


