# Цветные log-и с помощью ccze

* `sudo apt-get install ccze -y` -установка
* `ccze -l` -вывести список доступных плагинов выполните
* `tail -f /var/log/syslog | ccze -A` -вывод последних 10 строк логов в живом редиме (-f) с помощью подсветки ccze