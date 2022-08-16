# 클래스를 사용하는 이유
champion_name = "이즈리얼"
champion_health = 700
champion_attack = 90

print(f"{champion_name}님 소환사의 협곡에 오신 것을 환영합니다.")

champion_name2 = "리신"
champion_health2 = 800
champion_attack2 = 95

print(f"{champion_name2}님 소환사의 협곡에 오신 것을 환영합니다.")

champion_name3 = "야스오"
champion_health3 = 750
champion_attack3 = 92

print(f"{champion_name2}님 소환사의 협곡에 오신 것을 환영합니다.")

def basic_attack(name,attck):
    print(f"{name} 기본 공격 {attck}")

basic_attack(champion_name,champion_attack)
basic_attack(champion_name2,champion_attack2)
basic_attack(champion_name3,champion_attack3)

print("=========================================================================================================")

# class Monter:
#     def say(self):
#         print("나는 몬스터다!")


# goblin = Monter()
# goblin.say()

# 파이썬에서는 자료형도 클래스이다.

# 생성자
# : 인스턴스를 만들 때 호출 되는 메소드

class Monster:
    def __init__(self,health,attack,speed):
        self.health = health
        self.attack = attack
        self.speed = speed
    
    def decreas_health(self,num):
        self.health -= num
    def get_health(self):
        return self.health

# 고블린 인스턴스 생성
goblin = Monster(800,120,300)
goblin.decreas_health(100)
print(goblin.get_health())

# 늑대 인스턴스 생성
wolf = Monster(1500,200,350)
wolf.decreas_health(1000)
print(wolf.get_health())