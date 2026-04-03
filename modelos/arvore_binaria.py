class No:
    def __init__(self, lead):
        self.lead = lead
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, lead):
        def _inserir(no, lead):
            if no is None:
                return No(lead)

            if lead.cpf < no.lead.cpf:
                no.esquerda = _inserir(no.esquerda, lead)
            else:
                no.direita = _inserir(no.direita, lead)

            return no

        self.raiz = _inserir(self.raiz, lead)