# Implement Union, Intersection, Complement and Difference operations on fuzzy sets. Also create fuzzy relations by Cartesian product of any two fuzzy sets and perform max-min composition on any two fuzzy relations.

from typing import Set, Dict, Union, List
import pandas as pd

class FuzzySet:
    def __init__(self,fuzzy_values: Dict[Union[str, int], float] = None) -> None:
        self.fuzzy_values = dict()
        

        if fuzzy_values:
            for element, membership in fuzzy_values.items():
                if not (0 <= membership <= 1):
                    raise ValueError(f"Membership value for '{element}' must be between 0 and 1.")
                self.fuzzy_values[element] = membership

        self.elements = list(self.fuzzy_values.keys())
            

    def __str__(self):
        return str(pd.DataFrame(columns=['Element', 'Membership'],data=self.fuzzy_values.items()))
    
    def get(self, element:str|int) -> float:
        return self.fuzzy_values[element]
    
    def set(self, element:str|int, value:float) -> None:
        self.fuzzy_values[element] = value

    def items(self):
        return self.fuzzy_values.items()
    
    def copy(self) -> "FuzzySet":
        return FuzzySet(self.fuzzy_values)
    
class FuzzySetOperator:
    def __init__(self) -> None:
        pass
    
    def union(self, A:FuzzySet, B:FuzzySet) -> FuzzySet:
        Result = FuzzySet()
        elements: Set = sorted(set(A.elements + B.elements))
        for element in elements:
            if element in A.elements and element in B.elements:
                value = max(A.get(element), B.get(element))
                Result.set(element, value)
            elif element in A.elements:
                value = A.get(element)
                Result.set(element, value)
            else:
                value = B.get(element)
                Result.set(element, value)

        return Result
    
    def intersection(self, A:FuzzySet, B:FuzzySet) -> FuzzySet:
        Result = FuzzySet()
        elements: Set = sorted(set(A.elements + B.elements))
        for element in elements:
            if element in A.elements and element in B.elements:
                value = min(A.get(element), B.get(element))
                Result.set(element, value)

        return Result
    
    def complement(self, A:FuzzySet) -> FuzzySet:
        Result = FuzzySet()
        for element, membership in A.items():
            Result.set(element, 1 - membership)
        return Result
    
    def difference(self, A:FuzzySet, B:FuzzySet) -> FuzzySet:
        Result = FuzzySet()
        for element in A.elements:
            a_mem = A.get(element)
            if element in B.elements:
                b_mem = B.get(element)
                result_mem = min(a_mem, 1 - b_mem)
            else:
                result_mem = a_mem 
            Result.set(element, result_mem)
        return Result


if __name__=='__main__':
    #Fuzzy Values
    a = {'x1':0.2,
        'x2':0.6,
        'x3':0.3,
        'x4':0.5,
        'x5':0.9}

    b = {'x1':0.4,
        'x2':0.7,
        'x3':0.5,
        'x4':0.1,
        'x5':0.2,
        'x6':0.1}
    
    A = FuzzySet(a)
    B = FuzzySet(b)
    operator = FuzzySetOperator()

    print("Following is the Fuzzy Set A: \n",A)
    print("Following is the Fuzzy Set B: \n",B)

    UnionResult = operator.union(A,B)

    print("Union of Fuzzy Set A and B: \n",UnionResult)

    IntersectionResult = operator.intersection(A,B)

    print("Intersection of Fuzzy Set A and B: \n",IntersectionResult)

    ComplementResult = operator.complement(A)

    print("Complement of Fuzzy Set A: \n",ComplementResult)
        
    DifferenceResult = operator.differencee(A,B)

    print("Difference of Fuzzy Set B from A: \n",DifferenceResult)



        