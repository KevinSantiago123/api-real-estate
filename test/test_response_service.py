import requests

__author__ = 'kcastanedat'

URL_SERVICE = f"http://127.0.0.1:8000/dev/estate/?"

def test_get_estate_by_filters():
    """Makes a request type get to the real estate service with the parameters allowed for the filter"""
    year = 2019
    city = "pereira"
    status = "vendido"
    response = requests.get(
        f"{URL_SERVICE}status={status}&city={city}&year={year}")
    print(response)
    expected_response = {
        "data": [
            [
                70,
                "Cll 1A #11B-20b",
                "pereira",
                "vendido",
                300000000,
                "hermoso acabado, listo para estrenar super comodo"
            ],
            [
                16,
                "Cll 1A #11B-20",
                "pereira",
                "vendido",
                300000000,
                "hermoso acabado, listo para estrenar super comodo"
            ]
        ],
        "message": "Ok",
        "status": 200
    }
    assert response.json() == expected_response


def test_get_estate_key_failed():
    """Verify name of parameters in the service, the options are status, year and city"""
    key = "statu"
    response = requests.get(
        f"{URL_SERVICE}{key}=2019")

    expected_response = {
        "message": f"The key: '{key}' is not a valid parameter",
        "status": 400
    }
    assert response.json() == expected_response


def test_get_estate_value_status_failed():
    """Check that the response indicates when the value is not valid in the status"""
    value = "vendid"
    response = requests.get(
        f"{URL_SERVICE}status={value}")

    expected_response = {
        "message": "The possible values for the key: 'status' are ['pre_venta', 'en_venta', 'vendido']",
        "status": 400
    }
    assert response.json() == expected_response


def test_get_estate_value_year_failed():
    """Check that the response indicates when the value is not valid in the year, considering only positive values"""
    value = -2021
    response = requests.get(
        f"{URL_SERVICE}year={value}")

    expected_response = {
        "message": "The value of key: 'year' is not positive",
        "status": 400
    }
    assert response.json() == expected_response
