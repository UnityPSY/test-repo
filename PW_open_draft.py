class Drug:

    def __init__(self, name, chemical_class, effect_class, roa):
        self.name = name
        self.chemical_class = chemical_class
        self.effect_class = effect_class
        self.roa = roa
    
drug_1 = Drug('LSD', 'lysergamide', 'psychedelic', 'oral')

print(drug_1.name)
