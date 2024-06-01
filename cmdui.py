import msvcrt
import os
import colorama
import sys
colorama.init(0)
def clearScreen(): return os.system("cls")
def print_specific_position(row, col, content):
    sys.stdout.write('\033[{};{}H'.format(row, col))
    print(content,end="")
class simpleChooseObject:
    def __init__(self,title:str,*option:str,default:int = 0):
        self.index = default
        self.option = option
        self.title = title
    def startup(self):
        while 1:
            clearScreen()
            print(self.title+"\n")
            for i in self.option:
                if self.option.index(i) == self.index:
                    print(colorama.Back.WHITE+colorama.Fore.BLACK+i+colorama.Style.RESET_ALL)
                else:
                    print(i)
            v1 = msvcrt.getch()
            if v1 == b"\r": break
            v2 = msvcrt.getch()
            if v1 == b"\xe0" and v2 == b"H" and self.index >= 1:
                self.index = self.index - 1
            elif v1 == b"\xe0" and v2 == b"P" and not self.index >= len(self.option) - 1:
                self.index = self.index + 1
            else:
                print("\a")
        return self.index
class customChooseObject():
    def __init__(self):
        self.data = []
        self.index = 0
    def add_checkbox(self,text:str,value:bool = False):
        self.data.append({"type":"checkbox","text":text,"value":value})
    def add_radio(self,text:str,id:str,value:bool = False):
        self.data.append({"type":"radio","id":id,"text":text,"value":value})
    def add_lable(self,text:str):
        self.data.append({"type": "lable","text": text})
    def add_input(self,text:str,type:str = "string",length:int = 100,default:str = ""):
        self.data.append({"type":"input","text":text,"value":default,"length":length,"inputType":type})
    def startup(self):
        self.data.append({"type":"submit"})
        while True:
            clearScreen()
            for i in self.data:
                if i['type'] == "lable" and self.data.index(i) == self.index:
                    print(colorama.Style.RESET_ALL+colorama.Fore.LIGHTBLACK_EX+i['text']+colorama.Style.RESET_ALL)
                elif i['type'] == "lable":
                    print(colorama.Style.RESET_ALL+i['text'])
                elif i['type'] == "checkbox" and i['value'] and self.data.index(i) == self.index:
                    print(colorama.Style.RESET_ALL+colorama.Back.WHITE+colorama.Fore.BLACK+"[ ✓ ] "+i['text']+colorama.Style.RESET_ALL) 
                elif i['type'] == "checkbox" and not i['value'] and self.data.index(i) == self.index:
                    print(colorama.Style.RESET_ALL+colorama.Back.WHITE+colorama.Fore.BLACK+"[   ] "+i['text']+colorama.Style.RESET_ALL) 
                elif i['type'] == "checkbox" and i['value']:
                    print(colorama.Style.RESET_ALL+"[ ✓ ] "+i['text']) 
                elif i['type'] == "checkbox" and not i['value']:
                    print(colorama.Style.RESET_ALL+"[   ] "+i['text']) 
                elif i['type'] == "radio" and i['value'] and self.data.index(i) == self.index:
                    print(colorama.Style.RESET_ALL+colorama.Back.WHITE+colorama.Fore.BLACK+"( * ) "+i['text']+colorama.Style.RESET_ALL) 
                elif i['type'] == "radio" and not i['value'] and self.data.index(i) == self.index:
                    print(colorama.Style.RESET_ALL+colorama.Back.WHITE+colorama.Fore.BLACK+"(   ) "+i['text']+colorama.Style.RESET_ALL) 
                elif i['type'] == "radio" and i['value']:
                    print(colorama.Style.RESET_ALL+"( * ) "+i['text']) 
                elif i['type'] == "radio" and not i['value']:
                    print(colorama.Style.RESET_ALL+"(   ) "+i['text']) 
                elif i['type'] == "submit" and self.data.index(i) == self.index:
                    print(colorama.Style.RESET_ALL+colorama.Back.WHITE+colorama.Fore.BLACK+"\n[提交/Submission]"+colorama.Style.RESET_ALL)
                elif i['type'] == "submit":
                    print(colorama.Style.RESET_ALL+"\n[提交/Submission]")
                elif i['type'] == "input" and self.data.index(i) == self.index:
                    print(i['text'])
                    if i['inputType'] == "password":
                        print(colorama.Style.RESET_ALL+colorama.Back.WHITE+colorama.Fore.BLACK+(len(i['value'])*"*"),end="")
                    else:
                        print(colorama.Style.RESET_ALL+colorama.Back.WHITE+colorama.Fore.BLACK+i['value'],end="")
                    print(" "*(i['length']-len(i['value']))+colorama.Style.RESET_ALL,end="\n")
                    #print(" "*(100-len(i['text']))+colorama.Style.RESET_ALL)
                    #sys.stdout.write('\033[;256H')
                elif i['type'] == "input":
                    print(i['text'])
                    if i['inputType'] == "password":
                        print(colorama.Style.RESET_ALL+colorama.Back.LIGHTBLACK_EX+(len(i['value'])*"*"),end="")
                    else:
                        print(colorama.Style.RESET_ALL+colorama.Back.LIGHTBLACK_EX+i['value'],end="")
                    print(" "*(i['length']-len(i['value']))+colorama.Style.RESET_ALL,end="\n")
                    #sys.stdout.write('\033[;256H')

            v1 = msvcrt.getwch()
            if v1 == "\xe0":
                v2 = msvcrt.getwch()
            else: v2 = None
            if v1 == "\xe0" and v2 == "H" and self.index >= 1:
                self.index = self.index - 1
            elif v1 == "\xe0" and v2 == "P" and not self.index > len(self.data)-2:
                self.index = self.index + 1
            elif self.data[self.index]['type'] == "checkbox" and self.data[self.index]['value'] == False and v1 == "\r":
                self.data[self.index]['value'] = True
            elif self.data[self.index]['type'] == "checkbox" and self.data[self.index]['value'] == True and v1 == "\r":
                self.data[self.index]['value'] = False
            elif self.data[self.index]['type'] == "radio" and self.data[self.index]['value'] == False and v1 == "\r":
                for i in self.data:
                    if i['type'] == "radio":
                        if i['id'] == self.data[self.index]['id']:
                            i['value'] = False 
                self.data[self.index]['value'] = True
            elif self.data[self.index]['type'] == "submit" and v1 == "\r":
                break
            elif self.data[self.index]['type'] == "input" and v1 == "\r":
                pass
            elif self.data[self.index]['type'] == "input" and v1 == "\x08":
                self.data[self.index]['value'] = self.data[self.index]['value'][:-1]
            elif self.data[self.index]['type'] == "input" and not v1 == "\xe0":
                self.data[self.index]['value'] =  self.data[self.index]['value'] + v1
            else:
                print("\a")
        return self.data