def caesar(ch, step):
    eng = [chr(i) for i in range(97, 123)]
    rus = [chr(i) for i in range(1072, 1104)]
    if ch in eng or ch in rus:
        return chr(ord(ch) + step)
    else:
        return ch
def is_valid_text(text):
    while text.isspace() or text == "":
        text = input("Ошибка! Введи хоть какой-то текст:\n")
    return text

def is_valid_num(step):
    while True:
        if step.isdigit() or (step[0] == "-" and step[1:].isdigit()):
            return int(step)
        else:
            step = input("Ошибка! Введи целое число:\n")

def create_result(text, step):
    result = ""
    for i in range(len(text)):
        result += caesar(text[i], step)
    return result

def main():
    print("хелоу! это программа по шифрованию/дешифрованию текста по шифру Цезаря.\n")
    print("особенности программы:\n• программа работает ТОЛЬКО с русским/английским языком.\n• текст может быть смешанным.\n• в русском языке, символ \"ё\"/\"Ё\". будет заменён \"е\"/\"Е\".\n")
    input_text = is_valid_text(input("чо шифруем/дешифруем:\n"))
    input_step = is_valid_num(input("введи шаг шифрования/дешифрования:\n(отрицательный шаг - ДЕШИФРУЕТ текст)\n"))
    print(create_result(input_text, input_step))

main()
