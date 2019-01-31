import json


def test_add_product(fx_client, data):
    response = fx_client.post('/api/v1/product', data=json.dumps(data),
                              content_type='application/json')

    assert response.status_code == 200

    response_output = json.loads(response.get_data())
    assert response_output['name'] == data['name']
    assert response_output['description'] == data['description']
    assert response_output['price'] == data['price']
    assert response_output['quantity'] == data['quantity']


def test_get_products(fx_client, data):
    response = fx_client.get('/api/v1/product')

    assert response.status_code == 200
    response_output = json.loads(response.get_data())

    assert isinstance(response_output, list)
    assert isinstance(response_output[0], dict)
    assert response_output[0]['name'] == data['name']
    assert response_output[0]['description'] == data['description']
    assert response_output[0]['price'] == data['price']
    assert response_output[0]['quantity'] == data['quantity']


def test_get_product(fx_client, data):
    response = fx_client.get('/api/v1/product/1')

    assert response.status_code == 200
    response_output = json.loads(response.get_data())

    assert isinstance(response_output, dict)
    assert response_output['id'] == 1
    assert response_output['name'] == data['name']
    assert response_output['description'] == data['description']
    assert response_output['price'] == data['price']
    assert response_output['quantity'] == data['quantity']


def test_update_product(fx_client, another_data):
    response = fx_client.put('/api/v1/product/1',
                             data=json.dumps(another_data),
                             content_type='application/json')

    assert response.status_code == 200
    response_output = json.loads(response.get_data())

    assert isinstance(response_output, dict)
    assert response_output['id'] == 1
    assert response_output['name'] == another_data['name']
    assert response_output['description'] == another_data['description']
    assert response_output['price'] == another_data['price']
    assert response_output['quantity'] == another_data['quantity']


def test_delete_product(fx_client, data):
    response = fx_client.delete('/api/v1/product/1')

    assert response.status_code == 200
    response_output = json.loads(response.get_data())

    assert isinstance(response_output, dict)
    assert response_output['id'] == 1
