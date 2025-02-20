input = "abadabac"

def find_not_repeating_char_array(string):
    alphabet_occurrence_array = [0] * 26 # 빈도수 배열

    # 아스키 코드: 각 문자들을 숫자(컴퓨터가 알아볼 수 있는)로 지정해 둔 값들
    # chr() 아스키 값을 통해 해당 문자를 반환
    # ord() 문자를 통해 아스키 코드 값 반환

    for char in string:
        if not char.isalpha(): # 알파벳인지 검사(공백 등등 알파벳인지 검증)
            continue
        current_index = ord(char) - ord('a') # 해당 문자를 현재 인덱스로 치환
        alphabet_occurrence_array[current_index] += 1 # 빈도수 배열에 현재 인덱스에 해당하는 값을 추가가
        
    not_repeating_char_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_char_array.append(chr(index + ord('a')))
            
    for char in string:
        if char in not_repeating_char_array:
            return char
            
    return '_'

result = find_not_repeating_char_array
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 = _ 현재 풀이 값 =", result("aaaaaaaa"))