filename = input()
print(filename)
with open(filename, "r+", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        _templine = line
        if line.find("’") or line.find("‘") or line.find("“") or line.find("”"):
            try:
                _templine = _templine.replace("’", "'")
            except:
                pass
            try:
                _templine = _templine.replace("‘", "'")
            except:
                pass
            try:
                _templine = _templine.replace("“", "\"")
            except:
                pass    
            try:
                _templine = _templine.replace("”", "\"")
            except:
                pass
            lines[lines.index(line)] = _templine

    f.seek(0)
    f.writelines(lines) 
    f.truncate() 