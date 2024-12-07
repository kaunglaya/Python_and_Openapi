import random

min = 1
max = 49

def numbers():
    random_numbers1 = [] #=list("random_numbers1")
    random_numbers = random.sample(range(min,max),7) #從1~49的範圍中會隨機抽取7個號碼
    random_numbers1 = sorted(random_numbers[:6])
    #normal_numbers = sorted(random_numbers[:6]) #會將隨機的號碼由小到大排序
    special_number = random_numbers[-1] #隨機號碼中最後一個會被當作特別號碼
    return random_numbers1,special_number
    
def main():
    random_numbers1, special_number = numbers()
    print("本期大樂透電腦選號號碼如下:\n")
    for lotto in random_numbers1:
        print(lotto,end=" ")
    print("\n")
    print(f"特別號碼:{special_number}")
    
if __name__ == "__main__":
    main()
