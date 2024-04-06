def calculate_bulls_to_release(N, K):
    bulls_per_family = N // K
    bulls_to_release = N - bulls_per_family * K
    return bulls_to_release

N = int(input("Введите количество добытых Таккаром быков: "))
K = int(input("Введите количество семей в племени Урус: "))

bulls_to_release = calculate_bulls_to_release(N, K)
print(f"Чтобы честно поделить добычу между всеми семьями, нужно отпустить на волю {bulls_to_release} быков.")
