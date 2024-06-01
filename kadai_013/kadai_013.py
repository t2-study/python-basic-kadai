def calculate_total(price, tax):
    #taxは10%の場合、10を入力するため、100で割る
    total = price * (1 + tax / 100)
    print(f"{total}円")

calculate_total(1000, 10)