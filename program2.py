with open("mywishes.txt","x") as f1:
    f1.write("1st wish to be happy")
    f1.write("2nd wish to go vacation himachal")
    f1.close()
with open("mywishes.txt","r") as f1:
    f1.read()
    
  