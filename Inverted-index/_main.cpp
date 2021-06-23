#include<bits/stdc++.h>
using namespace std;

typedef long long int ll;

struct word_position{
    string docName;
    ll line;
    ll index;
};
// resist: [A1.txt 2 1], [A1.txt 6 2] [B1.txt, lineno 3] 
class InvertedIndex{

    map<string, vector<word_position>> term_doc;
    vector<string> docList;

public:
    void addDoc(string docName);
    void show_docs();
    void query(string term);

};

void InvertedIndex::addDoc(string docName){
    ifstream fi;
    fi.open(docName, ios::in);

    if(!fi){
        cout << docName << " not found" << endl;
        return;
    }

    docList.push_back(docName);

    string line, word;

    int line_number = 0, word_number = 0;

    while(fi){
        getline(fi, line);
        
        line_number++;
        word_number = 0;

        stringstream words(line);
        while(words >> word){
            word_number++;
            // cout << word << endl;
            word_position wp;
            wp.docName = docName;
            wp.line = line_number;
            wp.index = word_number;
            term_doc[word].push_back(wp);
        }

    
    }
    // wp

    fi.close();
}

void InvertedIndex::query(string word){
    if(term_doc.find(word) == term_doc.end()){
        cout << "No instance found" << endl;
        return;
    }

    for(auto u: term_doc[word]){
        cout << "Document Name: " << u.docName << endl;
        cout << "Line Number: " << u.line << endl;
        cout << "Index: " << u.index << endl; 
    }

}
// resist
// key: val
// string : vector<word_position>


void InvertedIndex::show_docs(){
    if(!docList.size()){
        cout << "No Documents added" << endl;
        return;
    }
    cout << "{ ";
    for(auto u: docList){
        cout << u << ", ";
    }
    cout << "}";
    cout << endl;
}


InvertedIndex invIdx;
// termX: docY -> docZ ...

int main(){
    
    ll n;
    cout << "Enter number of Documents: " << endl;
    cin >> n;
    string docName;
    cout << "Enter name of all the documents with space\n";
    for(int i = 0; i < n; i++){
        cin >> docName;
        invIdx.addDoc(docName);
    }

    cout << "Files you added : ";
    invIdx.show_docs();

    ll q;
    cout << "Enter number of queries: " << endl;
    cin >> q;
    for(int i = 0; i < q; i++){
        string wrd;
        cout << "Enter term (word) to query all documents" << endl;
        cin >> wrd;
        invIdx.query(wrd);
    }

    return 0;
}