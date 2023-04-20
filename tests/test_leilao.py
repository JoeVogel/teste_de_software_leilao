import pytest
from src.usuario import Usuario
from src.lance import Lance
from src.avaliador import Avaliador

class TestUsuario:
    def test_usuario(self):
        usuario = Usuario("João")
        assert usuario.get_nome() == "João"

class TestLance:
    def test_lance(self):
        usuario = Usuario("João")
        lance = Lance(usuario, 100.0)
        assert lance.get_usuario() == usuario
        assert lance.get_valor() == 100.0

class TestAvaliador:
    @pytest.fixture
    def avaliador(self):
        return Avaliador()

    @pytest.fixture
    def usuarios(self):
        return [Usuario("João"), Usuario("Maria"), Usuario("Pedro")]

    @pytest.fixture
    def lances(self, usuarios):
        return [
            Lance(usuarios[0], 100.0),
            Lance(usuarios[1], 150.0),
            Lance(usuarios[0], 200.0),
            Lance(usuarios[2], 250.0),
            Lance(usuarios[1], 300.0),
        ]

    def test_maior_e_menor_lance(self, avaliador, lances):
        for lance in lances:
            avaliador.registrar_lance(lance)

        assert avaliador.obter_maior_lance().get_valor() == 300.0
        assert avaliador.obter_menor_lance().get_valor() == 100.0

    def test_tres_maiores_e_tres_menores_lances(self, avaliador, lances):
        for lance in lances:
            avaliador.registrar_lance(lance)

        maiores_lances = avaliador.obter_maiores_lances(3)
        assert [lance.get_valor() for lance in maiores_lances] == [300.0, 250.0, 200.0]

        menores_lances = avaliador.obter_menores_lances(3)
        assert [lance.get_valor() for lance in menores_lances] == [100.0, 150.0, 200.0]