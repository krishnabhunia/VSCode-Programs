import multiprocessing as mp
import time
def test(res = 0):
    print("Test start with res = ", res)
    time.sleep(res)
    print("Test stop")

def check():
    try:
        proc = mp.Process(target=test,args=([10]))
        proc.start()
        proc.join(timeout=3)
        if proc.is_alive():
            print("process is alive")
            proc.terminate()
        else:
            print("process ended normally")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    check()