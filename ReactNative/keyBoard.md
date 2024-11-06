
# Компонент клавиатуры для входа в систему.


```javascript

import React, { useState, useEffect } from "react";
import { View, Text, TouchableOpacity, StyleSheet } from "react-native";

import CONFIG from "../config";

export const KeyBoardPin = ({ navigation }) => {
	const [pin, setPin] = useState("");
	const [textColor, setTextColor] = useState("#000");
	const [infoText, setInfo] = useState("Введите PIN-код для входа");

	useEffect(() => {
		if (pin.length === 4 && pin != "1234") {
			setInfo("Неверный PIN");
			setTextColor("#ff0000");
			handleClear();
		} else if (pin.length === 4 && pin == "1234") {
			setInfo("Добро пожаловать");
			setTextColor("#51b155");
			navigation.replace("Home");
		}
	}, [pin]);

	const handlePress = (num) => {
		if (pin.length < 4) {
			setPin((prev) => prev + num);
		}
	};

	const handleBackspace = () => {
		setPin((prev) => prev.slice(0, -1));
	};

	const handleClear = () => {
		setPin("");
	};

	const renderCircles = () => {
		return (
			<View style={styles.circlesContainer}>
				{Array(4)
					.fill("")
					.map((_, index) => (
						<View
							key={index}
							style={[styles.circle, pin.length > index && styles.filledCircle]}
						/>
					))}
			</View>
		);
	};

	return (
		<View style={styles.container}>
			<Text style={[styles.titleText, { color: textColor }]}>{infoText}</Text>

			{renderCircles()}
			<View style={styles.keyboard}>
				{["1", "2", "3", "4", "5", "6", "7", "8", "9"].map((num) => (
					<TouchableOpacity
						key={num}
						style={styles.key}
						onPress={() => handlePress(num)}
					>
						<Text style={styles.keyText}>{num}</Text>
					</TouchableOpacity>
				))}
				<TouchableOpacity style={styles.key} onPress={handleClear}>
					<Text style={styles.keyText}>✖</Text>
				</TouchableOpacity>
				<TouchableOpacity style={styles.key} onPress={() => handlePress("0")}>
					<Text style={styles.keyText}>0</Text>
				</TouchableOpacity>
				<TouchableOpacity style={styles.key} onPress={handleBackspace}>
					<Text style={styles.keyText}>⌫</Text>
				</TouchableOpacity>
			</View>
		</View>
	);
};

const styles = StyleSheet.create({
	container: {
		height: "80%",
		justifyContent: "center",
		alignItems: "center",
	},
	instruction: {
		fontSize: 18,
		marginBottom: 20,
	},
	circlesContainer: {
		flexDirection: "row",
		marginBottom: 30,
	},
	circle: {
		width: 20,
		height: 20,
		borderRadius: 10,
		borderWidth: 2,
		borderColor: "#333",
		margin: 10,
		backgroundColor: "transparent",
	},
	filledCircle: {
		backgroundColor: "#333",
	},
	keyboard: {
		flexDirection: "row",
		flexWrap: "wrap",
		width: 240,
		justifyContent: "center",
	},
	key: {
		width: 70,
		height: 70,
		justifyContent: "center",
		alignItems: "center",
		margin: 5,
		backgroundColor: "#ddd",
		borderRadius: 5,
	},
	keyText: {
		fontSize: 28,
		fontWeight: "bold",
	},
});

```