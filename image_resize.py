from PIL import Image
from resizeimage import resizeimage
import numpy as np
import binascii

#Resize photo to 100x100 pixel dimmension
def resize_photo(image):
    with open(photo, 'r+b') as file:
        with Image.open(file) as imge:
            cover = resizeimage.resize_cover(img, [100, 100])
            cover.save('test.jpg', image.format)



#Convert new image to bitstring
def img_to_bits(image):
# Read data and convert to a list of bits
    in_bytes = np.fromfile(image, dtype = "uint8")
    in_bits = np.unpackbits(in_bytes)
    bits = np.array(in_bits)
    str_bits = ""
    # str_bits = bits.tostring()
    for bit in bits:
        str_bits += str(bit)
    return str_bits
str_bits = img_to_bits('test.jpg')
# print(str_bits)
print(len(str_bits))
def countLetters(word):
    freq={}
    for i in range(len(word)//8):
        letter = word[i:i+8]
        freq[letter] = 0
    for i in range(len(word)//8):
        letter = word[i:i+8]
        freq[letter] += 1
    total = sum(freq.values())
    for i in freq.keys():
        freq[i] /= total
    return freq
freq = countLetters(str_bits)
# a = {k: v / total for k, v in freq}
# print(a)

## TODO: Figure out how to encode freq_table into ASCII characters
## TODO: Create Decode Trie
## TODO: Decode






# Convert the list of bits back to bytes and save
# out_bits = np.array(data)
# print(np.all(out_bits == in_bits))
# out_bytes = np.packbits(out_bits)
# print(np.all(out_bytes == in_bytes))
# out_bytes.tofile(out_name)



# def access_bit(data, num):
#     base = int(num/8)
#     shift = num % 8
#     return (data[base] & (1<<shift)) >> shift
#
# with open("test.jpg", "r+b") as file:
#   img = file.read()
#   data = bytearray(img)
#   bits = [access_bit(data,i) for i in range(len(data)*8)]
#   print(bits)
#   print(len(bits))
#
#
# str_bits = ""
# for bit in bits:
#     str_bits += str(bit)
#
# def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
#     n = int(bits, 2)
#     return int2bytes(n).decode(encoding, errors)
#
# def int2bytes(i):
#     hex_string = '%x' % i
#     n = len(hex_string)
#     return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
#
# print(text_from_bits("00000010" + str_bits))
