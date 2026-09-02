import unittest
from jogo import determinar_vencedor

class TestSpockLagarto(unittest.TestCase):

    def test_empates(self):
        """Testa novos cenários de empate."""
        self.assertEqual(determinar_vencedor("spock", "spock"), "Empate")
        self.assertEqual(determinar_vencedor("lagarto", "lagarto"), "Empate")

    def test_vitorias_novas_opcoes(self):
        """Testa se as novas opções ganham de quem deveriam."""
        # Testando o Lagarto
        self.assertEqual(determinar_vencedor("lagarto", "spock"), "Jogador")
        self.assertEqual(determinar_vencedor("lagarto", "papel"), "Jogador")
        # Testando o Spock
        self.assertEqual(determinar_vencedor("spock", "pedra"), "Jogador")
        self.assertEqual(determinar_vencedor("spock", "tesoura"), "Jogador")

    def test_derrotas_novas_opcoes(self):
        """Testa se as novas opções perdem para quem deveriam."""
        # Lagarto perde para Pedra e Tesoura
        self.assertEqual(determinar_vencedor("lagarto", "pedra"), "Computador")
        self.assertEqual(determinar_vencedor("lagarto", "tesoura"), "Computador")
        # Spock perde para Papel e Lagarto
        self.assertEqual(determinar_vencedor("spock", "papel"), "Computador")
        self.assertEqual(determinar_vencedor("spock", "lagarto"), "Computador")

if __name__ == "__main__":
    unittest.main()


