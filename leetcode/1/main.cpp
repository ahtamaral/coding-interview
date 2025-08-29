#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
	{
		vector<int> indices;

		for ( long unsigned int i = 0; i < nums.size(); i++ )
		{
			for ( long unsigned int j = i+1; j < nums.size(); j++)
			{
				if (nums[i] + nums[j] == target) {
					indices.push_back(i);
					indices.push_back(j);
				}
			}
		}

		return indices;
	}

    /*
	// Solução O(n): Para cada valor do vetor, estou procurando seu complemente que somará 'target'. P/ exemplo,
	// Se na iteração corrente tenho o valor 3, estou procurando pelo valor 7 no vetor. Operações de busca em uma
	// hash table são O(1). Ou seja, é só buscar pelo 7. Se não encontrar, continua percorrendo o vetor.

	// My unordered_map -> 
	// What do i need to search?
	// key: What i search 
	// value: The value associated to my search.
	// I want to search the complement (target - v[i])
	// I want the index associateds with it
	{2,7,11,15}
	// The unordered_map needs to be just the value as key and index as value.

	v[i] = 2
	complement = target - v[i] // 7

	*/

	vector<int> twoSumUnMap(vector<int>& nums, int target) 
	{
		vector<int> indices;
		unordered_map<int, int> unMap;

		for ( long unsigned int i = 0; i < nums.size(); i++ ) {
			unMap[nums[i]] = i;
		}

		for ( long unsigned int i = 0; i < nums.size(); i++ )
		{
			int complement = target - nums[i];
			try {
				int secondIdx = unMap.at(complement);
				//std::cout << secondIdx << "\n";
				if (secondIdx != i){
					int firstIdx = i;
					indices.push_back(firstIdx);
					indices.push_back(secondIdx);
					return indices;
				}
			} catch(...) {}
		}

		return indices;
	}

};

int main()
{
	// vector<int> v = {2,7,11,15}; int target = 9;
	// vector<int> v = {3,0,0,0,0,0,0,0,3}; int target = 6;
	vector<int> v = {3,2,4}; int target = 6;

	vector<int> answer;

	Solution s;
	answer = s.twoSum(v, target);

	std::cout << "Answer: ";
	for (auto & i : answer)
		std::cout << i << " ";
	std::cout << std::endl;

	answer = s.twoSumUnMap(v, target);
	
	std::cout << "Answer: ";
	for (auto & i : answer)
		std::cout << i << " ";
	std::cout << std::endl;
	
	return 0;
}
