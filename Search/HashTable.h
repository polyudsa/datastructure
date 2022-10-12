/*
 * @author: Zhexuan Gu
 * @Date: 2022-10-12 12:52:34
 * @LastEditTime: 2022-10-12 14:58:55
 * @FilePath: /CPPprojects/PolyU_DSA_datastructure_database/Search/HashTable.h
 * @Description: Please implement
 */
#ifndef _HASHTABLE_H_J
#define _HASHTABLE_H_J

#include <iostream>
#include <vector>
using namespace std;

/*
这里不打算做很精细完美的HashTable 主要把ppt里的简单过一遍
因为一些高级的Hash算法太难我也做不出来。。。。Hash链式解决冲突，也不想做。。。
*/

namespace gzx_simple_search{
    // 以ppt中放进一个人物信息为例
    struct ContentNode{
        size_t key;            // 以身份证ID为例，没人ID是0
        string name;
        string sex;
        int age;
        bool deleted;          // 用于标记某个位置内容被删除，防止搜索的时候搜到此为止，明明没到数组尾却停止搜索了！
        ContentNode(size_t k = 0, string n = "", string s = "", int a = 0, bool de = false):key(k), name(n), sex(s), age(a), deleted(de){}
    };

    class HashTable{
        private:
            size_t capacity;
            vector<ContentNode> vec;
        public:
            HashTable(int primek);
            size_t HashVal(ContentNode* people);
            bool InsertPeople(ContentNode* people, size_t hashval);
            ContentNode Search(size_t key);
            bool Delete(size_t key);
    };
}

#endif