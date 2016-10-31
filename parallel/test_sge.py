from parallel import SGE
from time import sleep

if __name__ == "__main__":

    def f(x):
        sleep(30)
        return x * 2

    print("Start sge test", flush=True)
    sge = SGE(priority=0, memory="1G", name="test", time_h=1)

    print("Do map", flush=True)
    res = sge.map(f, [1, 2, 3, 4])

    print("Got results", flush=True)
    assert res == [2, 4, 6, 8], "Wrong result, got {}".format(res)

    print("Finished", flush=True)
