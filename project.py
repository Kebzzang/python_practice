# 주석달기!!
# 학생 포멧에 맞춰서 프린트하기
# class 형식
# 우리는 객체지향적인 삶을 삽시다

class Student:
    def __init__(self):
        self

    def show(self):
        pass

    def search(self):
        pass

    def changescore(self):
        pass

    def searchgrade(self):
        pass

    def add(self):
        pass

    def remove(self):
        pass

    def quit(self):
        # 끝내기
        pass


def main():
    fr = open("students.txt", "r")
    # 한 학생씩 읽어서 \t 삭제시켜주고, 각 학생 이름의 리스트에 성적 전부 넣어주기
    print(fr.read())

    fr.close()


main()

## 클래스로 만들라고?!
