def roman(num):
    if num == 1:
        return "I"
    if num == 2:
        return "II"

    def test_3():
        assert roman(3) == "III"

        def roman(num):
            if num <= 3:
                return "I" * num

    def test_4():
        assert roman(4) == "IV"

    if num == 5:
        return "V"


def test_9():
    assert roman(9) == "IX"
    if num == 9:
     return "IX"

    def roman(num):
        values = [
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        result = ""

        for value, symbol in values:
            while num >= value:
                result += symbol
                num -= value

        return result



