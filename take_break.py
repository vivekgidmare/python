import webbrowser
import time
count =0
print("Program Started :"+time.ctime())
while (count<2):
  time.sleep(5)
  webbrowser.open("https://www.youtube.com/watch?v=vL3_GMhNe4M")
  count=count+1
  print("::"+time.ctime())
else :
    if count == 0:
     for count in range(0,2):
        time.sleep(5)
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=vL3_GMhNe4M")
        count=count+1
        print(""+time.ctime())
print("Job done")
        
        
