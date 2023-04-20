from usuario import Usuario
from lance import Lance
from avaliador import Avaliador

if __name__ == '__main__':
    usuario1 = Usuario("João")
    usuario2 = Usuario("Maria")

    lance1 = Lance(usuario1, 100.0)
    lance2 = Lance(usuario2, 150.0)
    lance3 = Lance(usuario1, 200.0)
    lance4 = Lance(usuario2, 250.0)
    lance5 = Lance(usuario1, 300.0)

    avaliador = Avaliador()

    avaliador.registrar_lance(lance1)
    avaliador.registrar_lance(lance2)
    avaliador.registrar_lance(lance3)
    avaliador.registrar_lance(lance4)
    avaliador.registrar_lance(lance5)

    print("Maior lance: ", avaliador.obter_maior_lance().get_valor())
    print("Menor lance: ", avaliador.obter_menor_lance().get_valor())

    maiores_lances = avaliador.obter_maiores_lances()
    print("Três maiores lances: ", [lance.get_valor() for lance in maiores_lances])

    menores_lances = avaliador.obter_menores_lances()
    print("Três menores lances: ", [lance.get_valor() for lance in menores_lances])