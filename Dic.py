# 딕셔너리
# : 사전형태의 자료형

# 딕셔너리 만들기
stock_a ={"삼성전자":82000, "LG전자":150000}
stock_b ={
    "삼성전자" : [81000,35000,566000,866000,22000],
    "LG전자" : (23000,98000,56000,10000,20000),
}

stock_c = {
    "삼성전자" : {
        "현재가" : 82000,
        "보유수량" : 5,
        "매수단가" : 84000
    }
}

# print(stock_a)
# print(stock_b)
# print(stock_c)

# 딕셔너리 접근
print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["보유수량"])

# 딕셔너리 할당하기
stock_a["삼성전자"] = 85000
print(stock_a)

# 딕셔너리 삭제하기
del stock_a["LG전자"]
print(stock_a)


# 딕셔너리 함수
stock_d={
    "삼성전자" : 82000,
    "SK하이닉스" : 123000,
    "NAVER" : 370000,
    "카카오" : 130000
}

# items() : 키와 데이터 쌍
print(stock_d.items())

for item in stock_d.items():
    print(item)

# keys() : 키
for key in stock_d.keys():
    print(key)

# values() : 데이터
for value in stock_d.values():
    print(value)