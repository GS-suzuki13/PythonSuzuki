from unittest import TestCase

from soma import soma
from soma import Pessoa


class TestAssert(TestCase):
    def test_sum(self):
        # Arrange (Organiza)



        # Action (Ação)
        result = soma(2,2)


        # Assetion (Afirmações)
        self.assertEqual(result,4)

    def test_classe_pessoa(self):
        # Arrange (Organiza)


        # Action (Ação)
        nova_pessoa = Pessoa('Gustavo', "Suzuki")

        # Assetion (Afirmações)
        self.assertIsInstance(nova_pessoa, Pessoa)
        self.assertEqual(nova_pessoa.nome, 'Gustavo')
        self.assertEqual(nova_pessoa.sobrenome, 'Suzuki')
