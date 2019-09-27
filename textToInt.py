zeros = {"thousand":3, "million":6, "billion":9, "trillion":12}
numbers = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9,
           "ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19,
           "twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90}
def textToInt(text):
    total = 0
    counter = 0
    for x in text.lower().replace(" and", '').split(' '):
        if x in numbers:
            counter += numbers[x]
            continue
        if x == "hundred":
            counter *= 100
            continue
        if x in zeros:
            counter *= (10 ** (zeros[x]))
        total += counter
        counter = 0
    total += counter
    return total
