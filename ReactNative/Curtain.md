# Абстракция навигации через "шторку" (выпадающее меню)


## Установка


## Использование

```js

import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';

// Импорт страниц
import { NewScreen } from './pages/NewPage';
import { HomeScreen } from './pages/HomePage';
import { AuthScreen } from './pages/AuthPage';


// Создаем конфигуратор Drawer
const Drawer = createDrawerNavigator();

// Главная функция приложения
export default function App() {
	return (
		<NavigationContainer>
			<Drawer.Navigator
				initialRouteName="Auth"
				screenOptions={{
					drawerStyle: {
						backgroundColor: '#f0f0f0',
						width: 250,
					},
				}}
			>
				<Drawer.Screen
					name="Auth"
					component={AuthScreen}
				/>
                <Drawer.Screen
					name="Home"
					component={HomeScreen}
				/>
                <Drawer.Screen
					name="New"
					component={NewScreen}
				/>
			</Drawer.Navigator>
		</NavigationContainer>
	);
}

```

<br><br>
<br><br>

###### 12.01.2025