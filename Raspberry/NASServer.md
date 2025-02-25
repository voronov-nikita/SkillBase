# Домашний NAS сервер

## Содержание

1. [Введение](./NASServer.md#введение)
2. [Используемые материалы и инструменты](./NASServer.md#используемые-материалы-и-инструменты)
3. [Готовая реализация](./NASServer.md#готовая-реализация)
4. [Полезные ссылки](./NASServer.md#полезные-ссылки)

## Введение

В современном мире никого уже не удивит, что на телефоне есть несколько сотен гигабайт свободного места, а на компьютерах несколько терабайт.
Но что делать, если у вас есть большое количество файлов, которые необходимо хранить и использовать сразу на нескольких устройствах?
В голову сразу приходит покупка отдельного облачного сервиса, но современные облака стоят довольно дорого.

Почему бы не создать собственное облако с возможностью доступа к файлам из любой точки мира, 
а позже и расширением до большего количества файлов?
Звучит сложно, но это нет так. Raspberry поможет в реализации данной задачи.

## Используемые материалы и инструменты

Для реализации данной задачи нам понадобится следующее компоненты, знания и понимания:

1. **Raspberry Pi**: 
    Подойдет любая модель, но для наилучшей работы стоит выбирать Raspberry с наибольшим 
    количеством ОЗУ (от 2 GB), а так же с быстрым процессором. 
    В этой статье будет использоваться Raspberry Pi 3B+ с 2 Gb ОЗУ и 4-х ядерным процессором.
2. **Ethernet или Wifi соединение**: 
    Как ни странно необходимо иметь сетевое подключение с выходом в интернет, 
    но в случае, если использование будет ограничено локальной сетью, то можно обойтись без доступа, непосредственно, в глобальную сеть.
3. **Базовые знания и понимание Linux систем и работы с терминалом**:
    В проекте используется операционная система от компании Raspberry - *Raspberry OS Lite*, 
    следовательно это Linux система без графической оболочки.
    Подключение к Raspberry осуществляется по средствам удаленного терминала **SSH**.
4. **Понимание принципа работы сетей. Умение "пробрасывать" порты**:
   Есть несколько способов получения доступа к локальным ресурсам. Одном из самых простых является понимание принципа построение TCP/IP сетей с использованием технологии удаленного администрирования SSH.

## Готовая реализация

Проект с готовой реализацией можно посмотреть по [ссылке](https://github.com/voronov-nikita/NAS-platform).

В репозитории описаны все моменты, сложности, ошибки и решения для них при реализации проекта.

> [!NOTE]
> На самом деле проект NAS-platform нацелен на другое. А конкретно на написание WEB сервиса для удаленного доступа к файлам на домашнем NAS сервере.
>
> В лучшем случае, все что можно узнать оттуда полезного, так это то, как пробросить порты, настроить DDNS и DHCP серверы на своем, даже самом стареньком роутере, привязанном к определенным операторам без покупки дорогостоящих услуг (о предоставлении постоянного IP адреса, к примеру).

## Полезные ссылки

1. [raspberrypi.com](https://www.raspberrypi.com/)
2. [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
3. [Основы Linux (обзор с практическим уклоном) - habr.com](https://habr.com/ru/articles/655275/)
4. [Учебное пособие по Linux/Unix - geeksforgeeks.org](https://www.geeksforgeeks.org/linux-tutorial/)
5. [Знакомство с SSH - habr.com](https://habr.com/ru/articles/802179/)
6. [Сетевые хранилища NAS: зачем нужны и как выбрать подходящее? - habr.com](https://habr.com/ru/companies/seagate/articles/538336/)
7. [Файл-сервер на Raspberry Pi как домашний NAS - habr.com](https://habr.com/ru/companies/first/articles/592307/)
8. [How to build a Raspberry Pi NAS - raspberrypi.com](https://www.raspberrypi.com/tutorials/nas-box-raspberry-pi-tutorial/)
9. [Личный сервер дома: собираем полноценный NAS на базе Raspberry Pi - trashbox.ru](https://trashbox.ru/link/nas-via-raspberry-pi)


<br><br>
<br><br>

###### 30.11.2024
