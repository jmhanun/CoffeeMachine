num = float(input())
if num < 2.0:
    print("Analytic")
elif 2.0 <= num <= 3.0:
    print("Synthetic")
elif num > 3.0:
    print("Polysynthetic")
