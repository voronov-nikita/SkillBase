# Реализация структуры стека на C++

> [!NOTE]
> Использование ветвления через структуры может быть нецелесообразным,
>
> поэтому было принято решение реализовать стек исключительно используя указатели и динамическое управление памятью


```cpp

#include <iostream>

class Stack {

public:

    Stack()
    {
        this->next = nullptr;
        this->top = 0;

    }

    // Конструктор для нового элемента
    Stack(int val, Stack* nextStack) : top(val), next(nextStack) {}

    // Добавление элемента в стек
    Stack* add(int val) {
        // создаем новый элемент, указывающий на текущий стек
        return new Stack(val, this);
    }

    // Удаление элемента из стека
    Stack* del() {
        if (next == nullptr) {
            return this; // возвращаем тот же стек, если он пуст
        }
        
        Stack* nextStack = next;
        delete this;
        return nextStack;
    }

    // Получение верхнего элемента стека
    int getTop() const {
        if (next == nullptr) {
            return -1;
        }
        return top;
    }

    // Проверка пустоты стека
    bool isEmpty() {
        return next == nullptr;
    }

    // Очистка стека
    Stack* clear() {
        Stack* tempStack = this;
        while (!tempStack->isEmpty()) {
            tempStack = tempStack->del();
        }
        return tempStack;
    }

    // Печать стека
    void printStack() const {
        const Stack* tempStack = this;

        while (tempStack->next != nullptr) {
            std::cout << tempStack->top << " ";
            tempStack = tempStack->next;
        }
        std::cout << std::endl;
    }

private:
    int top;
    Stack* next;
};


int main() {
    Stack* stack = new Stack();

    stack = stack->add(5);
    stack->printStack();

    stack = stack->add(10);
    stack->printStack();

    stack = stack->add(15);
    stack->printStack();

    return 0;
}

```

<br><br>
<br><br>

###### 16.12.2024