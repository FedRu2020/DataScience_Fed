from time import sleep
from random import gauss
from requests import Session

def main():
    data = [0.9079665 ,  0.34736425, -1.03201904,  0.61099849,  0.30889008,
        1.54205361,  0.7459991 ,  1.80380665, -0.0072127 ,  0.30598963,
       -0.58477711, 1.,  0.]
    with Session() as s:
        for i in range(50):
            data[0] = gauss(0.9, 0.05) #replacing 0 value with gauss distribution. the rest data are static
            data[3] = gauss(0.62, 0.05)
            data[5] = gauss(0.74, 0.05)
            data[6] = gauss(1.8, 0.2)
            resp = s.post("http://localhost:5000", json=data)
            resp.raise_for_status()
            if i % 10 == 0:
                print(f"response[{i}]: {resp.json()}")
            sleep(0.1)

if __name__ == "__main__":
    main()