def count_substring(string, sub_string):
    chunkCount = 0
    for i in range(len(string)):     
        chunk = string[i:i+len(sub_string)]
        if chunk == sub_string:
            chunkCount += 1
    return chunkCount

string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)
