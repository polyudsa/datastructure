#ifndef ArrayStack_H
#define ArrayStack_H
template <class T>
class ArrayStack{
    public:
        ArrayStack();
        ArrayStack(int n);
        ~ArrayStack();
        bool isEmpty();
        bool isFull();
        void push(T x);
        T top();
        T pop();
        int length();
        int size();
    private:
        T *data;
        int dlength;
        int dtop;
};
#endif