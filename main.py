from greatest_common_factor import GreatestCommonFactor


def main():
    gcf = GreatestCommonFactor(200, 700)
    result = gcf.calculate_gcf()
    print(result)
    gcf2 = GreatestCommonFactor(855, 435)
    result = gcf2.calculate_gcf()
    print(result)
    gcf2 = GreatestCommonFactor(6482, 42)
    result = gcf2.calculate_gcf()
    print(result)

main()