import pandas as pd

data = {
    'ім’я студента': ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро'],
    'середній бал': [4.8, 4.2, 4.6, 4.1, 4.3],
    'оцінка за іспит': [85, 75, 80, 70, 77],
    'кількість спроб здачі іспиту': [1, 2, 3, 2, 1]
}

df = pd.DataFrame(data)
print(df)

# Додавання нової колонки "Доступ студента до іспиту" за допомогою логічної операції
df['Доступ студента до іспиту'] = df['середній бал'] >= 4.5

print(df)
