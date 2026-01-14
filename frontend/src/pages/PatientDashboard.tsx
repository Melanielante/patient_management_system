import { useEffect, useState } from "react";
import api from "../api/axios";
import { Patient } from "../types/models";

export default function PatientDashboard() {
  const [patient, setPatient] = useState<Patient | null>(null);

  useEffect(() => {
    api.get<Patient>("/patients/me").then((res) => {
      setPatient(res.data);
    });
  }, []);

  if (!patient) return <p>Loading...</p>;

  return (
    <div>
      <h2>My Profile</h2>
      <p>
        {patient.first_name} {patient.last_name}
      </p>
    </div>
  );
}
