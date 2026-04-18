#include <iostream>
class Solution {
public:
  int mirrorDistance(int n) {
    int result = 0;

    while (n != 0) {
	  int secondnum = n % 10; 
	  result =result *10 + secondnum;
	  n /= 10; 
    };

    return result;
  }
};

Solution solution;
int main () {
  auto result = solution.mirrorDistance(100); 
  result = static_cast<char>(result); 
  std::cout << result ; 
}
