#translate file from gbk to utf 
file = "单片机指令说明书.txt"

with open(file, 'r') as f:
    strs = f.read()

    
try:        
    stra = strs.encode("ansi").decode("gbk")
    file_n = "ammeded_" + file
    
    with open(file_n, 'w', encoding='utf-8') as f:
        f.write(stra)
    print("done")
except  UnicodeDecodeError as e:
    print(e)  

  
    