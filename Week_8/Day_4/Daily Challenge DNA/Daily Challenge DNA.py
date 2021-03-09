import random 

class Gene():
    def __init__(self):
        self.value = random.randint(0,1)
        
    
    def flip(self):
        if random.randint(0,1) == 0:
            if self.value == 0:
                self.value = 1          

class Chromosome() :
    Array_gene = []

    def __init__(self,array_gene):
        if len(array_gene) == 10: 
            self.Array_gene = array_gene
        else:
            print("Error you have to put 10 genes")

    
    def flip(self):
        for gene in self.Array_gene :
            gene.flip()

class DNA():
    Array_chromosome = []
    def __init__(self,array_chromosome):
        self.Array_chromosome = array_chromosome
        self.mutate = True

    def flip(self):
        print("flippp")
        if self.mutate:
            for chromosome in self.Array_chromosome :
                chromosome.flip()
        else:
            print("you cant flip")
   
    def is_all_ones(self):
        for ch in self.Array_chromosome:
            for ge in ch.Array_gene :
                if ge.value == 0 :
                    return False
        return True


class Organism():
    def __init__(self,dna,mutate):
        self.dna = dna
        self.dna.mutate = mutate
    
    def flip(self):
        dna.flip()

    
array_chromosome = []

for item in range(10):
    array_gene = []
    for item in range(10):
        gene = Gene()
        array_gene.append(gene)
    chromosome = Chromosome(array_gene) 
    array_chromosome.append(chromosome)

dna = DNA(array_chromosome)
def printD(org):
    for b in org.dna.Array_chromosome :
        print(f" chromo {b}")
        for c in b.Array_gene:
            print(f" gene {c.value}")


      
organism = Organism(dna,True)
organism1 = Organism(dna,True)
organism2 = Organism(dna,True)
orga = [organism,organism1,organism2]
count = 0
is_finishe = True
while is_finishe :
    print("00000")
    for org in orga :
        printD(org)
        if org.dna.is_all_ones():
            is_finishe = False
            break
    if is_finishe :      
        for org in orga :
            org.flip()
        count += 1

print(f"we flip {count} times atleast for one organsim")   


  