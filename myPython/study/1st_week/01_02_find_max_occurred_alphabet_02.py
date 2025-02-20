def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26 # 빈도수 배열

    # 아스키 코드: 각 문자들을 숫자(컴퓨터가 알아볼 수 있는)로 지정해 둔 값들
    # chr() 아스키 값을 통해 해당 문자를 반환
    # ord() 문자를 통해 아스키 코드 값 반환

    for char in string:
        if not char.isalpha(): # 알파벳인지 검사(공백 등등 알파벳인지 검증)
            continue
        current_index = ord(char) - ord('a') # 해당 문자를 현재 인덱스로 치환
        alphabet_occurrence_array[current_index] += 1 # 빈도수 배열에 현재 인덱스에 해당하는 값을 추가가
        
    # 반복 횟수를 저장한 배열에서 가장 큰 숫자와 해당 알파벳을 반환하도록 아래 설정    
    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index

    return chr(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))