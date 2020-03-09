from unittest import TestCase, mock
from unittest.mock import patch, call


from mock.mock import VendinhaDoZe
from test.test_soma import soma

class TestMock(TestCase):

    @patch('mock.mock.calculo_valor_total_compra')
    @patch('mock.mock.calculo_valor_total_refrigerantes')
    @patch('mock.mock.calculo_valor_total_salgados')
    @patch('mock.mock.print')
    def test_imprime_pedido(self, mock_print, mock_total_salgados, mock_total_refrigerante, mock_total_compra):
        # Arrange (Organizar)
        nova_vendinha_do_ze = VendinhaDoZe()
        mock_print.side_effects = ['', '', '', '']
        mock_total_refrigerante.return_value = 100
        mock_total_salgados.return_value = 200
        mock_total_compra.return_value = 300

        # Action
        retorno = nova_vendinha_do_ze.imprime_pedido()

        # Assertion (Afirmações)
        self.assertIsNone(retorno)
        mock_print.assert_has_calls([
            call('Seu pedido é: '),
            call('0 unidades de  no valor de 100.0'),
            call('0 unidades de  no valor de 200.0'),
            call('O valor total da compra é de R$ 300.0')
        ])



