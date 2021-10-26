from app import app
import time
from portfolio import generateResponse


@app.route("/", methods=["GET"])
def exp_route():
    start_time = time.time()
    resp = generateResponse()
    print("Response: ", resp)
    end_time = time.time()
    duration = round(end_time-start_time, 3)
    print(f'Response time: {duration}')
    return resp, 200


if __name__ == "__main__":
    print("inside index.py if")
    app.run(debug=True)
