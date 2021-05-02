from multiprocessing import Process, Pipe



class pro1:
    
    def __init__(self):

        self.A = 123
        self.p1 = Pipe()

    def f(self, conn):
        self.p1.send([self.A, None, 'hello'])
        conn.close()

    def re(self):
        print(self.p1.recv())


class pro2:
    
    def __init__(self):
        self.B = 123
        self.p2 = Pipe()

    def p(self, conn):
        conn.send([self.A, None, 'hello'])
        conn.close()
    
    def re(self):
        print(self.p2.recv())






""""
def f(conn):
    conn.send([43, None, 'hello'])
    conn.send([42, None, 'hello'])
    conn.send([43, None, 'hello'])
    conn.close()

def q(conn):
    conn.send([44, None, 'hello Child'])
    conn.close()
"""

if __name__ == "__main__":
    p1, p2 = pro1(), pro2()

    
    p = Process(target=p1.f(p1.p1), args= (p1.p1, ))
    p.start()
    print(p2.re())

