import sys
sys.path.append(r'C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\Pillow-8.0.0-py3.6-win32.egg')
sys.path.append(r'C:\users\asus\appdata\local\programs\python\python36-32\lib\site-packages\numpy-1.19.2-py3.6-win32.egg')
from PIL import Image
import numpy as np
from flask import Flask, request

def test():
    f = Image.open('IMG_9417.jpg')
    Al = np.asarray(f, dtype='uint8')
    
    '''for i in range(n):
       Al = f.readline()
        for j in range(m):
       A[i][j] = Al[j].split()'''
    f.close 
    return Al

def contr(A,n,m,gran):
    col = 0
    xs = 0
    ys = 0
    #a = 50
    for i in range(n):
        for j in range(m):
            for m in range(3):
                if A[i][j][m] != gran:
                    xs += i
                    ys += j
                    col += 1
    xm = xs/col
    ym = ys/col
    return "Координаты средней точки контраста: ",round(xm),round(ym)

def prover(C):
    xc = float(input())
    yc = float(input())
    if xc == C[0] and yc == C[1]:
        return True
    else:
        return False


if __name__ =='__main__':

    app = Flask(__name__)
    @app.route('/start')
    def start_robot():
        gran = request.args.get('gran')
        if gran == None:
            gran = 0
        else:
            gran = int(gran)
            
        A = test()
        n = len(A)
        m = len(A[n-1])

#       print(A)
#       print('размер картинки: ', n, '*', m)

        Cent = []*2
        Cent = contr(A,n,m,gran)
#       print('центр масс', Cent)
#       print(prover(Cent))

        return Cent
    app.run(debug = True)
        


