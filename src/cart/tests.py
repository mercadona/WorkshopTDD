from fastapi.testclient import TestClient
from src.cart.views import app, db

client = TestClient(app)


# TEST RETURN CART BY ID
def test_return_cart():
    db[1] = {
        "id": 1,
        "lines": [
            {"product": 50776, "quantity": 2},
            {"product": 15778, "quantity": 4}
        ]
    }

    response = client.get("/cart/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "lines": [
            {"product": 50776, "quantity": 2},
            {"product": 15778, "quantity": 4}
        ]
    }

# TEST ADD PRODUCT TO THE CART
# def test_


# BEFORE MOVING ON...
# HAVE YOU SET THE TEST TO GREEN??
# HAVE YOU DID A REFACTOR?


# TEST SUM QUANTITY TO A PRODUCT OF THE CART
# def test_

# BEFORE MOVING ON...
# HAVE YOU SET THE TEST TO GREEN??
# HAVE YOU DID A REFACTOR?


# TEST SUBSTRACT PRODUCT OF THE CART
# def test_

# BEFORE MOVING ON...
# HAVE YOU SET THE TEST TO GREEN??
# HAVE YOU DID A REFACTOR?


# TEST REST QUANTITY OF A PRODUCT OF THE CART
# def test_

# BEFORE MOVING ON...
# HAVE YOU SET THE TEST TO GREEN??
# HAVE YOU DID A REFACTOR?


# TEST CANT REST MORE QUANTITY THAN EXISTS OF A PRODUCT OF THE CART
# def test_

# BEFORE MOVING ON...
# HAVE YOU SET THE TEST TO GREEN??
# HAVE YOU DID A REFACTOR?


# TEST CLEAR THE CART
# def test_

# BEFORE MOVING ON...
# HAVE YOU SET THE TEST TO GREEN??
# HAVE YOU DID A REFACTOR?


# TEST ADD TOTAL TO THE CART
# def test_

# BEFORE MOVING ON...
# HAVE YOU SET THE TEST TO GREEN??
# HAVE YOU DID A REFACTOR?