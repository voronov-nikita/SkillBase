import React from "react";
import { SafeAreaView, Text} from "react-native";


export const ToDoApp = () => {
    return (
        <SafeAreaView style={{flex:1, backgroundColor:"#ccc", justifyContent:"center"}}>
            <Text style={{textAlign: "center", backgroundColor: "#a1a1a1"}}>ToDo App                         </Text>
        </SafeAreaView>
    );
}