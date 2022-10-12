/*
 * @author: Zhexuan Gu
 * @Date: 2022-10-12 12:53:26
 * @LastEditTime: 2022-10-12 15:14:09
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Search/test.cpp
 * @Description: Please implement
 */
#include "BinarySearch.h"
#include "BinarySearch.cpp"
#include "HashTable.h"
#include "HashTable.cpp"
#include "../Sortings/DifferentSortAlgorithms.h"
#include "../Sortings/DifferentSortAlgorithms.cpp"

/*因为二分查找要求有序，所以如果拿到了无序数组的话就调用SortAlgorithms里的算法排序一下即可*/

using namespace std;
using namespace gzx_simple_search;
void test_bsearch()
{
    vector<int> arr{1, 2, 3, 4, 5, 23, 30, 90, 100, 888, 1011, 2333, 6666};
    size_t location;
    bool ans;
    ans = BinarySearch(arr, 23, 0, arr.size() - 1, location);
    cout << boolalpha << ans << "   location is:" << location << endl;
}

void test_hashtable()
{
    ContentNode* people1 = new ContentNode(4301, "John", "male", 18);
    ContentNode* people2 = new ContentNode(8601, "Amy", "female", 18);
    ContentNode* people3 = new ContentNode(4310, "Mike", "male", 18);
    ContentNode* people4 = new ContentNode(6669, "James", "male", 18);
    HashTable ht(10);       // capacity 为 43
    // insertion
    ht.InsertPeople(people1, ht.HashVal(people1));
    ht.InsertPeople(people2, ht.HashVal(people2));
    ht.InsertPeople(people3, ht.HashVal(people3));
    ht.InsertPeople(people4, ht.HashVal(people4));

    cout << "\n";
    // search
    ContentNode people = ht.Search(8601);
    cout << "Hello, My name is " << people.name << ", I'm " << people.age << " years old.\n";
    cout << "Sex: " << people.sex << " --------   ID:" << people.key << endl; 
    cout << "\n";
    // delete
    ht.Delete(4301);
    ContentNode temp = ht.Search(4301);
    if(temp.key == 0)
        cout << "No Result" << endl;
}

int main()
{
    cout << "---------- testing Binary Search ----------" << endl;
    test_bsearch();
    cout << "---------- testing Hash Table ----------" << endl;
    test_hashtable();
    return 0;
}