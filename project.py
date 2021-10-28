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
import sys


# 데이터베이스는 학생들을 가진다.
# has-a 관계 : belongs to 관계
# 객체가 한 객체의 필드로써 존재한다


# 학생 클래스
class Student:
    # 학생 정보 수정하는 거 있어야 함
    # mid 와 final 계산하고,
    def __init__(self, info):
        print(info)
        self.grade = 'F'
        infos = info.split('\t')
        print(infos)
        self.id = infos[0]
        self.name = infos[1]
        self.mid = infos[2]
        self.final = infos[3][:-1]
        self.avg = (int(self.mid) + int(self.final)) / 2
        self.grading(self.avg)

    def __str__(self):
        return "{:10}\t{:>13}\t{:^8}\t{:^6}\t{:^7.1f}\t\t{:^6}".format(self.id,
                                                                       self.name,
                                                                       self.mid,
                                                                       self.final,
                                                                       self.avg,
                                                                       self.grade)

    # 알파벳 성적 부여
    def grading(self, avg):
        if avg >= 90:
            self.grade = 'A'
        elif avg >= 80:
            self.grade = 'B'
        elif avg >= 70:
            self.grade = 'C'
        elif avg >= 60:
            self.grade = 'D'

    @property
    def mid(self):
        return self.mid

    @mid.setter
    def mid(self, mid):
        self.mid = mid

    @property
    def final(self):
        return self.final

    @final.setter
    def final(self, final):
        self.final = final


# 데이터베이스 클래
class Database:
    def __init__(self, filename):
        self.students = []
        self.filename = filename
        fr = open(filename, 'r')
        # 파일 read 하고 닫아주기
        for line in fr:
            self.students.append(Student(line))
        fr.close()
        self.show()

    def show(self):
        print(
            "{:10}\t{:>13}\t{:8}\t{:>5}\t{:>7}\t\t{:>5}\n--------------------------------------------------------------------------------".format(
                "Student",
                "Name",
                "Mideterm",
                "Final",
                "Average",
                "Grade"))
        # 저장된 student 객체들을 학생의 평균에 따라 정렬한 뒤 출력한다
        self.students.sort(key=lambda st: -st.avg)
        # 만약 파일에 학생 정보가 존재하지 않는다면 학생이 없다고 알려줌

        for student in self.students:
            print(student)
        print()

    def search(self):
        st = input("Student ID:")
        result = "NO SUCH PERSON"
        for student in self.students:
            if student.id == st:
                result = "{:10}\t{:>13}\t{:8}\t{:>5}\t{:>7}\t\t{:>5}\n--------------------------------------------------------------------------------\n".format(
                    "Student",
                    "Name",
                    "Mideterm",
                    "Final",
                    "Average",
                    "Grade") + str(student)

        print(result)
        print()

    def changescore(self):
        st = input('Student ID: ')
        for student in self.students:
            print(student)

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
    # 일단
    filename = "students.txt"
    # 사용자가 파일 이름도 같이 입력을 해줬다면, 넘어오는
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    print(filename)
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
            print('***명령어는 show, search, changescore, remove, searchgrade, quit 입니다.***')


main()

# 클래스로 만들라고?!
