#! /usr/bin/env python3
import re,sys,dateparser 


file_path=sys.argv[1]
json_file=open(file_path,"r").read()
open(file_path.removesuffix("json_file")+"html","a").write("""<table border="0">""")
photo=re.findall(r"""(?<="photo": ").+?(?=",)""",json_file)
author=re.findall(r"""(?<="author": ").+?(?=",)""",json_file)
time=re.findall(r"""(?<="time": ").+?(?=",)""",json_file) 
cid=re.findall(r"""(?<="cid": ").+?(?=",)""",json_file)
text=re.findall(r"""(?<="text": ").+?(?=",)""",json_file)




        
if json_file.count('"cid": "')==json_file.count('", "text": "')==json_file.count('", "time": "')==json_file.count('", "author": "')==json_file.count('", "photo": "'):
        for i in range(len(cid)):
            if "." not in cid[i]: #This is so only main comments (not replies) are taken into account
                open(file_path.removesuffix("json")+"html","a").write('<tr><td></td></tr><tr><td rowspan="2"><img src="'+photo[i]+'"></td><td><strong>'+author[i]+'\
                </strong></td><td>\
                <span style="color: #9b9b9b;">'+time[i]+'</span></td></tr><tr><td id="'+cid[i]+'" colspan="2">'+text[i].replace("\\n","\n").replace('\\"','"')+'</td></tr>')
                comment_replies=re.findall(cid[i]+'\..+?(?=")',json_file)
                if len(comment_replies)>0:
                    for i in range (len(comment_replies)):
                        open(file_path.removesuffix("json_file")+"html","a").write('<tr><td></td><td rowspan="2"><img src="'+photo[cid.index(comment_replies[i])]+'"/></td><td><strong>'+author[cid.index(comment_replies[i])]+'</strong><span style="color: #9b9b9b;"> '+time[cid.index(comment_replies[i])]+'</span></td></tr><tr><td></td><td>'+text[cid.index(comment_replies[i])].replace("\\n","\n").replace('\\"','"')+'</td></tr>')
                       
                else:
                    pass
            else:
                pass
else:
        print("ERROR! Mismatch in descriptors!")
        print("comment identification numbers="+str(json_file.count('"cid": "')))
        print("comment texts="+str(json_file.count('", "text": "')))
        print("comment times="+str(json_file.count('", "time": "')))
        print("comment authors="+str(json_file.count('", "author": "')))
        print("comment author photos="+str(json_file.count('", "photo": "')))
