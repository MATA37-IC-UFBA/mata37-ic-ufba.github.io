import unittest
# Importa a função de lógica do nosso arquivo jogo.py
from jogo import determinar_vencedor

class TestPedraPapelTesoura(unittest.TestCase):

    def test_empates(self):
        """Testa se escolhas iguais resultam em empate."""
        self.assertEqual(determinar_vencedor("pedra", "pedra"), "Empate")
        self.assertEqual(determinar_vencedor("papel", "papel"), "Empate")
        self.assertEqual(determinar_vencedor("tesoura", "tesoura"), "Empate")

    def test_vitorias_do_jogador(self):
        """Testa todos os cenários onde o jogador deve vencer."""
        self.assertEqual(determinar_vencedor("pedra", "tesoura"), "Jogador")
        self.assertEqual(determinar_vencedor("papel", "pedra"), "Jogador")
        self.assertEqual(determinar_vencedor("tesoura", "papel"), "Jogador")

    def test_derrotas_do_jogador(self):
        """Testa todos os cenários onde o computador deve vencer."""
        self.assertEqual(determinar_vencedor("pedra", "papel"), "Computador")
        self.assertEqual(determinar_vencedor("papel", "tesoura"), "Computador")
        self.assertEqual(determinar_vencedor("tesoura", "pedra"), "Computador")

if __name__ == "__main__":
    unittest.main()


