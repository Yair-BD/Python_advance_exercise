def parse_ranges(ranges_string=""):
    split_list = (n.split("-") for n in ranges_string.split(","))
    cuples = (n for nun, mun in split_list for n in range(int(nun), int(mun)+1))
    return cuples


print(list(parse_ranges("1-2,4-5,8-100")))