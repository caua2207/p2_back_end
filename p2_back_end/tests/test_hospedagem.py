from tests.conftest import client


def test_criar_suite():
    response = client.post(
        "/suites/",
        json={
            "numero": 1,
            "categoria": "Luxo",
            "valor_hora": 100,
            "status": "Disponível"
        }
    )

    assert response.status_code == 200


def test_criar_hospedagem():
    response = client.post(
        "/hospedagens/",
        json={
            "data_entrada": "15/06/2026",
            "id_cliente": 1,
            "id_suite": 1
        }
    )

    assert response.status_code == 200


def test_listar_hospedagens():
    response = client.get("/hospedagens/")

    assert response.status_code == 200


def test_buscar_hospedagem():
    response = client.get("/hospedagens/1")

    assert response.status_code == 200


def test_checkout_hospedagem():
    response = client.put("/hospedagens/1/checkout")

    assert response.status_code == 200


def test_checkout_invalido():
    response = client.put("/hospedagens/1/checkout")

    assert response.status_code == 400