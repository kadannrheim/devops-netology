# Домашнее задание к занятию "5.5. Оркестрация кластером Docker контейнеров на примере Docker Swarm"

## Как сдавать задания

Обязательными к выполнению являются задачи без указания звездочки. Их выполнение необходимо для получения зачета и диплома о профессиональной переподготовке.

Задачи со звездочкой (*) являются дополнительными задачами и/или задачами повышенной сложности. Они не являются обязательными к выполнению, но помогут вам глубже понять тему.

Домашнее задание выполните в файле readme.md в github репозитории. В личном кабинете отправьте на проверку ссылку на .md-файл в вашем репозитории.

Любые вопросы по решению задач задавайте в чате учебной группы.

---

## Задача 1

Дайте письменые ответы на следующие вопросы:

1 - В чём отличие режимов работы сервисов в Docker Swarm кластере: replication и global?
2 - Какой алгоритм выбора лидера используется в Docker Swarm кластере?
3 - Что такое Overlay Network?
## Решение задачи 1
1. Replication - для разворачивания сервисов идентичных задач, подходит для известного количества сервисов (nginx, apache)
   Global - для сервиса в единственном экземпляре в каждой ноде, подходит для однотипных задач (zabbix, smtp).
2. Raft — это протокол для реализации распределенного консенсуса. Три состояния Follower, Candidate, Leader. По умолчанию все Follower, но если нет отклика от лидера они могут получить статус Candidate. Все ноды голосуют за какую то одну и она становистся новым лидером. ПРи условии что есть кворум (доступность более половины нод).
3. Overlay Network - это вируальная сеть построенная на основе уже существующей (vlan, openvpn, wireguard). В данном случае применимо к docker она позволяет общаться контейнерам между собой.
## Задача 2

Создать ваш первый Docker Swarm кластер в Яндекс.Облаке

Для получения зачета, вам необходимо предоставить скриншот из терминала (консоли), с выводом команды:
```
docker node ls
```
https://github.com/kadannrheim/devops-netology/blob/c2d615753734989ed8315a29057f524bbe5008fe/home-work/virt-homeworks/screenshots/05-virt-05-docker-swarm2.png
## Задача 3

Создать ваш первый, готовый к боевой эксплуатации кластер мониторинга, состоящий из стека микросервисов.

Для получения зачета, вам необходимо предоставить скриншот из терминала (консоли), с выводом команды:
```
docker service ls
```
https://github.com/kadannrheim/devops-netology/blob/c2d615753734989ed8315a29057f524bbe5008fe/home-work/virt-homeworks/screenshots/05-virt-05-docker-swarm3.png
## Задача 4 (*)

Выполнить на лидере Docker Swarm кластера команду (указанную ниже) и дать письменное описание её функционала, что она делает и зачем она нужна:
```
# см.документацию: https://docs.docker.com/engine/swarm/swarm_manager_locking/
docker swarm update --autolock=true
```
Данная команда включает блокировку Swarm менеджера против неразрешенного доступа к Raft логу. На каждую ноду menedger загружаются ключи дешифрования и шефрования, что позволяет шифровать сообщения.
https://github.com/kadannrheim/devops-netology/blob/c2d615753734989ed8315a29057f524bbe5008fe/home-work/virt-homeworks/screenshots/05-virt-05-docker-swarm4.png