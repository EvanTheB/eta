import sys
from datetime import datetime, timedelta
import time
import scipy.stats
import subprocess
from  collections import deque



def main():
    vs = set()
    v = []
    t = []
    sleep_time = 2
    while True:
        l = subprocess.run(
            sys.argv[1],
            stdout=subprocess.PIPE,
            check=True,
            shell=True,
            encoding='utf8',
        ).stdout

        if float(l) < 0.5:
            exit()

        if l not in vs:
            vs.add(l)
            v.append(float(l))
            t.append(datetime.now().timestamp())
        # print(t)
        # print(len(set(v)), len(set(v)) / len(v))

        if len(v) > 2:
            r = scipy.stats.linregress(t, v)
            # print(r)
            if r.slope != 0.0:
                eta = -r.intercept / r.slope
                # print(eta)

                etad = datetime.fromtimestamp(eta)
                # print(etad)

                print(
                    etad - datetime.now(),
                    # r.rvalue,
                )

        time.sleep(sleep_time)
        sleep_time = min(60, sleep_time * 1.05)


if __name__ == '__main__':
    main()
