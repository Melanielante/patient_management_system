export interface Patient {
  patient_id: string;
  first_name: string;
  last_name: string;
  date_of_birth: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
}
