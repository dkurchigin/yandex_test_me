import re
import json
import random
from collections import defaultdict

# 1 Напишите регулярное выражение, с помощью которого из URL можно
# извлечь его домен. Для проверки вашего регулярного выражения
# будет использован следующий файл с URL-адресами:

urls = [
    'http://falloutboy.com/',
    'http://xn----7sbajjbec0dd3k7b.xn--p1ai/vse_serii_podryad/multiki',
    'http://www.adobe.com/ru/',
    'http://www.mamba.ru/en/',
    'http://lurkmore.to/%D0%90%D0%BA%D1%83%D0%BD%D0%B8%D0%BD',
    'https://ru.bongacams.com/',
    'http://user@example.com',
    'https://en.wikipedia.org/wiki/Java_version_history',
    'http://rutor.info/',
    'https://www.youtube.com/user/momondo',
    'http://totori.ru/bezdomnyj-bog-2-sezon-12-seriya',
    'http://xn-----7kcabbec2afz1as3apmjtgqh4hrf.xn--p1ai/dlya-komyutera/viber-dlya-windows-7',
    'http://lurkmore.to/%D0%90%D0%BA%D1%83%D0%BD%D0%B8%D0%BD',
    'http://www.povarenok.ru/recipes/show/42046/',
    'http://blog.t-stile.info/v-vashem-aktive-net-inostrannyx-yazykov-ne-kruchintes',
    'http://www.bibo.kz/aforizmi/393836--chto-pervichno-jajjco-ili-kurica-.html',
    'https://yandex.ru/search/?lr=2&clid=2233330&win=195&msid=1485784820.7601.20943.16306&text=самый%20первый%20фильм%20в%20мире&example_source=all&nl=1',
    'http://lib.mexmat.ru:80/books/90359',
]


# REGEXP -> http[s]?:\/{2}(.*@|.*\.)?(.*\..*?(com|ru|info|to|kz|org|xn--p1ai))
# DOMAIN in 2 group
def get_domain(urls):
    domain_pattern = 'http[s]?:\/{2}(.*@|.*\.)?(.*\..*?(com|ru|info|to|kz|org|xn--p1ai))'

    for url in urls:
        matched_domain = re.match(domain_pattern, url)
        if matched_domain:
            print(f'Домен: {matched_domain[2]}')


get_domain(urls)


# 2. Задача — написать скрипт, который будет обрабатывать данный файл в
# формате json (https://yadi.sk/d/np2eKmoM3Zx8rB). Скрипт должен
# сгруппировать покупки по магазинам, в которых они были сделаны. В
# результате должен получиться массив, состоящий из трех элементов.
# Внутри каждого элемента содержатся название магазина и все
# покупки, совершенные в нем. Задачу необходимо решить на Python.


FILE = 'task_2.json'
with open(FILE, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

shops = defaultdict(list)
for element in data:
    shops[element['shop']].append(element['product'])
print(dict(shops))


# 3 Дан массив из n целых чисел. Нужно выбрать n-1 чисел так, чтобы их
# произведение было максимальным среди всех возможных n-1
# наборов.


def remove_min_multiplication_of_numbers(array):
    mult_min_values = []

    for first_n_index, first_n in enumerate(array):
        for second_n_index, second_n in enumerate(array):
            if first_n_index != second_n_index:
                try:
                    if mult_min_values[first_n_index] < first_n * second_n:
                        mult_min_values[first_n_index] = first_n * second_n
                except IndexError:
                    mult_min_values.append(first_n * second_n)

    min_element_index = mult_min_values.index(min(mult_min_values))
    array.pop(min_element_index)

    return array


SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
ARRAY = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(ARRAY)
result_ = remove_min_multiplication_of_numbers(ARRAY)
print(result_)


# 4. Есть два сортированных списка (массива). Нужно написать функцию,
# которая делает новый сортированный список с пересечением
# элементов этих двух списков.
# Пример:
# 1-ый список: 1, 2, 2, 5, 7, 14
# 2-й список: 4, 6, 6, 7, 9, 14, 15
# Пересечение: 7, 14

first_list = [1, 2, 2, 5, 7, 14]
second_list = [4, 6, 6, 7, 9, 14, 15]


def get_intersection_elements(first, second):
    return sorted(list(set(first) & set(second)))


print(get_intersection_elements(first_list, second_list))


# 5 Есть две таблицы:
# orders (order_id, promocode_id) - заказы
# promocodes (promocode_id, name, discount) - промокоды
# Вопросы:
# Какая доля заказов с промокодами?
# Какой самый популярный промокод (название) и число его
# использований?

# select count(*)*100/(select count(*) from orders) from orders where promocode_id;

# select name, count(orders.promocode_id) as promo_count from orders
# inner join promocodes on orders.promocode_id = promocodes.promocode_id group by promocodes.promocode_id
# order by promo_count desc limit 1;
