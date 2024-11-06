# Пример приложение ToDo листа

```javascript

import React, { useState } from "react";
import {
    SafeAreaView,
    StyleSheet,
    View,
    Text,
    TextInput,
    Button,
    FlatList,
    TouchableOpacity,
} from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";

const App = () => {
    const [task, setTask] = useState("");
    const [tasks, setTasks] = useState([]);

    const addTask = () => {
        if (task.length === 0) {
            return;
        }
        const newTask = {
            id: Date.now().toString(),
            text: task,
            completed: false,
        };
        setTasks([...tasks, newTask]);
        setTask("");
        storeTasks([...tasks, newTask]);
    };

    const toggleTask = (taskId) => {
        const updatedTasks = tasks.map((task) =>
            task.id === taskId ? { ...task, completed: !task.completed } : task
        );
        setTasks(updatedTasks);
        storeTasks(updatedTasks);
    };

    const storeTasks = async (tasks) => {
        try {
            await AsyncStorage.setItem("tasks", JSON.stringify(tasks));
        } catch (e) {
            console.error(e);
        }
    };

    const loadTasks = async () => {
        try {
            const tasks = await AsyncStorage.getItem("tasks");
            if (tasks !== null) {
                setTasks(JSON.parse(tasks));
            }
        } catch (e) {
            console.error(e);
        }
    };

    React.useEffect(() => {
        loadTasks();
    }, []);

    return (
        <SafeAreaView style={styles.container}>
            <View style={styles.inputContainer}>
                <TextInput
                    style={styles.input}
                    placeholder="Add a new task"
                    value={task}
                    onChangeText={setTask}
                />
                <Button title="Add" onPress={addTask} />
            </View>
            <FlatList
                data={tasks}
                renderItem={({ item }) => (
                    <TouchableOpacity onPress={() => toggleTask(item.id)}>
                        <View style={styles.taskContainer}>
                            <Text
                                style={
                                    item.completed
                                        ? styles.taskCompleted
                                        : styles.task
                                }
                            >
                                {item.text}
                            </Text>
                        </View>
                    </TouchableOpacity>
                )}
                keyExtractor={(item) => item.id}
            />
        </SafeAreaView>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: "#f5f5f5",
    },
    inputContainer: {
        flexDirection: "row",
        margin: 20,
    },
    input: {
        flex: 1,
        borderColor: "#333",
        borderWidth: 1,
        marginRight: 10,
        padding: 10,
        borderRadius: 5,
    },
    taskContainer: {
        padding: 20,
        borderBottomColor: "#ccc",
        borderBottomWidth: 1,
    },
    task: {
        fontSize: 18,
    },
    taskCompleted: {
        fontSize: 18,
        textDecorationLine: "line-through",
        color: "#999",
    },
});

export default App;

```