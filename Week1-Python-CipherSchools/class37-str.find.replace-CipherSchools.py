string="she is beautiful and she is good dancer"
print(string.replace(" ","_"))
print(string.replace("is","was"))
print(string.replace("is","-",1))
is_pos=string.find("is")
is_pos2=string.find("is",is_pos+1)
print(is_pos2)