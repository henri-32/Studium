all: 
	@g++ -std=c++17  -O0 -g -c Tasks/mergeStrings.cpp -o build/mergeStrings.o
	@g++ -std=c++17 -O0 -g -c Tasks/3782_Mirror_Distance_of_an_Integer.cpp -o build/3782_Mirror_Distance_of_an_Integer.o
	@echo "successfully compiled" 
	@g++ build/mergeStrings.o -o mergeStrings 
	g++ build/3782_Mirror_Distance_of_an_Integer.o -o mirrorDistance

clean: 
	@rm -f ./*.o 
	@rm -f ./builf/*.o
	@echo "object files removed"
