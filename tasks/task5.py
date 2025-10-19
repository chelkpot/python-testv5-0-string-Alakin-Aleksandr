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
    outut1 = "Код символа " + str(sim1) + " Равен " + str(code1)
    output2 = "Код символа " + str(sim2) + " Равен " + str(code2)
    output3 = "Код символа " + str(sim3) + " Равен " + str(code3)
    print(outut1)
    print(output2)
    print(output3)
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()