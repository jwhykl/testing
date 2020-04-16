import string

def transform(legacy_data):
    output={}
    for key, ld in legacy_data.items():
        for ld_i in ld:
            try:
                output[ld_i.lower()]=key
            except Exception as error:
                raise Exception("No matching key-value pair ", repr(error))
    return output
