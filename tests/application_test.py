from application import application
import json
import time

# Check if the home page is working as expected
def test_welcome():
    tester = application.test_client()
    response = tester.get("/", content_type="html/text")
    assert response.status_code == 200
    assert response.data == b"Welcome to the Fake News Detector Tool"

# Expected output is FAKE because Neil Armstrong went to the moon
def test_fake():
    tester = application.test_client()
    response = tester.get("/fake-news-detector?text='Neil Armstrong went to Jupiter'")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "FAKE" in data # Check ML algorithm result

# Expected output is REAL because George Washington was the first US president
def test_real():
    tester = application.test_client()
    response = tester.get("/fake-news-detector?text='George Washington was the first US president'")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "REAL" in data # Check ML algorithm result

# Expected output is FAKE because Leonardo DiCaprio did not make this donation
def test_fake_2():
    tester = application.test_client()
    response = tester.get("/fake-news-detector?text='Leonardo DiCaprio donates $10 million to his grandmother's homeland Ukraine'")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "FAKE" in data # Check ML algorithm result

# Expected output is REAL because Canada is the second largest country after Russia
def test_real_2():
    tester = application.test_client()
    response = tester.get("/fake-news-detector?text='Canada is the second largest country.'")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "REAL" in data # Check ML algorithm result
    
# Average latency for 100 calls of each funtion
""" def test_latency_1():
    total_time = 0
    for x in range(100):
        start_time = time.time()
        tester = application.test_client()
        response = tester.get("/fake-news-detector?text='Neil Armstrong went to Jupiter'")
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "FAKE" in data
        print("--- %s seconds ---" % (time.time() - start_time))
        total_time += time.time() - start_time
        print(x)
    average_time = total_time/100.0
    assert average_time == 0.0

def test_latency_2():
    total_time = 0
    for x in range(100):
        start_time = time.time()
        tester = application.test_client()
        response = tester.get("/fake-news-detector?text='George Washington was the first US president'")
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "REAL" in data 
        print("--- %s seconds ---" % (time.time() - start_time))
        total_time += time.time() - start_time
        print(x)
    average_time = total_time/100.0
    assert average_time == 0.0

def test_latency_3():
    total_time = 0
    for x in range(100):
        start_time = time.time()
        tester = application.test_client()
        response = tester.get("/fake-news-detector?text='Leonardo DiCaprio donates $10 million to his grandmother's homeland Ukraine'")
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "FAKE" in data
        print("--- %s seconds ---" % (time.time() - start_time))
        total_time += time.time() - start_time
        print(x)
    average_time = total_time/100.0
    assert average_time == 0.0

def test_latency_4():
    total_time = 0
    for x in range(100):
        start_time = time.time()
        tester = application.test_client()
        response = tester.get("/fake-news-detector?text='Canada is the second largest country.'")
        assert response.status_code == 200
        data = json.loads(response.data)
        assert "REAL" in data
        print("--- %s seconds ---" % (time.time() - start_time))
        total_time += time.time() - start_time
        print(x)
    average_time = total_time/100.0
    assert average_time == 0.0 """