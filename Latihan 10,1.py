dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print(f"{'key':<4}{'value':<6}{'item':<5}")

for key, value in dict.items():
    print(f"{key:<4}{value:<6}{key:<5}")