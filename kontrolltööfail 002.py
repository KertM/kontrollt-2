fp=open("kttekst.txt","r+");
sõnad=fp.read();
word_count=1;
for i in sõnad:
    if i==" ":
        word_count=word_count+1;

print ("sõnu on:", word_count);


words = sõnad.split()
väiksemkui5 = 0
with open("kttekst.txt") as f:
     for sõnad in words:
        if(len(sõnad)<5):
            väiksemkui5 +=1

print("väiksemad kui 5:", väiksemkui5)
            
