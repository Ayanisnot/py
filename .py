def shutdown(s) :
    s = s.upper()
    if s == "YES":
        return  "shutting down..."
    elif s == "NO":
        return "shutdown aborted.." 
    else :
        return "SORRY, I DIDNT UNDERSTAND THAT."
    

print(shutdown("maybe")) 


