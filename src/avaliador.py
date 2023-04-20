class Avaliador:
    def __init__(self):
        self.lances = []

    def registrar_lance(self, lance):
        self.lances.append(lance)

    def obter_maior_lance(self):
        maior_lance = None
        for lance in self.lances:
            if maior_lance is None or lance.get_valor() > maior_lance.get_valor():
                maior_lance = lance
        return maior_lance

    def obter_menor_lance(self):
        menor_lance = None
        for lance in self.lances:
            if menor_lance is None or lance.get_valor() < menor_lance.get_valor():
                menor_lance = lance
        return menor_lance
    
    def obter_maiores_lances(self, quantidade=3):
        sorted_lances = sorted(self.lances, key=lambda x: x.get_valor(), reverse=True)
        return sorted_lances[:quantidade]

    def obter_menores_lances(self, quantidade=3):
        sorted_lances = sorted(self.lances, key=lambda x: x.get_valor())
        return sorted_lances[:quantidade]