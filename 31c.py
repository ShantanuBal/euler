import time

def brute_force_coin():
    step = 0
    coin = 200

    for i in range(coin,-1,-200):
        for a in range(i,-1,-100):
            for b in range(a,-1,-50):
                for c in range(b,-1,-20):
                    for d in range(c,-1,-10):
                        for e in range(d,-1,-5):
                            for f in range(e,-1,-2):
                                    step += 1



    print step

def main():
    start = time.time()
    brute_force_coin()
    elapsed = time.time() - start

    print 'elapsed time: %3f ms' % int(round(elapsed* 1000))

if __name__ == '__main__':
    main()
