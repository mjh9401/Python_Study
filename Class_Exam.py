
class Item:
    def __init__(self,name,price,weight,isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    
    def sale(self):
        print(f"[{self.name}] 판매가격은 [{self.price}]")
    def discard(self):
        if self.isdropable:
            print(f"[{self.name}] 버렸습니다.")
        else:
            print(f"[{self.name}] 버릴 수 없습니다.")

class WearableItem(Item):
    def __init__(self, name, price, weight, isdropable,effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    
    def wear(self):
        print(f"[{self.name}] 착용했습니다. {self.effect}")

class UsableItem(Item):
    def __init__(self, name, price, weight, isdropable,effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect

    def use(self):
        print(f"[{self.name}] 사용했습니다. {self.effect}")

sword= WearableItem("명검",30000,4,True,"체력증가 5000")
sword.wear()
sword.sale()
sword.discard()

potion = UsableItem("체력포션",500,1,False,"체력 500 회복")
potion.use()
potion.sale()
potion.discard()