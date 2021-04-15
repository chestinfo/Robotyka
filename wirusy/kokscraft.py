from multiprocessing import Pool

def f(x):
    t = []
    while True:
        t.append(x * x)

        #ile rdzeni chcemy wykorzystac (mozna podac dowolnie duza liczbe, i tak obciazenie nie przekroczy 100%
rdzeni = 15

if __name__ == '__main__':
    p = Pool(rdzeni)
    p.map(f, range(rdzeni))
