def convert_to_roman(num):
    result = ""
    poops = {
    "M":1000,
    "CM":900,
    "D":500,
    "CD":400,
    "C":100,
    "XC":90,
    "L":50,
    "XL":40,
    "X":10,
    "IX":9,
    "V":5,
    "IV":4,
    "I":1
    }
    for item in poops:
        while(num >= poops[item]):
            result += item
            num = num - poops[item]
    print(result)
    return result


# def convert_to_roman(num):
#     if(num == 0):
#         return False
#     result = ""
#     while num >= 1000:
#         result += "M"
#         num = num - 1000
#     if(num >= 900):
#         result += "CM"
#         num = num - 900
#     if(num >= 500):
#         result += "D"
#         num = num - 500
#     if(num >= 400):
#         result += "CD"
#         num = num - 400
#     while(num >= 100):
#         result += "C"
#         num = num - 100
#     if(num >= 90):
#         result += "XC"
#         num = num - 90
#     if(num >= 50):
#         result += "L"
#         num = num - 50
#     if(num >= 40):
#         result += "XL"
#         num = num - 40
#     while(num >= 10):
#         result += "X"
#         num = num - 10
#     if(num >= 9):
#         result += "IX"
#         num = num - 9
#     if(num >= 5):
#         result += "V"
#         num = num - 5
#     if(num >= 4):
#         result += "IV"
#         num = num - 4
#     while(num >= 1):
#         result += "I"
#         num = num - 1
#     print(result)
#     return result


convert_to_roman(1944)