#include <iostream>
#include <string>
int main() {
    freopen("tttt.in", "r", stdin);
    freopen("tttt.out", "w", stdout);
    std::string board;
	for (int i{0};i<9;i++){
        char c;
        std::cin >> c;
        board.push_back(c);
    }
    std::string checks[] = {"012","345","678","036","147","258","048","246"};
    uint ones{0};
    uint twos{0};
    for (std::string win : checks){
        int a,b,c;
        a = std::stoi(win.substr(0,1)); b = std::stoi(win.substr(1,1)); c = std::stoi(win.substr(2,1));
        
        if (board[a]==board[b] && board[b]==board[c]){
            ones++;}
        if (board[a]==board[b] || board[b]==board[c] || board[c]==board[a]){
            twos++;}
    }
    std::cout << ones << std::endl;
    std::cout << twos;

    return 0;
}
