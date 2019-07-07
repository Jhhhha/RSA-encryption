import numpy

#…………………………………………………………………………………………………………模的相关知识………………………………………………………………………………………………
def mod_reversi(x, y): #求模的逆元
    if x % y == 0:
        return 0, 0
    if(x % y == 1):
        return 1, -(x // y);
    t2 = -(x // y )
    t, t_ = mod_reversi(y, x % y)
    return t_, t+t2*t_

def miller_rabin(n, k=50): #素数检验
    if n < 6:
        return [False, False, True, True, False, True][n]
    elif n & 1 == 0:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        s = s + 1
        d = d >> 1
    for _ in range(k):
        a = numpy.random.randint(pow(2,63))
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            elif x == n - 1:
                a = 0
                break
        if a:
            return False
    return True


def proBin(w):  # w表示希望产生位数
    list = []
    list.append(1)  #最高位定为1
    for i in range(w - 2):
        c = numpy.random.randint(0, 2)
        list.append(c)
    list.append(1) #最低位也定为1
    ls2 = [str(j) for j in list]
    # print("ls2:",ls2)
    ls3 = ''.join(ls2)
    # print('ls3',ls3)

    b = int(ls3[0])
    for i2 in range(len(ls3) - 1):
        b = b << 1
        b = b + int(ls3[i2 + 1])
    # d = long(b)
    # print("b", b)
    return b

def getPrime(bit): #获得大素数
    w = proBin(bit)
    while (miller_rabin(w, 50) == False):
        w = proBin(bit)
    return w

def getKeys(p, q, bit): #获得公钥和私钥对
    e = getPrime(bit)
    n1 = (p-1)*(q-1)
    d,_ = mod_reversi(e,n1)
    d = d % n1
    return e, d

#…………………………………………………………………………………………………………密文的转换………………………………………………………………………………………………
def ints2bytes(ints, size):
    res = b''
    for i in ints:
        res += i.to_bytes(size,byteorder='little')
    return res

def bytes2str(bytes_):
    str = ''
    for i in bytes_:
        str += chr(i)
    return str

def str2bytes(str):
    res = b''
    for j in str:
        tmp = ord(j)
        res += bytes([tmp])
    return res

def bytes2ints(bytes_, size):
    res = []
    count = len(bytes_) // size
    for i in range(count):
        t = bytes_[i * size : (i+1) * size]
        tmp = int.from_bytes(t, byteorder='little')
        res.append(tmp)
    return res

def ints2str(ints, size):
    bytes_ = ints2bytes(ints, size)
    return bytes2str(bytes_)

def str2ints(str, size):
    byte_ = str2bytes(str)
    return bytes2ints(byte_, size)
#………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………



#…………………………………………………………………………………………………………明文的转换………………………………………………………………………………………………
def ints2str_M(ints, bit):
    res = b''
    for i in ints:
        res += i.to_bytes(bit,byteorder= 'little').rstrip(b'\x00')
    return res.rstrip(b'\x00')



def str2ints_M(str, byte):
    bytes_ = str.encode()
    res = []
    for i in range((bytes_.__sizeof__()-33) // byte + 1):
        t = bytes_[i*byte : (i+1)*byte]
        tmp = int.from_bytes(t,byteorder='little')
        res.append(tmp)
    return res
#………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………

def bytes2ints_(str):
    hexs = str.split('0x')
    del hexs[0]
    res = []
    for hex in hexs:
        res.append(int(hex,16))
    print(res)
    return res


# print(k2)
# print(type(k2))
# bytes2ints_(k2)


# def bytes2ints(bytes):


#……………………………………………………………………………………………………………加密和解密…………………………………………………………………………………………………
def encrypt(str, e, N, size):
    ints = str2ints_M(str, size)
    print("明文变成数字：", ints)
    res = []
    for m in ints:
        res.append(pow(m,e,N))
        # print(res)
    print("密文的噢 :", hex(N))
    str = ""
    for m in res:
        str += hex(m)
    # print("str:", str)
    return str

def decrypt(str, d, N, size):
    ints = bytes2ints_(str)
    print(ints)
    print("密文变成数字", ints)
    res = []
    for m in ints:
        res.append(pow(m, d, N))
    print("解码后的数字:" , res)
    res = ints2str_M(res, size).decode()
    return res
#………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………

if __name__ == '__main__':
    bit = 512
    p = getPrime(bit)
    print("p:",hex(p))
    q = getPrime(bit)
    print("q:", hex(q))
    n = p * q
    print("n:", hex(n))
    n1 = (p-1)*(q-1)
    print("n1:", hex(n1))
    e, d = getKeys(p,q,32)
    print("e:", hex(e))
    print("d:", hex(d))

    str = "密码学真是一门有意思的学科！！！叶广智是一个弟弟！！！密码学真是一门有意思的学科！！！叶广智是一个弟弟！！！密码学真是一门有意思的学科！！！叶广智是一个弟弟！！！密码学真是一门有意思的学科！！！叶广智是一个弟弟！！！密码学真是一门有意思的学科！！！叶广智是一个弟弟！！！密码学真是一门有意思的学科！！！叶广智是一个弟弟！！！"
    print("\n明文是：", str)

    p = encrypt(str, e, n, 64)
    print("\n密文：")
    print(p,'\n')

    m = decrypt(p, d, n ,64)
    print("解密后：", m)
