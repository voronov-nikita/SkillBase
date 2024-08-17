//
// Отправка всплывающего уведомления на экран.
// Используется для связи с пользователем.
//

import { Alert } from "react-native";
import React from "react";

export const showAlertNotification = (titleText, mainText) => {
	Alert.alert(
		titleText,
		mainText,
		[
			{
				text: "OK",
				onPress: () => console.log("Нажато OK"),
			},
		],
		{ cancelable: true }
	);
};