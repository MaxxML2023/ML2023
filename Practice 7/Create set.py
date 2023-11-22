import pandas as pd
import numpy as np

# Функція для генерації синтетичних даних для мультикласової класифікації
def generate_multi_classification_data(num_samples):
    # Генерація випадкових оцінок для двох атрибутів (наприклад, дві оцінки студента)
    attribute1_grades = np.random.randint(0, 101, size=num_samples)  # Оцінка для атрибуту 1 (0-100)
    attribute2_grades = np.random.randint(0, 101, size=num_samples)  # Оцінка для атрибуту 2 (0-100)
    
    # Обчислення середнього значення для кожного запису
    average_grades = (attribute1_grades + attribute2_grades) / 2
    
    # Умови для класифікації: "низький", "середній", "високий"
    labels = np.where(average_grades < 60, 'низький', np.where(average_grades < 80, 'середній', 'високий'))
    
    # Створення DataFrame з атрибутами та мітками
    data = pd.DataFrame({'Attribute1': attribute1_grades, 'Attribute2': attribute2_grades, 'Label': labels})
    
    return data

# Генерація даних для мультикласової класифікації
multi_classification_data = generate_multi_classification_data(1000)  # 1000 записів у наборі даних

# Збереження створеного набору даних у CSV файл
multi_classification_data.to_csv('multi_classification_data.csv', index=False)
