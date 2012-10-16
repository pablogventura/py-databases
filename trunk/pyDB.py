from itertools import permutations, combinations


def subconjuntos(conjunto):
    result = []
    for i in range(1, len(conjunto)+1):
        result = result + [set(a) for a in combinations(conjunto,i)]
    return result
        

class DF(object): #dependencia funcional a->b
    def __init__(self, a, b):

        self.a=set(a)
        self.b=set(b)

        
    def es_trivial(self):
        return self.b <= self.a
        
    def atributos(self):
        return self.a.union(self.b)
    def __eq__(self, other):
        return self.a==other.a and self.b==other.b
        
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
    def __init__(self, f, atributos=None):
        self.f=set(f)
        if not atributos == None:
            self.atr=set(atributos)

    def atributos(self):
        
        result=set()
        for i in self.f:
            result=result.union(i.a)
            result=result.union(i.b)
        return self.atr
        
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
            anterior=result
            for i in result:
                contador=contador +1
                print str(contador) + "|" + str(i)
                for j in subconjuntos(i):
                    
                    a_mas=self.clausura_de_atributos(j)
                    if not (a_mas.isdisjoint(i - j) or i <= a_mas):
                        ya_esta=False # sino donde se pone en False?
                        for n in self.f:
                            if not n.es_trivial():
                                if not DF(n.a,i) in list(f_mas):
                                    
                                    if n.a.isdisjoint(n.b):
                                        result.remove(i)
                                        temp = i-n.b
                                        result.append(temp)
                                        temp=n.a.union(n.b)
                                        result.append(temp)
                                        ya_esta=True
                                        break
                        if ya_esta:
                            break
                    #else:
                    #    hecho = True
        return result

        
    def __str__(self):
        result = "{"
        for i in self.f:
            result = result + str(i) + ", "
        result = result[:-2] + "}"
        return result
