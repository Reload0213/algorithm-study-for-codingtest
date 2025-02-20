input = 22

# 소수는 자기 자신과 1이외 에는 아무것도 나눌 수 없다.

def find_prime_list_under_number(number):
    prime_list = []
    
    for n in range(2, number + 1):
        # for i in range(2, n): # 자신은 어차피 나누어지니까 n-1까지
        for i in prime_list: # 자신보다 작은 소수(즉 prime_list)로 나누어 떨어지지 않는다면
            if n % i == 0:
                break
        else:
            prime_list.append(n)
                
    return prime_list


result = find_prime_list_under_number(input)
print(result)