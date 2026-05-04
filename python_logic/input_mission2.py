'''
키보드로 값을 입력받아 요구조건대로 처리하고 출력되게 코드를 작성하시오.
기본값을 가진 변수 생성 할당해 둠 :
    total_point = 12500
입력 내용 :
    고객 이름 : 황지니 (custom_name : str)
    결재 금액 : 3000000 (price : int)
처리 내용 :
    결재금액의 5 % 를 포인트(point : float)로 처리
    계산된 포인트를 누적포인트(total_point)에 증가 연산 처리함
출력 내용 :
    황지니 고객님의 사용금액은 3000000 원, 발생 포인트는 15000
    현재 이용하실 수 있는 누적포인트는 162500 점입니다.
'''

total_point = 12500
custom_name = input('이름을 입력하세요: ')
price = int(input("결제 금액을 입력하세요: "))
plus_point = price * 0.05
total_point = total_point + plus_point

print("{} 고객님의 사용급액은 {} 원, 발생 포인트는 {}" \
"현재 이용하실 수 있는 누적 포인트는 {} 점입니다.".format(custom_name, price, plus_point, total_point))