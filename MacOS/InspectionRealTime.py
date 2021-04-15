import psutil
import polling2
import time

def CheckDocument():

    for proc in psutil.process_iter():
        
        if proc.name() == "Microsoft Excel":

            time.sleep(1)
            path = []
            for i in proc.open_files():
                if i[0][-4:] == "xlsx":
                    path.append(i[0])

                    
            proc.kill()
            
            
            if len(path) != 0:
                for i in path:
                    if i.find("$") == -1:
                        return i

            else:
                break

