# def solution(n):
#     numeral = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     roman = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

#     # for num in numeral:
#     #     roman_in = numeral.index(num)
#     #     print(
#     #         f"the roman eqivilent of {num} is {roman[roman_in]}")

#     if n in numeral:
#         roman_in = numeral.index(n)
#         print(
#             f"the roman eqivilent of {n} is {roman[roman_in]}")

#     # return string(myval)
# solution(3)


def solution(n):
    numerals = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40,
                "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
    range_flag = None
    for roman_numeral, integer in numerals.items():
        if integer == n:
            return roman_numeral

        if n > integer:
            range_flag = roman_numeral
    reminder = n - numerals[range_flag]
    return range_flag + solution(reminder)


print(solution(4))
