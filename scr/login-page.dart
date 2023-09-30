

class MainLogin extends StatelessWidget {
  const MainLogin({super.key});

  @override
  Widget build(BuildContext context) {

    String userInputLogin = '';
    String userInputPassword = '';
    List listUsers = [];

    return Scaffold(
      // основное тело
      body: Center(
        // рамка
        child: Container(
          // параметры рамки
          padding: EdgeInsets.all(18.0),
            decoration: BoxDecoration(
              border: Border.all(
                color: Colors.black,
                width: 10.0,
              ),
            ),

          // дочерний обьект 
          child: Column(
            // ценрирование 
            mainAxisAlignment: MainAxisAlignment.center,
            children:[
              Image.asset(
                // Подключаем по желанию картинку
              ),
              // строка с логином
              TextField(
                onChanged: (value){
                  userInputLogin = value;
                },
                ),
              // строка с паролем
              TextField(
                onChanged: (value){
                  userInputPassword = value;
                },
                obscureText: true,
                ),

              // кнопка авторизации
              ElevatedButton(
                // при нажатии проверить строку и перейти
                onPressed: (){
                  if (listUsers.contains('$userInputLogin-$userInputPassword')){
                    // Переход на домашний экран при нажатии на кнопку
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => HomePage()),
                    );
                  } else{
                    // иначе показать диалоговое окно
                    showDialog(context: context, builder: (BuildContext context){
                      return AlertDialog(
                        // отображаемый текст
                        title: Text('Неверный логин или пароль. Попробуйте снова!'),
                        actions: [
                          // конка "OK", которая закрывает диалоговое окно
                          FloatingActionButton(
                            // цвет кнопки
                            backgroundColor: Colors.black,
                            child: Text('Ok'),
                            onPressed: () {
                              Navigator.of(context).pop();
                            },
                          ),
                        ],
                      );
                    });
                  }

                },
                child: const Text('Войти'),
              ),

              // кнока входа для гостя
              ElevatedButton(
                onPressed: () {
                  // Переход на домашний экран при нажатии на кнопку
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => HomePage()),
                    );
                },
                child: const Text('Войти как гость'),
              ),
            ]
          ),
        ),
      )
    );
  }
}