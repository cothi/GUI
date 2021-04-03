import psutil
import polling2
import time

def CheckDocument():

    for proc in psutil.process_iter():
        
        if proc.name() == "Microsoft Excel":
            print(proc)
            path = []
            for i in proc.open_files():
                if i[0][-4:] == "xlsx":
                    path.append(i[0])

            print(f"Find {proc.name()}")
            proc.kill()
            print(path)
            return path[1]



while True:
    time.sleep(3)
    CheckDocument()
    time.sleep(3)
