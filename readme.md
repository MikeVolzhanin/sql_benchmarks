<h1 align="center">Python SQL Libraries Benchmark</h1>
<p>Данная лабораторная работа направлена на разработку бенчмарков для измерения скорости выполнения четырех 
различных SQL-запросов, используя пять библиотек для работы с базами данных на Python. Для обеспечения достоверности 
результатов предполагается провести более 10 запусков для каждого запроса, с последующим использованием
медианного значения в качестве результата. Этот подход позволит учесть возможные колебания в 
производительности и обеспечит более точную оценку скорости выполнения запросов.</p>

<h4>Используемы запросы в работе:</h4>
 <p><b>1) SELECT VendorID, count(*) FROM yellow_taxi GROUP BY 1</b></p>
 <p>2) <b>SELECT passenger_count, avg(total_amount) FROM yellow_taxi GROUP BY 1</b></p>
 <p>3) <b>SELECT passenger_count, extract(year from tpep_pickup_datetime::timestamp) AS pickup_year ,COUNT(*)
FROM yellow_taxi GROUP BY passenger_count, pickup_year</b></p>
 <p>4) <b>SELECT passenger_count,extract(year from tpep_pickup_datetime::timestamp) AS pickup_year, round(trip_distance),
count(*) FROM yellow_taxi GROUP BY 1, 2, 3 ORDER BY 2, 4</b></p>

<h3 align="center">Что необходимо сделать, чтобы запустить проект?</h3>
<p>1) Склонируйте репозиторий с данным проектом</p>
<p>2) Загрузите с диска датасеты необходимые для работы проекта и поместите их в папку "datasets"(https://disk.yandex.ru/d/WSAK3ucfZpTaKA)</p>
<p>3) Чтобы работал бенчмарк для библиотеки psycopg2, необходимо загрузить датасет в postgresql и указать 
обязательные данные для подключения к БД в файле "src/benchmark_psycopg2.py".<p>
<div align="center"><img src="images/psycopg2.png" width="280"></div>
<p>4) Теперь можно приступить к запуску проекта, для этого запустите файл <b>start.bat</b> и введите 
без пробелов номера тех библиотек, которые хотите протестировать. (Например: 12 или 1)</p>
<div align="center"><img src="images/menu.png" width="400"></div>

<h3 align="center">Отчёт о работе 5 библиотек на 4 запросах<h3>
