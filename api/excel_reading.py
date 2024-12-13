import requests
import pytest
import pandas as pd

BASE_URL = "https://restful-booker.herokuapp.com"

"""
def get_payloads_from_excel(file_path):
    data = pd.read_excel(file_path)
    payloads = []
    for _, row in data.iterrows():
        payload = {
            "firstname": row["firstname"],
            "lastname": row["lastname"],
            "totalprice": int(row["totalprice"]),
            "depositpaid": row["depositpaid"] in [True, "True", 1],
            "bookingdates": {
                "checkin": row["checkin"],
                "checkout": row["checkout"]
            },
            "additionalneeds": row["additionalneeds"]
        }
        payloads.append(payload)
    print("TTTT", payloads)
    return payloads
"""
def get_payloads_from_excel(file_path):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path, sheet_name="API2")
    pd.read_csv(file_path)
    # Convert the DataFrame into a list of dictionaries (one per row)
    payloads = df.to_dict(orient="records")
    print(payloads)
    return payloads


# Used to parameterize tests, allowing you to run a test function multiple times with different inputs.
# @pytest.mark.parametrize(argnames, argvalues)
@pytest.mark.parametrize("payload", get_payloads_from_excel("payload.xlsx"))
def test_create_booking(payload):
    create_endpoint = f"{BASE_URL}/booking"
    create_headers = {}
    create_response = requests.post(create_endpoint, headers=create_headers, json=payload)

    assert create_response.status_code == 200, "Failed to create booking"
    booking_data = create_response.json()
    booking_id = booking_data.get("bookingid")
    print(f"Created Booking ID: {booking_id}")

