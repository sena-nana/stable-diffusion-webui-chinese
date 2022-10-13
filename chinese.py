import json
with open("chinese.json",encoding = "utf-8") as f:
    map=json.load(f)
    print(f"汉化文件加载完成")
for file,value in map.items():
    print(f"正在汉化{file}")
    hasvalue=len(value)
    dovalue=0
    with open(file,"r",encoding = "utf-8") as f:
        code=f.read()
    for old,new in value.items():
        code=code.replace(old,new)
        dovalue += 1
    with open(file,"w",encoding = "utf-8") as f:
        f.write(code)
    print(f"{file}汉化完成，存在{hasvalue}条汉化条目，成功匹配{dovalue}")
