import pay_module

# 변수 사용
print(pay_module.version)

# 함수 사용
pay_module.printAuthor()

# 클래스 사용
pay_info = pay_module.Pay("A230023",13000,"2022-08-16")
print(pay_info.get_pay_info())