# WEB авторизация с учетом локального хранения cookies


```js

// Страница авторизации пользователей
//

import React, { useState, useEffect } from 'react';
import {
	View,
	Text,
	SafeAreaView,
	StyleSheet,
	TextInput,
	TouchableOpacity,
	Dimensions,
} from 'react-native';
import { MaterialCommunityIcons } from '@expo/vector-icons';

// импорт констант из файла с конфигурациями
import { URL } from '../config';

// Экспортируемый экран авторизации
export const AuthScreen = ({ navigation }) => {
	const { width } = Dimensions.get('window');
	// Ширина основного блока в зависимости от ширины экрана
	const mainBlockWidth = width < 400 ? '85%' : '34%';

	// Состояния для управления вводом и авторизацией
	const [message, setMessage] = useState('ВВЕДИТЕ ЛОГИН И ПАРОЛЬ');
	const [login, setLogin] = useState('');
	const [password, setPassword] = useState('');
	const [showPassword, setShowPassword] = useState(false);
	const [isAuthenticated, setIsAuthenticated] = useState(false);

	// Проверка сохранённой сессии при монтировании
	useEffect(() => {
		const token = localStorage.getItem('authToken');
		const expiresAt = localStorage.getItem('expiresAt');

		if (token && expiresAt && Date.now() < expiresAt) {
			setIsAuthenticated(true);
			navigation.navigate('Home'); // Перенаправляем на главную страницу
		} else {
			localStorage.removeItem('authToken');
			localStorage.removeItem('expiresAt');
		}
	}, []);

	// Функция обновления токена (пример)
	const refreshAuthToken = async () => {
		try {
			const response = await fetch(`${URL}/refresh`, {
				method: 'POST',
				credentials: 'include', // Передача cookie для refresh
			});
			const data = await response.json();
			const { access, expiresIn } = data;

			if (access) {
				const expiresAt = Date.now() + expiresIn * 1000;
				localStorage.setItem('authToken', access);
				localStorage.setItem('expiresAt', expiresAt);
				setIsAuthenticated(true);
			}
		} catch (error) {
			console.error('Ошибка обновления токена:', error);
		}
	};

	// Авторизация пользователя
	const sendDataToServerAuth = async () => {
		if (login !== '' || password !== '') {
			try {
				// формирование POST запроса на сервер с постфиксом auth
				const response = await fetch(`${URL}/auth`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        login: 'admin',
                        password: 'admin',
                    }),
                    credentials: 'include',
                });

				// Проверка кода статуса ответа
				if (response.ok) {
					const data = await response.json();
					const { access, refresh, expiresIn } = data;

					if (access) {
						const expiresAt = Date.now() + expiresIn * 1000;
						localStorage.setItem('authToken', access);
						localStorage.setItem('expiresAt', expiresAt);
						console.log('Access token сохранён:', access);
						console.log('Refresh token получен и хранится в куках автоматически');

						setIsAuthenticated(true);
						navigation.navigate('Home');
					}
				} else {
					// Обработка различных кодов ошибок
					switch (response.status) {
						case 401:
							setMessage('Неверный логин или пароль');
							break;
						case 500:
							setMessage('Ошибка сервера, попробуйте позже');
							break;
						default:
							console.log(response.status);
							setMessage('Произошла неизвестная ошибка, попробуйте позже');
							break;
					}
				}
			} catch (error) {
				console.error('Ошибка при авторизации:', error);
				setMessage('Не удалось подключиться к серверу. Попробуйте позже.');
			}
		} else {
			setMessage('Поля логина и пароля не могут быть пустыми');
		}

		// Очистка полей после попытки авторизации
		setLogin('');
		setPassword('');
	};

	// Интерфейс страницы
	return (
		<SafeAreaView style={styles.container}>
			<View style={[styles.mainBlock, { width: mainBlockWidth }]}>
				<Text style={styles.topText}>{message}</Text>

				<View style={styles.blockTextInput}>
					<TextInput
						style={styles.textInput}
						placeholder="Логин или почта:"
						autoFocus={true}
						onChangeText={login => setLogin(login)}
						value={login}
					/>
				</View>

				<View style={styles.blockTextInput}>
					<TextInput
						secureTextEntry={!showPassword}
						style={styles.textInput}
						placeholder="Пароль:"
						onChangeText={passw => setPassword(passw)}
						value={password}
					/>

					<MaterialCommunityIcons
						name={showPassword ? 'eye-off' : 'eye'}
						size={28}
						color="#aaa"
						style={styles.icon}
						onPress={() => setShowPassword(!showPassword)}
					/>
				</View>

				<TouchableOpacity style={styles.button.active} onPressOut={sendDataToServerAuth}>
					<Text style={styles.buttonText}>Войти</Text>
				</TouchableOpacity>

				<TouchableOpacity
					style={styles.button.inactive}
					onPressOut={() => {
						navigation.navigate('Reg');
					}}
				>
					<Text style={styles.buttonText}>Регистрация</Text>
				</TouchableOpacity>
			</View>
		</SafeAreaView>
	);
};

// Конструктор стилей для экрана авторизации
const styles = StyleSheet.create({
	container: {
		alignItems: 'center',
		alignContent: 'center',
		justifyContent: 'center',
		flex: 1,
		backgroundColor: '#21292c',
	},

	mainBlock: {
		flex: 1,
		alignContent: 'center',
		justifyContent: 'center',
	},

	blockTextInput: {
		flexDirection: 'row',
		alignItems: 'center',
		justifyContent: 'center',
		backgroundColor: '#f3f3f3',

		borderWidth: 0.5,
	},

	textInput: {
		justifyContent: 'center',
		margin: 'auto',
		padding: '7%',
		backgroundColor: '#f3f3f3',
		color: 'black',
		width: '100%',

		fontFamily: 'Arial',
	},

	icon: {
		marginRight: '5%',
	},

	button: {
		active: {
			width: '100%',
			height: '10%',
			backgroundColor: '#007bb7',
		},

		inactive: {
			width: '100%',
			height: '10%',
			backgroundColor: '#374e59',
		},
	},

	buttonText: {
		display: 'flex',
		justifyContent: 'center',
		textAlign: 'center',
		fontFamily: 'Arial',
		fontWeight: 'bold',
		margin: 'auto',

		color: '#e2e8e9',
		fontSize: '1.25rem',
	},

	topText: {
		textAlign: 'center',
		justifyContent: 'center',

		fontSize: '1.05rem',
		color: '#e2e8e9',
		margin: '5%',
		padding: 'auto',
		fontFamily: 'Arial',
	},
});

```


<br><br>
<br><br>

###### 12.01.2025