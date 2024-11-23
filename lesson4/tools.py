PI = 3.1415926

class Person:
    '''
    我是person
    '''
    def __init__(self,name:str,age:int):
        self.name = name #attribute 儲存值
        self.age = age #attribute
#實體方法(instance method)
    def echo(self):
        print(f'我的名字是:{self.name}')
        print(f'我的歲數是:{self.age}')

class Student(Person):
    '''
    我是學生
    '''
    def __init__(self,name:str,age:int,score:int):
        super().__init__(name=name,age=age) #將上面的def init(self)的名字跟歲數繼承
        #super() 可以將原有多個儲存值寫在一起後繼承 -> 用一個程式碼代表
        self.__score = score

    @property #與屬性一樣故不用() 只能傳出去 無法傳入 所以不能修改
    def score(self)->int:
        return self.__score #分數會被保護 無法被修改

    def echo(self):
        super().echo() #將上面的def echo(self)的名字跟歲數繼承下來
        print(f'我的分數是:{self.score}')

def get_status(bmi:float)->str:
    '''
    docstring
    Parameter:
        bmi:bmi值可以整數或浮點數
    Return:str
    '''
    if bmi >= 35 :
        bmi_str = '重度肥胖'
    elif bmi >= 30 :
        bmi_str = '中度肥胖'
    elif bmi >= 27 :
        bmi_str = '輕度肥胖'
    elif bmi >= 24 :
        bmi_str = '過重'
    elif bmi >= 18.5 :
        bmi_str = '正常範圍'
    else :
        bmi_str = '過輕' 
    return bmi_str
    
def BMI_math(height_cm:float, weight_kg:float) -> float:
    height_m = round(height_cm/100, 2)
    bmi_kg_m2 = round(weight_kg/(height_m**2), 2)
    bmi_str = get_status(bmi_kg_m2)
    return bmi_kg_m2, bmi_str
