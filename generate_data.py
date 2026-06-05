import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

np.random.seed(42)
random.seed(42)

os.makedirs("data", exist_ok=True)

# -----------------------------
# Facilities
# -----------------------------
facilities = pd.DataFrame([
    ["FAC-001", "MetroHealth Central Hospital", "Tertiary Hospital"],
    ["FAC-002", "LagosCare Emergency Center", "Emergency"],
    ["FAC-003", "Abuja Specialist Hospital", "Specialist Hospital"],
    ["FAC-004", "Kano Community Clinic", "Primary Care"],
    ["FAC-005", "Port Harcourt Medical Center", "General Hospital"],
    ["FAC-006", "Central Diagnostic Laboratory", "Laboratory"],
    ["FAC-007", "Prime Pharmacy Network", "Pharmacy"],
    ["FAC-008", "National HMO Connect", "HMO"],
    ["FAC-009", "TeleHealth Nigeria", "Telemedicine"],
    ["FAC-010", "Maternal & Child Health Center", "Specialist Clinic"],
    ["FAC-011", "CardioRenal Institute", "Specialist Center"],
    ["FAC-012", "Infectious Disease Surveillance Unit", "Public Health"],
], columns=["facility_id", "facility_name", "facility_type"])

facilities.to_csv("data/facilities.csv", index=False)

# -----------------------------
# Patients
# -----------------------------
first_names = ["Amina", "Chinedu", "Fatima", "Tunde", "Ngozi", "Ibrahim", "Zainab", "Emeka", "Maryam", "Samuel"]
last_names = ["Bello", "Okafor", "Adeyemi", "Musa", "Eze", "Abubakar", "Lawal", "Nwosu", "Balogun", "Yakubu"]
genders = ["Female", "Male"]

patients = []
for i in range(1, 501):
    patient_id = f"MTX-{i:05d}"
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    age = np.random.randint(1, 90)
    gender = random.choice(genders)
    phone = f"+23480{np.random.randint(10000000, 99999999)}"
    city = random.choice(["Lagos", "Abuja", "Kano", "Port Harcourt", "Ibadan", "Kaduna"])
    patients.append([patient_id, name, age, gender, phone, city])

patients_df = pd.DataFrame(
    patients,
    columns=["patient_id", "name", "age", "gender", "phone", "city"]
)

patients_df.to_csv("data/patients.csv", index=False)

# -----------------------------
# Encounters
# -----------------------------
encounter_types = [
    "ED Visit", "Admission", "Outpatient Visit", "Lab Visit",
    "Pharmacy Visit", "Telemedicine Visit", "Discharge", "Referral"
]

start_date = datetime(2026, 1, 1)
encounters = []

for i in range(1, 2001):
    encounter_id = f"ENC-{i:06d}"
    patient_id = random.choice(patients_df["patient_id"].tolist())
    facility_id = random.choice(facilities["facility_id"].tolist())
    encounter_type = random.choice(encounter_types)
    date = start_date + timedelta(days=np.random.randint(0, 180), hours=np.random.randint(0, 24))
    status = random.choice(["Completed", "Active", "Pending"])
    encounters.append([encounter_id, patient_id, facility_id, encounter_type, date, status])

encounters_df = pd.DataFrame(
    encounters,
    columns=["encounter_id", "patient_id", "facility_id", "event", "date", "status"]
)

encounters_df.to_csv("data/encounters.csv", index=False)

# -----------------------------
# Observations
# -----------------------------
tests = {
    "Temperature": (35.5, 40.5),
    "Heart Rate": (55, 140),
    "Systolic BP": (85, 180),
    "Respiratory Rate": (12, 35),
    "Oxygen Saturation": (85, 100),
    "WBC": (3, 25),
    "Lactate": (0.5, 7),
    "Creatinine": (0.5, 4),
    "Glucose": (60, 350),
    "Hemoglobin": (7, 17)
}

observations = []
encounter_ids = encounters_df["encounter_id"].tolist()

for i in range(1, 6001):
    observation_id = f"OBS-{i:06d}"
    encounter_id = random.choice(encounter_ids)
    row = encounters_df.loc[encounters_df["encounter_id"] == encounter_id].iloc[0]
    patient_id = row["patient_id"]
    test_name = random.choice(list(tests.keys()))
    low, high = tests[test_name]
    result = round(np.random.uniform(low, high), 1)
    observed_at = pd.to_datetime(row["date"]) + timedelta(minutes=np.random.randint(10, 240))
    observations.append([observation_id, encounter_id, patient_id, test_name, result, observed_at])

observations_df = pd.DataFrame(
    observations,
    columns=["observation_id", "encounter_id", "patient_id", "test_name", "result", "observed_at"]
)

observations_df.to_csv("data/observations.csv", index=False)

# -----------------------------
# Medications
# -----------------------------
drugs = [
    "Ceftriaxone", "Metformin", "Paracetamol", "Amlodipine",
    "Insulin", "Azithromycin", "Salbutamol", "Omeprazole",
    "Furosemide", "Atorvastatin"
]

medications = []

for i in range(1, 2501):
    medication_id = f"MED-{i:06d}"
    patient_id = random.choice(patients_df["patient_id"].tolist())
    drug_name = random.choice(drugs)
    date_dispensed = start_date + timedelta(days=np.random.randint(0, 180))
    facility_id = random.choice(["FAC-007", "FAC-001", "FAC-003", "FAC-005"])
    medications.append([medication_id, patient_id, drug_name, date_dispensed, facility_id])

medications_df = pd.DataFrame(
    medications,
    columns=["medication_id", "patient_id", "drug_name", "date_dispensed", "facility_id"]
)

medications_df.to_csv("data/medications.csv", index=False)

print("Synthetic MetroHealth TransformX datasets generated successfully.")
print(f"Patients: {len(patients_df)}")
print(f"Facilities: {len(facilities)}")
print(f"Encounters: {len(encounters_df)}")
print(f"Observations: {len(observations_df)}")
print(f"Medications: {len(medications_df)}")