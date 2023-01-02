buffer = open("input.txt")
buffer_str = buffer.read()

for ix, char in enumerate(buffer_str):
    if ix < 13:
        continue
    
    signal = buffer_str[ix-13:ix+1]
    letters_set = set(signal)
        
    if len(signal) == len(letters_set):
        print("First marker after character: ", ix+1)
        break
