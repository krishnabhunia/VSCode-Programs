import json as js

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


def search_json(data, key):
    for i in data:
        print(type(i), i)
        print(type(data[i]), data[i])
        if data[i] is list:
            for j in data[i]:
                print(type(j), j)
                print(type(j[i]), j[i])
                if j[i] == key:
                    return j
                else:
                    return search_json(j, key)


print(search_json(raw_data, 'P001'))
