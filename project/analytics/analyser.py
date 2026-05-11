class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        pass

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")


class TopStudentsAnalyser(DataAnalyser):  # Сіздің Variant D
    def analyse(self):
        valid_students = list(filter(lambda s: s["final_exam_score"] != "", self.students))
        sorted_students = sorted(valid_students, key=lambda x: float(x["final_exam_score"]), reverse=True)
        top10 = sorted_students[:10]

        top10_list = []
        for i, s in enumerate(top10):
            top10_list.append({
                "rank": i + 1,
                "student_id": s["student_id"],
                "final_exam_score": float(s["final_exam_score"])
            })

        self.result = {"total_students": len(self.students), "top_10": top10_list}
        return self.result