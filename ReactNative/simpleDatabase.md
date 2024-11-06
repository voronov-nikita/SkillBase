# Пример работы с базой данных SQLite в React Native

```javascript

//
// Логика локальной SQLite базы данных для хранения различного рода информации.
// В фале представлены функции, которые рекомендуется импортировать
// в страницы проекта и логических компонентов
//

import * as SQLite from "expo-sqlite";
import { CONFIG } from "../config";

// функция создания реляционной базы данных для содержания всех отображаемых счетов пользователя
export const createDatabaseBanks = async (initFunction, initFetch) => {
	const dbInstance = await SQLite.openDatabaseAsync(CONFIG.databaseName);
	initFunction(dbInstance);

	await dbInstance.execAsync(`
        CREATE TABLE IF NOT EXISTS banks (id INTEGER PRIMARY KEY AUTOINCREMENT, 
		title TEXT, 
		sum FLOAT,
		tag TEXT);
    `);

	initFetch(fetchDataBank(dbInstance));
};

// функция создания реляционной базы данных для содержания всех отображаемых целей по накоплениям пользователя
export const createDatabaseTargets = async (initFunction, initFetch) => {
	const dbInstance = await SQLite.openDatabaseAsync(CONFIG.databaseName);
	initFunction(dbInstance);

	await dbInstance.execAsync(`
        CREATE TABLE IF NOT EXISTS targets (id INTEGER PRIMARY KEY AUTOINCREMENT, 
		title TEXT, 
		curSum FLOAT,
		targetSum FLOAT,
		tag TEXT);
    `);

	initFetch(fetchDataTargets(dbInstance));
};

// выбор всех элементов из таблицы счетов
export const fetchDataBank = async (db) => {
	if (db) {
		const allRows = await db.getAllAsync("SELECT * FROM banks");
		return allRows;
	}
};

// выбор всех элементов из таблицы целей
export const fetchDataTargets = async (db) => {
	if (db) {
		const allRows = await db.getAllAsync("SELECT * FROM targets");
		return allRows;
	}
};

// добавить новый элемент в таблицу счетов
export const addNewBank = async (db, title, sum, tag) => {
	if (db && title && sum && tag) {
		await db.runAsync(
			"INSERT INTO banks (title, sum, tag) VALUES (?, ?, ?)",
			title,
			sum,
			tag
		);
	}
	return true;
};

// добавить новый элемент в таблицу целей
export const addNewTarget = async (db, title, curSum, targetSum, tag) => {
	if (db && title && targetSum && tag && curSum) {
		await db.runAsync(
			"INSERT INTO banks (title, curSum, targetSum, tag) VALUES (?, ?, ?, ?)",
			title,
			curSum,
			targetSum,
			tag
		);
	}
	return true;
};

```