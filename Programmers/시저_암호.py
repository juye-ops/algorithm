def solution(s, n):
    small = "abcdefghijklmnopqrstu"
    large = small.upper()

    return "".join(map(lambda x: str(chr(65+((ord(x)-65+n)%26))) if x.isupper() else str(chr(97+((ord(x)-97+n)%26))) if x != " " else " ", s))