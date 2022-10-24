import os
import csv
from post import Post

# 파일경로
file_path = "./csv/data.csv"
# post 객체를 저장할 리스트
post_list = []

# data.csv 파일이 있다면
if os.path.exists(file_path):
    # 게시글 로딩
    print("게시글 로딩중...")
    f = open(file_path,"r",encoding="utf-8")
    reader = csv.reader(f)
    for data in reader :
        # Post 인스턴스 생성하기
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)

else:
    # 파일 생성하기
    f = open(file_path,"w", encoding="utf8", newline="")
    f.close()

# 게시글 쓰기
def write_post():
    """게시글 쓰기 함수"""
    print("\n\n 게시글 쓰기 -")
    title = input("제목을 입력해주세요\n>>>")
    content = input("내용을 입력해주세요\n>>>")
    # 글 번호
    id = post_list[-1].get_id()+1
    post = Post(id,title,content,0) 
    post_list.append(post)
    print("# 게시글이 등록되었습니다.")

def list_post():
    """게시글 출력 함수"""
    print(post_list)


# 메뉴 출력하기
while True:
    print("\n\n- FASTCAMPUS BLOG")
    print("- 메뉴를 선택해주세요 -")
    print("1. 게시글 쓰기")
    print("2. 게시글 목록")
    print("3. 프로그램 종료")

    try:
        choice = int(input(">>>"))
    except ValueError:
        print("숫자를 입력해주세요")
    else:
        if choice == 1 :
            write_post()
        elif choice == 2:
            list_post()
        elif choice == 3:
            print("프로그램 종료")
            break