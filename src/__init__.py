"""Реализация API для онлайн-калькулятора.

API предоставляет доступ к алгоритмам. Получить список имеющихся алгоритмов
можно посредством выполнения GET запроса к конечной точке /api/algorithms.
Ответ содержит экземпляр класса Algorithms.

Доступ к конкретному алгоритму осуществляется по URI
/api/algorithms/{algorithm_name}, с указанием уникального имени алгоритма.
Получить описание выбранного алгоритма можно посредством выполнения GET
запроса к конечной точке /api/algorithms/{algorithm_name}. Ответ содержит
экземпляр класса AnswerAlgorithmDefinition.

Получить результат выполнения алгоритма можно посредством выполнения POST
запроса к конечной точке /api/algorithms/{algorithm_name}, с передачей
фактических значений для набора входных параметров - с помощью объекта
класса Parameters. Ответ содержит экземпляр класса AnswerOutputs.

Получить версию сборки серверной части онлайн-калькулятора можно посредством
выполнения GET запроса к конечной точке /api/backend_version.
Ответ содержит строку с названием версии.

+--------+---------------------------+---------------------------------------+
| Запрос | Конечная точка            | Действие                              |
+========+===========================+=======================================+
| GET    | /api/algorithms           | Получить список имеющихся алгоритмов  |
+--------+---------------------------+---------------------------------------+
| GET    | /api/algorithms/fibonacci | Получить описание алгоритма fibonacci |
+--------+---------------------------+---------------------------------------+
| POST   | /api/algorithms/fibonacci | Выполнить алгоритм fibonacci          |
+--------+---------------------------+---------------------------------------+
| GET    | /api/backend_version      | Получить версию сборки                |
+--------+---------------------------+---------------------------------------+

"""

APP_CONFIG_FILE_PATH = 'config/app_config.json'
"""Путь к конфигурации приложения"""

LOG_CONFIG_FILE_PATH = 'config/log_config.json'
"""Путь к конфигурации логирования"""

PATH_CONFIG = 'path_config'
"""Ключ для раздела конфигурации, содержащего пути к файлам для алгоритмов"""

ALGORITHM_CONFIG = 'algorithm_config'
"""Ключ для раздела конфигурации с настройками для алгоритмов"""

IS_TEST_APP = 'IS_TEST_APP'
"""Переменная среды, свидетельствующая о проведении тестировании модуля main"""

EXECUTE_TIMEOUT = 'execute_timeout'
"""Ключ в конфигурации алгоритмов для задания времени выполнения алгоритма"""

ALGORITHMS_ENDPOINT = '/api/algorithms'
"""Конечная точка для API"""

BACKEND_VERSION_ENDPOINT = '/api/backend_version'
"""Конечная точка API для получения версии сборки серверной части"""

TIME_OVER_MSG = 'Время для выполнения алгоритма истекло'
"""Сообщение об ошибке таймаута"""
