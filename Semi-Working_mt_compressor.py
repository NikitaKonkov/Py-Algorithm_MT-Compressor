import concurrent.futures
from collections import Counter

with open("README.txt", "r", encoding="utf") as f:
    string = f.read()
    save_str = string
data_set = sorted(set(save_str)) # char set

not_allowed = data_set # removes chars which are in string for compression
fix = 14                # chars are not compatible fix
                        # more fix remove!!!

chars = sorted([char for char in [chr(x) for x in range(fix,128)] if not 0xD800 <= ord(char) <= 0xDFFF and char not in not_allowed]) # Creats Vhars for compression


str_length = 2  # Can be modified 2/3/4 it depends
min_freq = 2    # how often
def fs0(str):   # per core sim finder
    return [mc[0] for mc in Counter(str[i:i + str_length] for i in range(len(str) - str_length + 1)).most_common(1) if mc[1] > min_freq]
def fs1(str):
    return [mc[0] for mc in Counter(str[i:i + str_length] for i in range(len(str) - str_length + 1)).most_common(1) if mc[1] > min_freq]
def fs2(str):
    return [mc[0] for mc in Counter(str[i:i + str_length] for i in range(len(str) - str_length + 1)).most_common(1) if mc[1] > min_freq]
def fs3(str):
    return [mc[0] for mc in Counter(str[i:i + str_length] for i in range(len(str) - str_length + 1)).most_common(1) if mc[1] > min_freq]
def fs4(str):
    return [mc[0] for mc in Counter(str[i:i + str_length] for i in range(len(str) - str_length + 1)).most_common(1) if mc[1] > min_freq]
def fs5(str):
    return [mc[0] for mc in Counter(str[i:i + str_length] for i in range(len(str) - str_length + 1)).most_common(1) if mc[1] > min_freq]
def fs6(str):
    return [mc[0] for mc in Counter(str[i:i + str_length] for i in range(len(str) - str_length + 1)).most_common(1) if mc[1] > min_freq]
def fs7(str):
    return [mc[0] for mc in Counter(str[i:i + str_length] for i in range(len(str) - str_length + 1)).most_common(1) if mc[1] > min_freq]



if __name__ == '__main__':
    s = save_str
    print(s.__sizeof__())
    counter = 0
    cache = ""
    with concurrent.futures.ProcessPoolExecutor() as executor:
      for _ in range(255):
        x0 = s[:len(s) // 2]  # 2 string split up to 8 threads
        x1 = s[len(s) // 2:]

        y0 = x0[:len(x0) // 2] # 4
        y1 = x0[len(x0) // 2:]
        y2 = x1[:len(x1) // 2]
        y3 = x1[len(x1) // 2:]

        z0 = y0[:len(y0) // 2] # 8
        z1 = y1[:len(y1) // 2]
        z2 = y2[len(y2) // 2:]
        z3 = y3[len(y3) // 2:]
        z4 = y0[len(y0) // 2:]
        z5 = y1[len(y1) // 2:]
        z6 = y2[:len(y2) // 2]
        z7 = y3[:len(y3) // 2]

        f1 = executor.submit(fs0, z0)
        f2 = executor.submit(fs1, z1)
        f3 = executor.submit(fs2, z2)
        f4 = executor.submit(fs3, z3)
        f5 = executor.submit(fs4, z4)
        f6 = executor.submit(fs5, z5)
        f7 = executor.submit(fs6, z6)
        f8 = executor.submit(fs7, z7)

        similarity_list = []    # found sim collector
        similarity_list.extend(list(f1.result()))
        similarity_list.extend(list(f2.result()))
        similarity_list.extend(list(f3.result()))
        similarity_list.extend(list(f4.result()))
        similarity_list.extend(list(f5.result()))
        similarity_list.extend(list(f6.result()))
        similarity_list.extend(list(f7.result()))
        similarity_list.extend(list(f8.result()))

        if not set(similarity_list): # if NO sim anymore break
            FIN = chr(len(data_set))+"".join(data_set)+ chr(counter) + cache + s # Final compressed data
            with open("../testfile.nik", "w", encoding="utf") as f:
                f.write(FIN)
                print(FIN.__sizeof__())
                print("finish")
            break
        else:
            for x in sorted(set(similarity_list)):  # replaces similarities with another char
                cache += x # stores paar similarities
                s = s.replace(x, chars[counter]) # compression part
                counter += 1


