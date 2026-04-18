#include <iostream>
#include <string>

class Solution {
public:
  Solution() = default;
  std::string mergeAlternately(std::string word1, std::string word2) {
    int w1s = word1.size();
    int w2s = word2.size();

    std::string solutionString;
    solutionString.resize(w1s+w2s);

    int shortest = 0;
    int longest = 0;

	std::string longWord; 
	longWord.resize(longest); 

    if (w1s <= w2s) {
      shortest = w1s;
      longest = w2s;
	  longWord = word2; 
    } else {
      shortest = w2s;
      longest = w1s;
		longWord = word1; 
    };

    for (int i = 0; i < shortest * 2; i += 2) {
      solutionString[i] = word1[i - (i/2)];
      solutionString[i + 1] = word2[i - (i/2)];
    };

    for (int i = shortest; i < longest; ++i) {
      solutionString[shortest + i] = longWord[i];
    };

    return solutionString;
  };
};

// Ausführung der Lösung
Solution solution;

int main() {
  auto result = solution.mergeAlternately("ab", "pqrs");
  std::cout << result;
};
