# Проект № 7: Возьмете Бэтмобиль?

[SF-DST] Car Price prediction part 2
Прогнозирование стоимости автомобиля по характеристикам

## Задача
	Создать нилучшую модель с использованием нейросетей для предсказывания стоимости автомобиля по его характеристикам.

## Описание выполнения работы
	Построили "наивную"/baseline модель, предсказывающую цену по модели и году выпуска 
	Обработаем и отнормируем признаки
	Сделаем первую модель на основе градиентного бустинга с помощью CatBoost
	Сделаем вторую модель на основе нейронных сетей и сравним результаты
	Сделаем multi-input нейронную сеть для анализа табличных данных и текста одновременно
	Добавим в multi-input сеть обработку изображений
	Осуществим ансамблирование градиентного бустинга и нейронной сети (усреднение их предсказаний)
