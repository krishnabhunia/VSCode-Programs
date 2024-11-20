import json

raw_data = {
    "patients": [
        {
            "patient_id": "P001",
            "name": "John Doe",
            "claims": [
                {
                    "claim_id": "C001",
                    "billing_code": "B1001",
                    "claim_amount": 500.0
                },
                {
                    "claim_id": "C002",
                    "billing_code": "B1002",
                    "claim_amount": 1500.0
                }
            ]
        },
        {
            "patient_id": "P002",
            "name": "Jane Smith",
            "claims": [
                {
                    "claim_id": "C003",
                    "billing_code": "B1003",
                    "claim_amount": 200.0
                },
                {
                    "claim_id": "C004",
                    "billing_code": "B1004",
                    "claim_amount": 3000.0
                }
            ]
        },
        {
            "patient_id": "P003",
            "name": "Alice Brown",
            "claims": [
                {
                    "claim_id": "C005",
                    "billing_code": "B1005",
                    "claim_amount": 750.0
                },
                {
                    "claim_id": "C006",
                    "billing_code": "B1006",
                    "claim_amount": 1250.0
                }
            ]
        }
    ]
}

# Extracting maximum claim amount for each patient
max_claims = {}
for patient in raw_data['patients']:
    patient_id = patient['patient_id']
    max_claim = max(claim['claim_amount'] for claim in patient['claims'])
    max_claims[patient_id] = max_claim

print(max_claims)


patient_input = 'P002'
max_claim = None
for patient in raw_data['patients']:
    if patient['patient_id'] == patient_input:
        max_claim = max(claim['claim_amount'] for claim in patient['claims'])
        break

print(f"Maximum claim amount for patient {patient_input}: {max_claim}")
