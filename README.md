# Прокси Чекер

## Описание

Прокси Чекер — это инструмент для проверки работоспособности прокси-серверов. Он написан на Python с использованием библиотек `requests`, `BeautifulSoup` и `colorama`. Этот проект позволяет быстро и удобно проверять валидность прокси и сохранять результаты в отдельные файлы.

## Основные особенности

- **Язык:** Python 3.10
- **Библиотеки:** `requests`, `BeautifulSoup`, `colorama`
- **Формат прокси:** Поддержка форматов `host:port` и `login:password@host:port`
- **Мультипоточность:** Поддержка многопоточной проверки прокси для ускорения процесса.
- **Геолокация:** Определение страны и города прокси.
- **Отчетность:** Все валидные прокси сохраняются в файл `valid_proxy.txt`, а невалидные — в `invalid_proxy.txt`.
- **Настройка через `config.json`:** Удобное управление настройками без необходимости редактировать код.

## Установка

1. **Установите Python:**
   - Перейдите на [официальный сайт Python](https://www.python.org/downloads/) и скачайте версию 3.10.
   - Убедитесь, что вы выбрали опцию "Add Python to PATH" при установке.

2. **Скачивание и настройка чекера:**
   - Скачайте архив с прокси чекером и распакуйте его.
   - Откройте файл `config.json` и настройте формат прокси и количество потоков.

   Пример файла `config.json`:
   ```json
   {
       "proxy_format": "host:port",
       "threads": 10
   }
