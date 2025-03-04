import pandas as pd
import random

# Уникальные примеры задач и технологий
data = [
    ("Создание веб-сайта", ["HTML", "CSS", "JavaScript", "React", "Django"]),
    ("Разработка мобильного приложения", ["Kotlin", "Swift", "Flutter", "React Native"]),
    ("Анализ данных", ["Python", "R", "Pandas", "NumPy", "Matplotlib"]),
    ("Создание игры", ["C++", "C#", "Unity", "Unreal Engine", "Godot"]),
    ("Разработка бэкенда", ["Python", "Django", "Flask", "Node.js", "Java", "Spring"]),
    ("Разработка AI-моделей", ["Python", "TensorFlow", "PyTorch", "Scikit-learn", "Keras"]),
    ("Создание API", ["Flask", "FastAPI", "Django", "Node.js", "GraphQL"]),
    ("Разработка IoT-приложений", ["C", "C++", "MicroPython", "Rust", "Embedded C"]),
    ("Автоматизация процессов", ["Python", "Bash", "PowerShell", "Ansible", "Terraform"]),
    ("Разработка блокчейн-приложений", ["Solidity", "Rust", "Go", "Ethereum", "Hyperledger"])
]

# Генерация 300 уникальных записей
dataset = []
for _ in range(30):
    for task, languages in data:
        random.shuffle(languages)  # Перемешиваем технологии для разнообразия
        dataset.append((task, " ".join(languages)))

# Создание DataFrame и сохранение в CSV
columns = ["task", "languages"]
df = pd.DataFrame(dataset, columns=columns)
df.to_csv("dataset.csv", index=False, encoding="utf-8")

print("CSV-файл 'dataset.csv' успешно создан!")
