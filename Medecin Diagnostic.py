class Patient:
    def __init__(self, nom, maladie, argent=0, poche=None, etat_sante="malade"):
        self.nom = nom
        self.maladie = maladie
        self.argent = argent
        self.poche = poche
        self.etat_sante = etat_sante

