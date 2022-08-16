# 예외 발생 클래스 
class PositiveNumberError(Exception):
    def __init__(self):
        super().__init__("양수는 입력 불가")

# raise 구문을 사용해서 에러를 강제로 발생시켜 봅시다.
try:
    num = int(input("음수를 입력해주세요 >>>>>>"))
    if num > 0:
        raise PositiveNumberError
except PositiveNumberError as e:
    print("에러 발생!", e)

