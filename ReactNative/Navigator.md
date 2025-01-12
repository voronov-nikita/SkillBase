# Код стандартной навигации с помощью объектов navigation.navigate

## Установка

```bash
npm install @react-navigation/native @react-navigation/stack
```


## Использование

```js

import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import React from "react";

import { AuthScreen } from "./AuthPage";
import { HomeScreen } from "./HomePage";

// создаем экхемпляр объекта навигатора состояний
const Stack = createStackNavigator();

// обрабатываем первичный запрос пользователя
// По умолчанию откроются данные для ввода логина и пароля
const AppNavigator = () => {
    return (
        <NavigationContainer>
            <Stack.Navigator
                initialRouteName="Auth"
                screenOptions={{
                    headerStyle: {
                        backgroundColor: "#000",
                        color: "#fff",
                    },
                }}
            >
                <Stack.Screen
                    name="Auth"
                    component={AuthScreen}
                    options={{ headerShown: false }}
                />

                <Stack.Screen
                    name="Home"
                    component={HomeScreen}
                />
            </Stack.Navigator>
        </NavigationContainer>
    );
};

```

<br><br>
<br><br>

###### 12.01.2025