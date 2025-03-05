with open("../testfile.nik", "r", encoding='utf-8') as f:  # open compressed file
    f = f.read()

fix = 14  # bs fix
not_allowed = f[1:ord(f[0])+1]  # char set for filter
chars = sorted([char for char in [chr(x) for x in range(fix, fix+ord(f[0])+1)]
                if not 0xD800 <= ord(char) <= 0xDFFF and char not in not_allowed])  # char list for decompression

# Extract the substring that was used in the NumPy array
substring = f[ord(f[0])+2:ord(f[ord(f[0])+1])*2+ord(f[0])+2]

# Manually reshape the list into pairs (2 columns)
cache = []
for i in range(0, len(substring), 2):
    if i+1 < len(substring):  # Make sure we have a pair
        cache.append([substring[i], substring[i+1]])

# Reverse the list (equivalent to [::-1])
cache.reverse()

s = f[ord(f[ord(f[0])+1])*2+ord(f[0])+2:]  # compressed part

for x in range(len(cache)):  # decompression part
    s = s.replace(chars[len(cache)-x-1], "".join(cache[x]))

with open("testfile.txt", "r", encoding="utf-8") as f:  # open original file to check
    string = f.read()

if s == string:
    print("ok")
    print(s)