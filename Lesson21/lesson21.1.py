# Create a Python class representing a Hospital account with methods to schedule visit
# and remove schedule

from datetime import datetime

class HospitalAccount:
    def __init__(self, patient_name):
        self.patient_name = patient_name
        self.scheduled_visits = []

    def schedule_visit(self, date, time, doctor_name, purpose):
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Use YYYY-MM-DD."

        try:
            datetime.strptime(time, "%H:%M")
        except ValueError:
            return "Invalid time format. Use HH:MM (24-hour format)."

        for visit in self.scheduled_visits:
            if visit["date"] == date and visit["time"] == time and visit["doctor_name"] == doctor_name:
                return f"Visit on {date} at {time} with Dr. {doctor_name} is already scheduled."

        visit = {
            "date": date,
            "time": time,
            "doctor_name": doctor_name,
            "purpose": purpose
        }
        self.scheduled_visits.append(visit)
        return f"Visit is scheduled on {date} at {time} with Dr. {doctor_name} for {purpose}."

    def remove_schedule(self, date, time, doctor_name):
        for visit in self.scheduled_visits:
            if visit["date"] == date and visit["time"] == time and visit["doctor_name"] == doctor_name:
                self.scheduled_visits.remove(visit)
                return f"Visit on {date} at {time} with Dr. {doctor_name} is removed."
        return f"No visit found on {date} at {time} with Dr. {doctor_name}."

    def get_scheduled_visits(self):
        if not self.scheduled_visits:
            return "No visits scheduled."
        return "\n".join(
            f"Date: {visit['date']}, Time: {visit['time']}, Doctor: Dr. {visit['doctor_name']}, Purpose: {visit['purpose']}"
            for visit in self.scheduled_visits
        )


account = HospitalAccount(patient_name="John")
print(account.schedule_visit("2025-01-20", "10:30", "Smith", "General Check-up"))
print(account.schedule_visit("2025-01-22", "15:00", "Brown", "Dental Cleaning"))



