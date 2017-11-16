fp=open("kttekst.txt","r+");
sõnad=fp.read();
word_count=1;
for i in sõnad:
    if i==" ":
        word_count=word_count+1;

print ("sõnasi on:", word_count);

#siit allapoole ei tööta
with open("kttekst.txt") as f:
    for line in f:
        if len(line >= 5):
            print (line)
