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
    def __init__(self, info):
        infos=info.split('\t')
        self.studentid=infos[0]
        self.name=infos[1]
        self.mid=info[2]
        self.final=info[3][:-1]
        self.avg=(int(self.mid)+int(self.final))/2
        self.grade='A' # 성적 처리 어떻게 할 거니?
    @property
    def infos(self):
        pass


class Database:
    def __init__(self, filename='Student.txt'):
        students=[]
        self.filename=filename
        # 파일명이 안주어졌을 때도 핸들링하나?
        if not os.path.isfile(filename):
            print('기본 파일인 \'Student.txt\'를 엽니다')
            # 파일 열고 한 줄씩 읽으면서 각각 Student 생성해주기
        else:
            fr=open(self.filename)
            for line in fr:
                students.append(Student(line))
            fr.close()

    def show(self):
        pass

    def search(self):
        pass

    def changescore(self):
        pass

    def searchgrade(self):
        pass

    def add(self):
        # student 객체 생성하기
        pass

    def remove(self):
        pass

    def quit(self):
        # 끝내기
        pass


def main():
    filename = input('Filename : ')
    db = Database(filename)
    while True:
        comm = input('')
        if comm == 'quit' :
            db.quit()
        elif comm == 'show':
            db.show()
#  filename=input('Filename: ')
#
#
# while True :
#     comm = input('')
#     if comm == 'quit' :
#     else comm == 'show'


main()

## 클래스로 만들라고?!
