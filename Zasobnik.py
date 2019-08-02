class Stack:
    def __init__(self):
        self.items = []

    def push (self, item):
        self.items.append(item)

    def pop (self):
        return self.items.pop()

    def is_empty (self):
        return len(self.items) == 0

    def peek (self):
        last = len(self.items) - 1
        return self.items[last]

stack = Stack()
for c in "Hello":
    stack.push(c)

result = ""

while not stack.is_empty():
    c = stack.pop()
    result += c

print(result)

vyraz = input("Zadej vyraz")

operatori = ["(", ")", "+", "-", "*", "/"]
def lexer(v):
    v = "( " + v + " )"
    vysledek = []
    token = ""
    for x in v:
        if x != " ":
            if x in operatori:
                if not token == "":
                    vysledek.append(token)
                    token = ""
                vysledek.append(x)
            else:
                token = token + x
    print(vysledek)
    return vysledek



tokeny_vyraz = lexer(vyraz)

cislice=Stack()
znamenka=Stack()
def spocitej(operator, a, b):
    if operator == "+":
        a = a + b
    if operator == "-":
        a = a - b
    if operator == "*":
        a = a * b
    if operator == "/":
        if b == 0:
            a = None
        else:
            a = a / b
    return a





def posledni_znamenko():
    kandidat = znamenka.pop()
    b = cislice.pop()
    a = cislice.pop()
    vysledek = spocitej(kandidat, a, b)
    cislice.push(vysledek)


for x in tokeny_vyraz:
    if not x.strip() == "":
        if not x in operatori:
            cislice.push(int(x))
        elif x == "(":
            znamenka.push(x)
        elif x == ")":
            while not znamenka.peek() == "(":
                posledni_znamenko()
            znamenka.pop()
        else:
            while True:
                if znamenka.is_empty():
                    znamenka.push(x)
                    break
                else:
                    kandidat = znamenka.peek()
                    if operatori.index(x) > operatori.index(kandidat):
                        znamenka.push(x)
                        break
                    else:
                        posledni_znamenko()

print(cislice.peek())


class Node:
    def compute(self):
        pass
    def optimize(self, parent):
        return self
    def visit(self, visitor):
        pass

class Operator (Node):
    def __init__(self, operator, priorita):
        self.operator = operator
        self.priorita = priorita
    def visit(self, visitor):
        visitor.visit_operator(self)

class Binarni_Operator(Operator):
    def __init__(self, operator, priorita):
        super().__init__(operator, priorita)
        self.levy = None
        self.pravy = None
    def __repr__(self):return "{} {} {}".format(self.levy, self.operator, self.pravy)

    def compute(self):
        l=self.levy.compute()
        p=self.pravy.compute()
        return spocitej(self.operator,l, p)

    def optimize(self, parent):
        if self.operator == "+":
            LO = self.levy.optimize(self)
            PO = self.pravy.optimize(self)
            if isinstance(LO, Cisla) and LO.hodnota == 0:
                return PO
            if isinstance(PO, Cisla) and PO.hodnota == 0:
                return LO
            self.pravy = PO
            self.levy = LO
            return self
        if self.operator == "-":
            LO = self.levy.optimize(self)
            PO = self.pravy.optimize(self)
            if isinstance(LO, Cisla) and LO.hodnota == 0:
                if(isinstance(PO, Cisla)):
                    PO.hodnota = PO.hodnota*-1
                return PO
            if isinstance(PO, Cisla) and PO.hodnota == 0:
                return LO
            self.pravy = PO
            self.levy = LO
            return self
        if self.operator == "*":
            LO = self.levy.optimize(self)
            PO = self.pravy.optimize(self)
            if isinstance(LO, Cisla) and LO.hodnota == 1:
                return PO
            if isinstance(PO, Cisla) and PO.hodnota == 1:
                return LO
            if isinstance(LO, Cisla) and LO.hodnota == 0:
                return LO
            if isinstance(PO, Cisla) and PO.hodnota == 0:
                return PO
            self.pravy = PO
            self.levy = LO
            return self
        if self.operator == "/":
            LO = self.levy.optimize(self)
            PO = self.pravy.optimize(self)
            if isinstance(PO, Cisla) and PO.hodnota == 1:
                return LO
            if isinstance(LO, Cisla) and LO.hodnota == 0:
                return LO
            self.pravy = PO
            self.levy = LO
            return self


class Zavorky(Operator):
    def __init__(self, obsah):
        super().__init__("()", 3)
        self.obsah = obsah
    def __repr__(self): return "( {} )".format(self.obsah)

    def compute(self):
        return self.obsah.compute()

    def optimize(self, parent):
        OO = self.obsah.optimize(self)
        if isinstance(OO,Zavorky):
            return OO
        if isinstance(self.obsah, Operator):
            podrizene_znamenko = self.obsah.priorita
            if parent != None and isinstance(parent, Operator):
                nadrizene_znamenko = parent.priorita
                if podrizene_znamenko>nadrizene_znamenko:
                    return OO
        self.obsah = OO
        return self


class Leva_zavorka (Operator):
    def __init__(self):
        super().__init__("(", 0)


class Cisla (Node):
    def __init__(self, hodnota):
        self.hodnota = hodnota
    def __repr__(self): return "{}".format(self.hodnota)

    def compute(self):
        return self.hodnota
    def visit(self, visitor):
        visitor.visit_cislo(self)



cislice=Stack()
znamenka=Stack()

def vrchni_znamenko():
    kandidat = znamenka.pop()
    b = cislice.pop()
    a = cislice.pop()
    kandidat.levy = a
    kandidat.pravy = b
    cislice.push(kandidat)

for x in tokeny_vyraz:
    if not x.strip() == "":
        if not x in operatori:
            cislo = Cisla(int(x))
            cislice.push(cislo)
        elif x == "(":
            znamenka.push(Leva_zavorka())
        elif x == ")":
            while not isinstance(znamenka.peek(), Leva_zavorka):
                vrchni_znamenko()
            znamenka.pop()
            o = cislice.pop()
            z = Zavorky(o)
            cislice.push(z)

        else:
            priorita = 0
            if x in ["+", "-"]: priorita = 1
            else: priorita = 2
            znamenko = Binarni_Operator(x, priorita)
            while True:
                if znamenka.is_empty():
                    znamenka.push(znamenko)
                    break
                else:
                    kandidat = znamenka.peek()
                    if znamenko.priorita > kandidat.priorita:
                        znamenka.push(znamenko)
                        break
                    else:
                        vrchni_znamenko()

class Visitor:
    def visit_cislo(self, cislo):
        pass
    def visit_operator(self, operator):
        pass

class Printing_Visitor(Visitor):
    def __init__(self):
        self.text = ""
    def visit_cislo(self, cislo):
        self.text = self.text + "{}".format(cislo.hodnota)
    def visit_operator(self, operator):
        if isinstance(operator, Zavorky):
            self.text = self.text + "("
            operator.obsah.visit(self)
            self.text = self.text + ")"
        if isinstance(operator, Binarni_Operator):
            operator.levy.visit(self)
            self.text = self.text + operator.operator
            operator.pravy.visit(self)


class Computing_Visitor(Visitor):
    def __init__(self):
        self.vysledek = 0

    def visit_cislo(self, cislo):
        self.vysledek = cislo.hodnota

    def visit_operator(self, operator):
        if isinstance(operator, Zavorky):
            operator.obsah.visit(self)
        if isinstance(operator, Binarni_Operator):
            levy_poctar = Computing_Visitor()
            pravy_poctar = Computing_Visitor()
            operator.levy.visit(levy_poctar)
            operator.pravy.visit(pravy_poctar)
            levy_vysledek = levy_poctar.vysledek
            pravy_vysledek = pravy_poctar.vysledek
            self.vysledek = spocitej(operator.operator, levy_vysledek, pravy_vysledek)

class Optimizing_Visitor(Visitor):
    def __init__(self):
        self.vysledek = None

    def visit_cislo(self, cislo):
        self.vysledek = cislo

    def visit_operator(self, operator):
        if isinstance(operator, Zavorky):
            obsahovy_optimalizator = Optimizing_Visitor()
            operator.obsah.visit(obsahovy_optimalizator)
            if isinstance(obsahovy_optimalizator.vysledek, Zavorky):
                self.vysledek = obsahovy_optimalizator.vysledek
            else:
                if isinstance(obsahovy_optimalizator.vysledek, Binarni_Operator):
                    optimalozovany_operator = obsahovy_optimalizator.vysledek
                    if optimalozovany_operator.operator == "*" or optimalozovany_operator.operator == "/":
                        self.vysledek = obsahovy_optimalizator.vysledek
                        return
                self.vysledek = operator
                self.vysledek.obsah = obsahovy_optimalizator.vysledek

        if isinstance(operator, Binarni_Operator):
            levy_optimalizator = Optimizing_Visitor()
            pravy_optimalizator = Optimizing_Visitor()
            operator.levy.visit(levy_optimalizator)
            operator.pravy.visit(pravy_optimalizator)
            if operator.operator == "+":
                if isinstance(levy_optimalizator.vysledek, Cisla) and levy_optimalizator.vysledek.hodnota == 0:
                    self.vysledek = pravy_optimalizator.vysledek
                elif isinstance(pravy_optimalizator.vysledek, Cisla) and pravy_optimalizator.vysledek.hodnota == 0:
                    self.vysledek = levy_optimalizator.vysledek
                else:
                    self.vysledek = operator
                    if isinstance(levy_optimalizator.vysledek, Zavorky) and isinstance(levy_optimalizator.vysledek.obsah, Binarni_Operator) :
                        self.vysledek.levy = levy_optimalizator.vysledek.obsah
                    else:
                        self.vysledek.levy = levy_optimalizator.vysledek
                    if isinstance(pravy_optimalizator.vysledek, Zavorky) and isinstance(
                            pravy_optimalizator.vysledek.obsah, Binarni_Operator):
                        self.vysledek.pravy = pravy_optimalizator.vysledek.obsah
                    else:
                        self.vysledek.pravy = pravy_optimalizator.vysledek

            if operator.operator == "-":
                if isinstance(levy_optimalizator.vysledek, Cisla) and levy_optimalizator.vysledek.hodnota == 0:
                    if isinstance(pravy_optimalizator.vysledek, Cisla):
                        self.vysledek = pravy_optimalizator.vysledek
                        self.vysledek.hodnota = -1 * self.vysledek.hodnota
                        return
                elif isinstance(pravy_optimalizator.vysledek, Cisla) and pravy_optimalizator.vysledek.hodnota == 0:
                    self.vysledek = levy_optimalizator.vysledek
                else:
                    self.vysledek = operator
                    self.vysledek.levy = levy_optimalizator.vysledek
                    self.vysledek.pravy = pravy_optimalizator.vysledek
            if operator.operator == "*":
                if isinstance(levy_optimalizator.vysledek, Cisla) and levy_optimalizator.vysledek.hodnota == 1:
                    self.vysledek = pravy_optimalizator.vysledek
                elif isinstance(pravy_optimalizator.vysledek, Cisla) and pravy_optimalizator.vysledek.hodnota == 1:
                    self.vysledek = levy_optimalizator.vysledek
                elif isinstance(levy_optimalizator.vysledek, Cisla) and levy_optimalizator.vysledek.hodnota == 0:
                    self.vysledek = levy_optimalizator.vysledek
                elif isinstance(pravy_optimalizator.vysledek, Cisla) and pravy_optimalizator.vysledek.hodnota == 0:
                    self.vysledek = pravy_optimalizator.vysledek
                else:
                    self.vysledek = operator
                    self.vysledek.levy = levy_optimalizator.vysledek
                    self.vysledek.pravy = pravy_optimalizator.vysledek
            if operator.operator == "/":
                if isinstance(levy_optimalizator.vysledek, Cisla) and levy_optimalizator.vysledek.hodnota == 0:
                    self.vysledek = levy_optimalizator.vysledek
                elif isinstance(pravy_optimalizator.vysledek, Cisla) and pravy_optimalizator.vysledek.hodnota == 1:
                    self.vysledek = levy_optimalizator.vysledek
                else:
                    self.vysledek = operator
                    self.vysledek.levy = levy_optimalizator.vysledek
                    self.vysledek.pravy = pravy_optimalizator.vysledek


print("-----------------------------")

navstevnik1 = Printing_Visitor()
cislice.peek().visit(navstevnik1)
print(navstevnik1.text)

poctar1 = Computing_Visitor()
cislice.peek().visit(poctar1)
print(poctar1.vysledek)

naparsovany_vyraz_Obaleny_zavorkami = cislice.peek()
naparsovany_vyraz = naparsovany_vyraz_Obaleny_zavorkami.obsah
optimalizator = Optimizing_Visitor()
naparsovany_vyraz.visit(optimalizator)

navstevnik1 = Printing_Visitor()
optimalizator.vysledek.visit(navstevnik1)
print(navstevnik1.text)







