def test_metrics_route(client):
    # Сбросить счетчик
    global request_count
    request_count = 0

    # Вызвать /time 3 раза
    for _ in range(3):
        client.get('/time')

    response = client.get('/metrics')
    data = response.get_json()
    assert data['count'] == 3
