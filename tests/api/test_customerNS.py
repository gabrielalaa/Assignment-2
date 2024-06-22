# import pytest
#
#
# def test_post_add_customer(client):
#     data = {
#         "customer_name": "Carla Radulescu",
#         "customer_age": 20,
#         "customer_gender": "female",
#         "customer_address": "123 Stone Street",
#         "balance": 200
#     }
#
#     response = client.post("/customer/", json=data)
#     print(response.json)
#     assert response.status_code == 200
#     assert 'customer_id' in response.json
#     assert response.json['customer']['customer_name'] == 'Carla Radulescu'
