

#ifndef _HASHTABLE_CPP_J
#define _HASHTABLE_CPP_J

#include "HashTable.h"

/*
仅仅为了模拟课上的内容
有很多不完善的地方，可以去看看一些C++ STL源码的实现等，会足够细致
*/

namespace gzx_simple_search{
    HashTable::HashTable(int primek)
    {
        capacity = 4 * primek + 3;
        vec.resize(capacity);
        for(size_t i = 0 ; i < capacity ; i ++)
        {
            vec[i].age = 0;
            vec[i].key = 0;
            vec[i].name = "";
            vec[i].sex = "";
            vec[i].deleted = false;
        }
    }

    size_t HashTable::HashVal(ContentNode* people)
    {
        return people->key % capacity;
    }

    bool HashTable::InsertPeople(ContentNode* people, size_t hashval)
    {
        bool hasempty = false;
        for(size_t i = hashval ; i < capacity ; i ++)
        {
            if(vec[i].key == 0){ // means null
                if(hashval != i)
                    cout << "Hash Colision, I'm moving forward to " << i;
                else
                    cout << "No colision, hashval is " << i;
                cout << endl;
                vec[i].age = people->age;
                vec[i].key = people->key;
                vec[i].name = people->name;
                vec[i].sex = people->sex;
                hasempty = true;
                break;
            }
        }
        return hasempty;
    }

    ContentNode HashTable::Search(size_t key)
    {
        ContentNode temp;
        size_t hashVal = key % capacity;
        for(size_t i = hashVal ; i < capacity ; i ++)
        {
            if(vec[i].key == 0 && vec[i].deleted == false)
                break;
            if(vec[i].key == key){
                temp = vec[i];
                break;
            }
        }
        return temp;
    }

    bool HashTable::Delete(size_t key)
    {
        bool ans = false;
        size_t hashVal = key % capacity;
        for(size_t i = hashVal ; i < capacity ; i ++)
        {
            if(vec[i].key == key){
                vec[i].age = 0;
                vec[i].deleted = true;
                vec[i].key = 0;
                vec[i].sex = "";
                vec[i].name = "";
                ans = true;
                break;
            }
        }
        return ans;
    }
}

#endif