# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    a, b, c = map(str, input().split())
    sim1 = a
    sim2 = b
    sim3 = c
    code1 = ord(a)
    code2 = ord(b)
    code3 = ord(c)
    print("Код символа " + str(sim1) + " Равен " + str(code1) + "\n" + "Код символа " + str(sim2) + " Равен " + str(code2) + "\n" + "Код символа " + str(sim3) + " Равен " + str(code3))
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()