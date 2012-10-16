from itertools import permutations, combinations


def subconjuntos(conjunto):
    result = []
    for i in range(1, len(conjunto)+1):
        result = result + [set(a) for a in combinations(conjunto,i)]
    return result
        

class DF(object): #dependencia funcional a->b
    def __init__(self, a=[], b=[]):

        self.a=set(a)
        self.b=set(b)

        
    def es_trivial(self):
        return self.b <= self.a
        
    def atributos(self):
        return self.a.union(self.b)

    def from_parse(self, cadena):
        a,b=cadena.split("->",2)
        a=filter(lambda x: x!="", a.split(" "))
        b=filter(lambda x: x!="", b.split(" "))
        self.a=set(a)
        self.b=set(b)
        
    def __eq__(self, other):
        return self.a==other.a and self.b==other.b
        
    def __hash__(self):
        return hash((tuple(self.a),tuple(self.b)))
        
    def __str__(self):
        result = "("
        for i in self.a:
            result = result + str(i) + " "
        result = result + "-> "
        for i in self.b:
            result = result + str(i) + " "
        result = result[:-1] + ")"
        return result
        
class CDF(object): #conjunto de dependencias funcionales
    def __init__(self, f=[], atributos=set()):
        self.f=set(f)
        self.atr=set(atributos)

    def atributos(self):
        if len(self.atr) > 0:
            result = self.atr
        else:
            result=set()
            for i in self.f:
                result=result.union(i.a)
                result=result.union(i.b)

        return result
        
    def clausura_de_atributos(self, atributos):
        result = set(atributos)
        anterior=set()
        while anterior != result:
            anterior = result
            for i in self.f:
                if i.a <= result: # a esta incluido en result
                    result = result.union(i.b)
                    cambio = True
        return result
        
    def clausura(self): #agregar capacidad de tomar esquema de atributos
        result = set()
        for i in subconjuntos(self.atributos()):
            for j in subconjuntos(self.clausura_de_atributos(i)):
                result.add(DF(i,j))
        return result


    def es_fnbc(self,d):
        ri = d.atributos()
        for i in subconjuntos(ri):
            pass #TODO
        return d.es_trivial() or True 

        
    
    def fnbc(self):

        result=[self.atributos()]
        hecho=False
        f_mas=self.clausura()
        anterior=[]
        contador = 0
        while result != anterior:
            anterior=result[:] # para hacer una copia real
            for i in result:
                contador=contador +1
                for j in subconjuntos(i):
                    
                    a_mas=self.clausura_de_atributos(j)
                    if not (a_mas.isdisjoint(i - j) or i <= a_mas):
                        ya_esta=False # sino donde se pone en False?
                        for n in self.f:
                            if not n.es_trivial():
                                if not DF(n.a,i) in f_mas:
                                    if n.a.isdisjoint(n.b) and not i.isdisjoint(n.b):
                                        # es posible que la segunda condicion tenga que ver con F_i
                                        result.remove(i)
                                        temp = i-n.b
                                        result.append(temp)
                                        temp=n.a.union(n.b)
                                        result.append(temp)


                                        ya_esta=True
                                        break
                        if ya_esta:
                            break
        return result

    def from_parse(self, cadena, s_atributos=""):
        dfs=cadena.split(",")
        self.atr=set(filter(lambda x: x!="", s_atributos.split(","))) # TODO mejorar el parseo para que no sea solo con comas
        for i in dfs:
            new = DF()
            new.from_parse(i)
            self.f.add(new)
        
    def __str__(self):
        result = "{"
        for i in self.f:
            result = result + str(i) + ", "
        result = result[:-2] + "}"
        return result
