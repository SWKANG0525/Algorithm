/*
	Author : Kang Ho Dong
	Date : 2019 - 01 - 10
	Title : BOJ 1011 ( Fly to the Alpha Centauri )
	Link : https://www.acmicpc.net/problem/1011
	Language : C++

*/

#include <iostream>
#include <cmath>

using namespace std;
int main() {
	int xpos1,xpos2,count; // Input Data xpos1, xpos2
	cin >> count; // Loop Count. 
	
	while(count--) { // Loop Count -- 
		cin >> xpos1 >> xpos2;  // Data Input
		
		int _maxhop = xpos2-xpos1; // Max hop distance
		int _k = 1; // Max Distance at once 
		int _min_distance=0; // Minimum Distance. ( Answer )
		int _between = 0 ; // (V0(1) ... V1(_k)) * Hop(t) = _between(S). 
	 
			// Line 18~28 Calculate Max_K (k^2)
			while(true) {
			
				if(pow(_k,2) <=_maxhop) 
					_k += 1;

				else if(pow(_k,2) > _maxhop) {
					_k-=1;
					break;
				}
			
		}
		
		//Calculate Moved Distance. And Hop Count.
		for(int temp = 1; temp<=_k; temp++) {
			_min_distance++;	
			_between += temp;
		}
		
		//Calculate HopCount Remainder.
		if(pow(_k,2) == _maxhop)
			_min_distance = _min_distance*2-1;
		else if(_maxhop-_between>_between)
			_min_distance = _min_distance*2+1;
		else if(_between>=_maxhop-_between)
			_min_distance *=2;

		//Print Answer!
		cout <<_min_distance << endl;
	}

	}

