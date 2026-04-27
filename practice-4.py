# variant-D Top 10 Students Zhuldyz Smagul BDA-2506

import os
import csv
import json

# Task D1
print("Checking file...")

if not os.path.exists("students.csv"):
    print("Error: students.csv not found. Please download the file from LMS.")
else:
    print("File found: students.csv")

    print("")
    print("Checking output folder...")
    if not os.path.exists("output"):
        os.makedirs("output")
        print("Output folder created: output/")
    else:
        print("Output folder already exists: output/")

    # Task D2 - Чтение данных из CSV
    students = []
    # Используем 'with', чтобы файл закрылся автоматически
    with open("students.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

    print("")
    print("Total students: " + str(len(students)))
    print("")
    print("First 5 rows:")
    print("-" * 30)
    # Выводим первые 5 строк для предпросмотра
    for i in range(5):
        s = students[i]
        print(s["student_id"] + " | " + s["age"] + " | " + s["gender"] + " | " + s["country"] + " | GPA: " + s["GPA"])
    print("-" * 30)

    # Task D3 - Сортировка: Топ-10 студентов по баллам за экзамен
    # Добавляем проверку на пустые значения (if ... else 0.0), чтобы код не выдавал ошибку
    sorted_students = sorted(
        students,
        key=lambda x: float(x["final_exam_score"]) if x["final_exam_score"].strip() != "" else 0.0,
        reverse=True
    )
    top10 = sorted_students[:10]

    print("")
    print("-" * 30)
    print("Top 10 Students by Exam Score")
    print("-" * 30)
    for i in range(len(top10)):
        s = top10[i]
        print(str(i + 1) + ". " + s["student_id"] + " | " + s["country"] + " | " + s["major"] + " | Score: " + s[
            "final_exam_score"] + " | GPA: " + s["GPA"])
    print("-" * 30)

    # Task D4 - Сохранение результата в JSON
    top10_list = []
    for i in range(len(top10)):
        s = top10[i]
        # Проверяем баллы и GPA перед сохранением, чтобы в JSON были числа, а не пустые строки
        score_val = float(s["final_exam_score"]) if s["final_exam_score"].strip() != "" else 0.0
        gpa_val = float(s["GPA"]) if s["GPA"].strip() != "" else 0.0

        top10_list.append({
            "rank": i + 1,
            "student_id": s["student_id"],
            "country": s["country"],
            "major": s["major"],
            "final_exam_score": score_val,
            "GPA": gpa_val
        })

    result = {
        "analysis": "Top 10 Students by Exam Score",
        "total_students": len(students),
        "top_10": top10_list
    }

    # Записываем результат в папку output
    with open("output/result.json", "w", encoding="utf-8") as output_file:
        json.dump(result, output_file, indent=4)

    print("")
    print("=" * 30)
    print("ANALYSIS RESULT")
    print("=" * 30)
    print("Analysis : Top 10 Students by Exam Score")
    print("Total students : " + str(len(students)))
    print("Top 10 saved to output/result.json")
    print("=" * 30)