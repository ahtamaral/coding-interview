from datetime import datetime
from typing import List

"""
Complexity: O(n**2)

for i in range(0, len(list)):
    for j in range(i+1, len(list))
        if list[i]!= list[j]:
            if list[i] == list[j]:
                return [i, j]

dict.fromkeys(a, 0)

Why use dicts: Search complexity O(1), because it is implemented as a hash table.
"""

"""
myDict = {
    2: 0,
    7: 1,
    11: 2,
    15: 3
}
"""

start_time = datetime.now()

list = [5, 7, 11, 15, 3, 8, 16, 19, 2] 
target = 9

# enumerate(nums)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # O que tava me ferrando na solução anterior era fazer uma etapa de inicialização e depois fazer o processamento.
        # Falhava p/ elementos repetidos na lista. P.ex., [3, 3] virava o dicionário {3: 1}, que permitia a lógica anterior achar a resposta
        
        # Hash map que representa os valores que já encontramos na lista e o último index associado a ele.
        seen = {}

        for idx, num in enumerate(nums):
            complement = target - num 

            # Se o complemento existe na hash_map "seen", então o elemento da lista na iteração corrente mais ele formam a resposta.
            # In this case, it doesn't matter three equal values, as we have only one solution as a premisse of the problem.
            # So, if we have two equal elements that represents a solution, not both of them will enter the seen hash.
            if complement in seen:
                return [seen[complement], idx]

            seen[num] = idx



list = [5, 7, 11, 15, 3, 8, 16, 19, 2] 
target = 9

list = [3, 3]
target = 6

sol = Solution()


print(f"Starting Solution.TwoSum() execution.")
start_time = datetime.now()

answer = sol.twoSum(list, target)

end_time = datetime.now()
time_difference = end_time - start_time

print(f"Time elapsed: {time_difference.total_seconds() * 1000:.1f} ms")

print(f"Answer: {answer}")

