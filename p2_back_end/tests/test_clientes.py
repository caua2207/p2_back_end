from tests.conftest import client


def test_criar_cliente():
    response = client.post(
        "/clientes/",
        json={
            "nome": "Caua",
            "telefone": "22999999999",
            "cpf": "12345678901",
            "email": "caua@email.com"
        }
    )

    assert response.status_code == 200


def test_buscar_cliente_existente():
    response = client.get("/clientes/1")

    assert response.status_code == 200


def test_buscar_cliente_inexistente():
    response = client.get("/clientes/999")

    assert response.status_code == 404


def test_listar_clientes():
    response = client.get("/clientes/")

    assert response.status_code == 200