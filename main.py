import requests
import json
import time
from colorama import Fore, Style, init

# Инициализация colorama для цветного вывода
init(autoreset=True)

# Загрузка конфигурации из config.json с указанием кодировки utf-8
def load_config():
    with open('config.json', 'r', encoding='utf-8') as config_file:
        config = json.load(config_file)
    return config

# Функция для определения типа прокси
def get_proxy_type(ip):
    try:
        response = requests.get(f'http://ipinfo.io/{ip}/json')
        data = response.json()
        if 'ipv6' in data:
            return 'IPv6'
        else:
            return 'IPv4'
    except Exception:
        return 'Unknown'

# Функция для проверки прокси
def check_proxy(proxy, proxy_format):
    try:
        proxy_dict = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}",
        }

        start_time = time.time()
        response = requests.get('http://ipinfo.io/json', proxies=proxy_dict, timeout=5)
        elapsed_time = time.time() - start_time

        if response.status_code == 200:
            data = response.json()
            country = data.get('country', 'Unknown')
            city = data.get('city', 'Unknown')
            proxy_ip = data.get('ip', 'Unknown')
            proxy_type = get_proxy_type(proxy_ip)  # Определяем тип прокси
            
            return (True, proxy, country, city, elapsed_time, proxy_type)
        else:
            return (False, proxy)
    except requests.RequestException:
        return (False, proxy)

# Чтение списка прокси из файла и их проверка
def check_proxies_from_file(file_path, proxy_format):
    with open(file_path, 'r') as file:
        proxies = file.readlines()

    results = []
    for proxy in proxies:
        proxy = proxy.strip()  # Убираем лишние пробелы и переносы строк
        if proxy:
            result = check_proxy(proxy, proxy_format)
            results.append(result)
    return results

# Сохранение результатов в файлы
def save_results(results):
    valid_proxies = []
    invalid_proxies = []

    for result in results:
        if result[0]:
            valid_proxies.append(result[1])
        else:
            invalid_proxies.append(result[1])

    with open('valid_proxies.txt', 'w') as valid_file:
        valid_file.write('\n'.join(valid_proxies))
    
    with open('invalid_proxies.txt', 'w') as invalid_file:
        invalid_file.write('\n'.join(invalid_proxies))

# Вывод результатов
def print_results(results):
    print("\n" + Fore.YELLOW + Style.BRIGHT + "Результаты проверки прокси:\n")
    for result in results:
        if result[0]:
            print(f"{Fore.GREEN}[+] Valid Proxy: {result[1]}")
            print(f"{Fore.GREEN}[+] GEO: {result[2]}, {result[3]}")
            print(f"{Fore.GREEN}[+] Response Time: {result[4]:.2f} seconds")
            print(f"{Fore.GREEN}[+] Proxy Type: {result[5]}\n")
        else:
            print(f"{Fore.RED}[-] Invalid Proxy: {result[1]}\n")

# Основная часть программы
if __name__ == "__main__":
    print("Добро пожаловать в Proxy Checker!")
    config = load_config()  # Загружаем конфигурацию
    proxy_format = config['proxy_format']  # Получаем формат прокси из конфигурации

    # Запрашиваем у пользователя путь к файлу с прокси
    file_path = input("Введите путь к файлу с прокси (по умолчанию 'proxy.txt'): ") or 'proxy.txt'
    
    print(f"Проверяем прокси из файла: {file_path}...\n")
    
    results = check_proxies_from_file(file_path, proxy_format)  # Проверяем прокси
    print_results(results)  # Выводим результаты
    save_results(results)  # Сохраняем результаты в файлы
