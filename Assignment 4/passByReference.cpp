#include <iostream>

void fun(int &a)
{ // this formal argument is the alias for actual argument
    a = a + 1;
}

int main()
{
    int a = 5;
    fun(a);
}