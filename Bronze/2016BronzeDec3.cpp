#include <iostream>
#include <string>

int main(){
    freopen("cowsignal.in", "r", stdin);
	freopen("cowsignal.out", "w", stdout);


    ulong M,N,K;
    std::cin >> M >> N >> K;
    for (int i{0};i<M;i++){
        std::string S;
        std::cin >> S;
        std::string S2 = "";
        for (char c : S){
            for (int ii{0};ii<K;ii++){
                S2+=c;
            }
        }
        for (int ii{0};ii<K;ii++){
                std::cout << S2 <<std::endl;
            }
    }



    return 0;
}