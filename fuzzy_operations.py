# Implement Union, Intersection, Complement and Difference operations on fuzzy sets. Also create fuzzy relations by Cartesian product of any two fuzzy sets and perform max-min composition on any two fuzzy relations.

from typing import Set, Dict, Union, List, Any
import pandas as pd

class FuzzySet:
    def __init__(self,fuzzy_values: Dict[Any, float] = None) -> None:
        self.fuzzy_values = dict()
        

        if fuzzy_values:
            for element, membership in fuzzy_values.items():
                if not (0 <= membership <= 1):
                    raise ValueError(f"Membership value for '{element}' must be between 0 and 1.")
                self.fuzzy_values[element] = membership

        self.elements = list(self.fuzzy_values.keys())
            

    def __str__(self):
        return str(pd.DataFrame(columns=['Element', 'Membership'],data=self.fuzzy_values.items()))
    
    def get(self, element:Any, default_val = None) -> float:
        if element in self.elements:
            return self.fuzzy_values[element]
        else:
            return default_val
    
    def set(self, element:Any, value:float) -> None:
        self.fuzzy_values[element] = value
        self.elements = list(self.fuzzy_values.keys())

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
    
    def cartesian_product(self, A:FuzzySet, B:FuzzySet) -> FuzzySet:
        Result = FuzzySet()
        for a_element in A.elements:
            a_mem = A.get(a_element)
            for b_element in B.elements:
                b_mem = B.get(b_element)
                pair = (a_element, b_element)
                Result.set(pair, min(a_mem, b_mem))
        return Result
    
    def max_min_composition(self, R:FuzzySet, S:FuzzySet) -> FuzzySet:
        Result = FuzzySet()
        for a,b1 in R.elements:
            for b2,c in S.elements:
                if b1 == b2:
                    value = min(R.get((a, b1)), S.get((b2,c)))
                    max_value = max(Result.get((a,c),0), value)
                    Result.set((a,c), max_value)

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

    # UnionResult = operator.union(A,B)

    # print("Union of Fuzzy Set A and B: \n",UnionResult)

    # IntersectionResult = operator.intersection(A,B)

    # print("Intersection of Fuzzy Set A and B: \n",IntersectionResult)

    # ComplementResult = operator.complement(A)

    # print("Complement of Fuzzy Set A: \n",ComplementResult)
        
    # DifferenceResult = operator.differencee(A,B)

    # print("Difference of Fuzzy Set B from A: \n",DifferenceResult)

    # ProductResult = operator.cartesian_product(A,B)

    # print("Cartesian Product of Fuzzy Set A and B: \n",ProductResult)

    # R: from X → Y
    R = {('x1', 'y1'): 0.2,('x1', 'y2'): 0.4,('x2', 'y1'): 0.6,('x2', 'y2'): 0.8}

    # S: from Y → Z
    S = {('y1', 'z1'): 0.3,('y1', 'z2'): 0.5,('y2', 'z1'): 0.7,('y2', 'z2'): 0.9}

    R = FuzzySet(R)
    S = FuzzySet(S)

    CompositionResult = operator.max_min_composition(R,S)

    print("Min-Max Composition of Fuzzy Relation R and S: \n",CompositionResult)


        