import tkinter as tk
from Calculator import draw,finder

btn_h = 3
btn_w = 12
get_input = ""
window = tk.Tk()
window.title("Calculator app")
window.geometry("900x900")
window.configure(background= "#AAAAAA")
mode = 0
def switch_mode():
    global mode
    
    mode += 1
    if mode % 2 == 1:
        btn[1].config(text = "X")
        btn[2].config(text = "^")
        btn[3].config(text =  "DRAW")
    else:
        btn[1].config(text = "/")
        btn[2].config(text = "%")
        btn[3].config(text =  "*")
        

def press(num):
    global temp
    global opt
    if mode % 2 == 0:
        if keys[num] == "C":
            disp.delete(0,tk.END)
        elif keys[num] == "+" or keys[num] == "-" or keys[num] == "/" or keys[num] == "*" or keys[num]=="%":
            opt = keys[num]
            temp = float(disp.get())
            print(temp)
            disp.delete(0,tk.END)
        elif keys[num] == "=":
            if opt == "+":
                
                result = temp + float(disp.get())
            elif opt == "-":
                result = temp - float(disp.get())
            elif opt == "*":
                result = temp*float(disp.get())
            elif opt == "/":
                result = temp / float(disp.get())
            elif opt == "%":
                result = temp/100
            disp.delete(0,tk.END)
            disp.insert(0, str(result))
            
        else:        
            k = keys[num]
            disp.insert(tk.END,str(k))
    else:
        if alt_keys[num] == "C":
            disp.delete(0,tk.END)
        #elif alt_keys[num] == "DRAW": ADD the function here
        elif alt_keys[num] == "DRAW":
            get_input = disp.get()
            draw(get_input)
            
        else:        
            k = alt_keys[num]
            disp.insert(tk.END,str(k))
        

disp = tk.Entry(window , width = 40, font = ("courier 28"))
disp.grid(row = 0 , column = 0 , columnspan = 5)

alt_keys  = ["C", "X","^","DRAW","7","8","9","-","4","5","6","+","1","2","3","=","0",".","MODE"]
keys = ["C", "/","%","*","7","8","9","-","4","5","6","+","1","2","3","=","0",".","MODE"]
btn = []

for i in range(len(keys) - 4):
    btn.append(tk.Button(window,width = btn_w, height= btn_h, text = keys[i], command = lambda v = i : press(v)))
    btn[i].grid(row = (i//4)+1, column = i%4, sticky = "nsew", padx = 2,pady = 2)
btn.append(tk.Button(window,width = btn_w, height= btn_h*2 +1, text = keys[15], command = lambda : press(15)))
btn[15].grid(row = 4, column = 3 , rowspan = 2, sticky = "nsew", padx = 2,pady = 2)

btn.append(tk.Button(window,width = btn_w*2 + 2, height= btn_h, text = keys[16], command = lambda : press(16)))
btn[16].grid(row = 5, column = 0 , columnspan = 2, sticky = "nsew", padx = 2,pady = 2)

btn.append(tk.Button(window,width = btn_w, height= btn_h, text = keys[17], command = lambda : press(17)))
btn[17].grid(row = 5, column = 2, sticky = "nsew", padx = 2,pady = 2 )



btn.append(tk.Button(window,width = btn_w, height= btn_h, text = keys[18], command = switch_mode))
btn[18].grid(row = 1, column = 4, sticky = "nsew", padx = 2,pady = 2 )
window.mainloop()