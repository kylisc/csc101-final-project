class Student:
    def __init__(self, name, sleep_hours, study_hours, stress_level):
        self.name = name.strip()
        self.sleep_hours = sleep_hours
        self.study_hours = study_hours
        self.stress_level = stress_level

    def sleep_to_study_ratio(self):
        if self.study_hours == 0:
            return 0.0
        return round(self.sleep_hours / self.study_hours, 2)

    def categorize_stress(self):
        if self.stress_level <= 3:
            return "Low"
        elif self.stress_level <= 7:
            return "Medium"
        else:
            return "High"

    def wellness_score(self):
        score = (self.sleep_hours * 1.5) - (self.study_hours * 0.5) - self.stress_level
        if score >= 7:
            label = "Excellent"
        elif score >= 4:
            label = "Moderate"
        else:
            label = "Needs Improvement"
        return round(score, 2), label

class Community:
    def __init__(self, students):
        self.students = students
        self.stress_groups = {"Low": [], "Medium": [], "High": []}
        self.summary = {"avg_sleep": 0.0, "avg_study": 0.0, "avg_stress": 0.0}
        self.wellness_tips = {
            "Low Sleep": "Try to maintain at least 7 hours of sleep.",
            "High Stress": "Take short breaks and use breathing exercises.",
            "Balanced": "Keep up the healthy habits!"
        }

    def compute_averages(self):
        if not self.students:
            return
        n = len(self.students)
        total_sleep = 0
        for s in self.students:
            total_sleep += s.sleep_hours
        avg_sleep = total_sleep / n
        self.summary["avg_sleep"] = (avg_sleep)

        total_study = 0
        for s in self.students:
            total_study += s.study_hours
        avg_study = total_study / n
        self.summary["avg_study"] = (avg_study)

        total_stress = 0
        for s in self.students:
            total_stress += s.stress_level
        avg_stress = total_stress / n
        self.summary["avg_stress"] = (avg_stress)

    def group_by_stress(self):
        for k in self.stress_groups:
            self.stress_groups[k] = []
        for s in self.students:
            self.stress_groups[s.categorize_stress()].append(s)

    def stress_distribution_percent(self):
        n = len(self.students)
        if n == 0:
            return {"Low": 0, "Medium": 0, "High": 0}
        result = {}
        for k, v in self.stress_groups.items():
            percent = len(v) * 100 / n
            result[k] = percent
        return result

    def tip_for_student(self, s):
        if s.sleep_hours < 7:
            return self.wellness_tips["Low Sleep"]
        if s.stress_level >= 7:
            return self.wellness_tips["High Stress"]
        return self.wellness_tips["Balanced"]

    def display_summary(self):
        self.compute_averages()
        self.group_by_stress()
        dist = self.stress_distribution_percent()
        print("\nCommunity Averages:")
        print("Average Sleep:", self.summary["avg_sleep"], "hours")
        print("Average Study:", self.summary["avg_study"], "hours")
        print("Average Stress Level (out of 10):", self.summary["avg_stress"])
        print("Stress Distribution")
        print("  Low:", dist['Low'], "%")
        print("  Medium:", dist['Medium'], "%")
        print("  High:", dist['High'], "%")


