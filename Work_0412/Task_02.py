# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления 
# данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q


import os.path


def incode():
    new_stroka = ""
    pred_simb = ""
    count = 1

    if os.path.exists("text_words.txt"):
        with open("text_words.txt") as S:
            stroka = S.read()
    else:
        print("Запрашиваемого текстового файла не существует.")

    with open("text_code_words.txt", "w") as rec_stroka:
        for sled_simb in stroka: 
            if sled_simb != pred_simb:
                if pred_simb:
                    new_stroka = new_stroka + str(count) + pred_simb
                count = 1
                pred_simb = sled_simb
            else: 
                count += 1 
        new_stroka = new_stroka + str(count) + pred_simb 
        rec_stroka.write(new_stroka)
    return new_stroka       


def outcode():
    de_stroka = ""
    count = ""

    with open("text_code_words.txt") as V:
        vs_stroka = V.read()
        for simb in vs_stroka:
            if simb.isdigit():
                count = count + simb
            else:
                de_stroka = de_stroka + simb*int(count)
                count = ""
    return de_stroka


n = input("Введите набор букв для проверки работы кодировки/раскодировки.\n")
with open("text_words.txt", "w") as F:
    F.write(n)
a = incode()
b = outcode() 
print(b)