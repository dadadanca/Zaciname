class uzivatelAuta:
    def __init__(self, name):
        self._name = name
        self._veze = []

    def naloz(self, koho):
        if len(self._veze)<4:
            if not self._veze.__contains__(koho):
                self._veze.append(koho)

    def vyloz(self, koho):
        pass

Jarda=uzivatelAuta("Jarda")
Monika=uzivatelAuta("Monika")
Roman=uzivatelAuta("Roman")
Zuzana=uzivatelAuta("Zuzana")
Veronika=uzivatelAuta("Veronika")
Albert=uzivatelAuta("Albert")

Jarda.naloz(Monika)
Jarda.naloz(Roman)
Jarda.naloz(Roman)
Jarda.naloz(Zuzana)
Jarda.naloz(Veronika)
Jarda.naloz(Albert)
