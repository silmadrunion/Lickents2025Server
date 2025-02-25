def validateType(key_name, value, type):
    if isinstance(value, type):
        return True
    else: 
        return f"{key_name} is not {type}"
    
def validateRange(key_name, value, min, max):
    if value > min and value < max:
        return True
    else:
        return f"{key_name} is not between {min} and {max}"