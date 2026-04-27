# Variant D - Top 10 Students
# Zhuldyz Smagul BDA-2506
import os
import csv
import json

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found. Please download the file from LMS.")
            return False

    def create_output_folder(self, folder="output"):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.students.append(row)

            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students

        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
            return []

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("-" * 30)

        for i in range(min(n, len(self.students))):
            s = self.students[i]
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")

        print("-" * 30)


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        def safe_score(student):
            try:
                return float(student["final_exam_score"])
            except ValueError:
                return 0.0

        sorted_students = sorted(
            self.students,
            key=lambda x: float(x["final_exam_score"]) if x["final_exam_score"] != "" else 0.0,
            reverse=True
        )


        top10 = sorted_students[:10]

        top10_list = []

        for i, s in enumerate(top10):
            score = safe_score(s)
            try:
                gpa = float(s["GPA"])
            except ValueError:
                gpa = 0.0

            top10_list.append({
                "rank": i + 1,
                "student_id": s["student_id"],
                "country": s["country"],
                "major": s["major"],
                "final_exam_score": score,
                "GPA": gpa
            })

        self.result = {
            "analysis": "Top 10 Students by Exam Score",
            "total_students": len(self.students),
            "top_10": top10_list
        }
        return self.result

    def print_results(self):
        print("-" * 30)
        print("Top 10 Students by Exam Score")
        print("-" * 30)

        for student in self.result["top_10"]:
            print(
                f"{student['rank']}. {student['student_id']} | "
                f"{student['country']} | {student['major']} | "
                f"Score: {student['final_exam_score']} | GPA: {student['GPA']}"
            )

        print("-" * 30)


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, "w", encoding="utf-8") as file:
                json.dump(self.result, file, indent=4)

            print(f"Result saved to {self.output_path}")

        except Exception as e:
            print(f"Error while saving file: {e}")


if __name__ == "__main__":
    fm = FileManager("students.csv")

    if not fm.check_file():
        print("Stopping program.")
        exit()

    fm.create_output_folder()

    dl = DataLoader("students.csv")
    dl.load()
    dl.preview()

    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()

    saver = ResultSaver(analyser.result, "output/result.json")
    saver.save_json()