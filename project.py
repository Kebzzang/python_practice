# 주석달기!!
# 학생 포멧에 맞춰서 프린트하기
# class 형식
# 우리는 객체지향적인 삶을 삽시다
#  정말 이렇게 스튜던트 인포 하나만 띡 만들거야?
# 클래스는 여러 개로 분리해야 하지 않겠니?
## class Student
## class Database
### Database has students
### has a 관계 그림을 생각해
### https://wikidocs.net/21053

### https://jinmay.github.io/2019/11/23/python/python-class-first/

### https://www.daleseo.com/python-property/
import os


class Student:
    # 학생 정보 수정하는 거 있어야 함
    # mid 와 final
    def __init__(self, info):
        infos = info.split('\t')
        print(infos)
        self.studentid = infos[0]
        self.name = infos[1]
        self.mid = infos[2]
        self.final = infos[3][:-1]
        self.avg = (int(self.mid) + int(self.final)) / 2
        self.grading(self.avg)

    def __str__(self):
        return "{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(self.studentid, self.name, self.mid, self.final, self.avg, self.grade)

    def grading(self, avg):
        if avg > 90:
            self.grade = 'A'
        elif avg > 80:
            self.grade = 'B'
        elif avg > 70:
            self.grade = 'C'
        elif avg>60:
            self.grade='D'
        else:
            self.grade='F'


class Database:
    def __init__(self, filename):
        self.students = []
        print('Here is file name', filename)

        # 아무것도 입력안한채로 넘어왔을 때
        if filename == '':
            print("here1")
            self.filename = "students.txt"
        # 파일명이 넘어왔으면
        else:
            print("Here2")
            self.filename = filename

        fr = open(filename, 'r')

        for line in fr:
            st = Student(line)
            self.students.append(st)
        fr.close()
        self.show()

    def show(self):
        print(self.students)


    def search(self):
        print("SEARCH")

    def changescore(self):
        print("CHANGESCORE")

    def searchgrade(self):
        print("SEARCHGRADE")

    def add(self):
        # student 객체 생성하기
        print("ADD")

    def remove(self):
        print("REMOVE")

    def quit(self):
        # 끝내기
        print('Quit Here')


def main():
    filename = input('Filename : ')
    db = Database(filename)
    while True:
        comm = str.lower(input('명령어를 입력하세요: '))
        if comm == 'quit':
            db.quit()
            break
        elif comm == 'show':
            db.show()
        elif comm == 'search':
            db.search()
        elif comm == 'remove':
            db.remove()
        else:  # 커맨드가 이상하면??
            print('***명령어는 show, search, remove 입니다.***')


main()

## 클래스로 만들라고?!
