from math import ceil

def calc_account(m):
    # 初乗り距離と運賃
    initial_distance = 1700
    initial_fare = 610

    # それ以降の増加距離と増加運賃
    increment_distance = 315
    increment_fare = 80

    # 距離が0m以下の場合
    if m <= 0:
        return None

    # 初乗り距離までの場合
    if m <= initial_distance:
        return initial_fare

    # 初乗り距離を超えた場合
    # 初乗り運賃に加えて、315m毎に80円増える
    excess_distance = m - initial_distance
    increments = ceil(excess_distance / increment_distance)
    total_fare = initial_fare + increments * increment_fare

    return total_fare


if __name__ == "__main__":
    from argparse import ArgumentParser
    import sys

    parser = ArgumentParser(description="引数に金額を渡すとタクシー料金を計算します")
    parser.add_argument("distance", help="走行距離(メートル)", type=int)

    args = parser.parse_args()
    d = args.distance
    a = calc_account(d)
    if a == None:
        print("不正な数値です、1以上の整数値を渡してください", file=sys.stderr)
        sys.exit(1)
    print(f"走行距離 {args.distance}m => 金額は {calc_account(args.distance)}円です。")


