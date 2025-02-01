#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>

void printBank(std::unordered_map<std::string, std::vector<std::string>>& bank){
    std::cout << std::endl;
    for (std::string i : {"noun","conjunction","intransitive-verb","transitive-verb"}){
        std::cout << i << ":" << std::endl;
        std::vector<std::string> vect = bank[i];
        for (std::string ii : vect){
            std::cout << "\t" << ii << std::endl;
        }
    }
    std::cout << std::endl;
}

void printSentences(std::vector<std::vector<std::string>>& sentences){
    for (std::vector<std::string>& sentence : sentences){
        for (std::string& word : sentence){
            std::cout << word << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

int findNTN(std::vector<std::vector<std::string>>& sentences){
    for (int i{0};i<sentences.size();i++){
        if (sentences[i].size() ==3){
            return i;
        }
    }
    return -1;
}






int main(){
    int T;
    std::cin >> T;
    for (int i{0};i<T;i++){
        int N,C,P;
        std::cin >> N >> C >> P;
        std::unordered_map<std::string, std::vector<std::string>> wordBank{};
        for (int ii{0};ii<N;ii++){
            std::string word,type;
            std::cin >> word >> type;
            wordBank[type].push_back(word);
        }
        ulong nCount{wordBank["noun"].size()};
        ulong tCount{wordBank["transitive-verb"].size()};
        ulong iCount{wordBank["intransitive-verb"].size()};
        ulong cCount{wordBank["conjunction"].size()};

        std::vector<std::vector<std::string>> sentences{};
 int ntnCount{0};
        while (tCount >0 && nCount>1){ //make as many ntn sentences as possible
            std::string n1,n2,t1;
            t1 = wordBank["transitive-verb"].back();
            wordBank["transitive-verb"].pop_back();
            n1 = wordBank["noun"].back();
            wordBank["noun"].pop_back();
            n2 = wordBank["noun"].back();
            wordBank["noun"].pop_back();
            std::vector<std::string> sentence{};
            sentence.push_back(n1);
            sentence.push_back(t1);
            sentence.push_back(n2);
            tCount -=1;
            nCount -=2;
            sentences.push_back(sentence);
            ntnCount++;
        }
        
while (iCount >0 && nCount >0){ //makes as many ni sentences as possible

            std::string n1,i1;
            i1 = wordBank["intransitive-verb"].back();
            wordBank["intransitive-verb"].pop_back();
            n1 = wordBank["noun"].back();
            wordBank["noun"].pop_back();
            std::vector<std::string> sentence{};
            sentence.push_back(n1);
            sentence.push_back(i1);
            iCount -=1;
            nCount -=1;
            sentences.push_back(sentence);
        }

int NTNIndex= findNTN(sentences);
        if (NTNIndex != -1){ 
            while (C>0 && nCount>0){ //maximizes one ntn,n... sentence
                std::string n1;
                n1 = wordBank["noun"].back();
                wordBank["noun"].pop_back();
                C-=1;
                nCount-=1;
                sentences[NTNIndex][sentences[NTNIndex].size()-1]+=",";
                sentences[NTNIndex].push_back(n1);
            }
        }

        


        std::sort(sentences.begin(),sentences.end(),[](std::vector<std::string>& a, std::vector<std::string>& b){return a.size()<b.size();});
        std::vector<std::vector<std::string>> conjuctedSentences{};
        
        while (cCount >1 && sentences.size()>1){
            std::vector<std::string> s1,s2;
            s1=sentences.back();
            sentences.pop_back();
            s2=sentences.back();
            sentences.pop_back();
            std::vector<std::string> cSentence;
            for (std::string word : s1){
                cSentence.push_back(word);
            }
            std::string c1 = wordBank["conjunction"].back();
            wordBank["conjunction"].pop_back();
            cSentence.push_back(c1);
            for (std::string word : s2){
                cSentence.push_back(word);
            }
            conjuctedSentences.push_back(cSentence);
            cCount-=1;

        }


        for (std::vector<std::string> sentence : sentences){
            conjuctedSentences.push_back(sentence);
        }
        std::sort(conjuctedSentences.begin(),conjuctedSentences.end(),[](std::vector<std::string>& a, std::vector<std::string>& b){return a.size()<b.size();});
        std::vector<std::string> final;
        while (P>0 && conjuctedSentences.size()>0){
            std::vector<std::string> s1;
            s1 = conjuctedSentences.back();
            conjuctedSentences.pop_back();
            for (std::string i : s1){
                final.push_back(i);
            }
            final[final.size()-1]+=".";
            P-=1;
        }
        std::cout << final.size() << std::endl;
        for (int i{0};i<final.size();i++){
            std::cout << final[i] << (((i+1)!=final.size()) ? " " : "");
        } std::cout << std::endl;
        //std::cout << std::endl<< N << std::endl << C << std::endl << P <<std::endl;
        //printSentences(conjuctedSentences);
    }

    return 0;
}
