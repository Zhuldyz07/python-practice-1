from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import TopStudentsAnalyser

if __name__ == "__main__":

    fm = FileManager("students.csv")
    if not fm.check_file():
        exit()
    fm.create_output_folder()


    dl = DataLoader("students.csv")
    students_data = dl.load()
    dl.preview()

    analyser = TopStudentsAnalyser(students_data)

    saver = ResultSaver(analyser.result, "output/result.json")
    report = Report(analyser, saver)
    report.generate()


