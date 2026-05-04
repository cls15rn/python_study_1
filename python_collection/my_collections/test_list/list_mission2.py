# file path: my_collections\\test_list\\list_mission2.py
# module: my_collections.test_list.list.mission2
# 리스트 실습문제 2

"""    키보드로 값들을 입력받아, 요구대로 처리하고 확인 출력 코드를 작성하시오.
입력 내용 :
    국어 점수 : 78.5 (kor : float)
    영어 점수 : 88.7 (eng: float)
    수학 점수 : 93.5 (mat : float)
처리 내용 :
    3명의 학생 점수를 입력 받음, 각 학생의 총점과 평균은 각각 계산함
    학생별 점수는 각 리스트에 저장한 다음, [국어, 영어, 수학, 총점, 평균]
    각 학생 점수를 리스트(sungjuk_list)에 순서대로 저장 처리함
    [[국, 영, 수, 총, 평], [국, 영, 수, 총, 평], [국, 영, 수, 총, 평]]
    3명의 점수의 총합(total_score : int)과 전체평균(average_score : float)를
    계산하시오.
출력 내용 :
    리스트에 저장된 값들을 출력함,   국, 영, 수, 총, 평균 순서로 출력
     -> 점수는 소수점아래 둘째자리까지 표시
    -> format() 사용함
    전체 총점과 전체 평균을 출력하시오.
"""

def practice():
    # pass #함수 선언만 하고, 내용은 나중에 채우고자 할 때 사용함 (내용 없는 빈 함수 선언)
    average = 0
    total = 0
    a_sungjuk = []
    a_sungjuk.append(float(input('국어 점수: ')))
    a_sungjuk.append(float(input('영어 점수: ')))
    a_sungjuk.append(float(input('수학 점수: ')))
    b_sungjuk = []
    b_sungjuk.append(float(input('국어 점수: ')))
    b_sungjuk.append(float(input('영어 점수: ')))
    b_sungjuk.append(float(input('수학 점수: ')))
    c_sungjuk = []
    c_sungjuk.append(float(input('국어 점수: ')))
    c_sungjuk.append(float(input('영어 점수: ')))
    c_sungjuk.append(float(input('수학 점수: ')))
    a_score = []
    a_score.append(float(a_sungjuk[0]))
    a_score.append(float(a_sungjuk[1]))
    a_score.append(float(a_sungjuk[2]))
    a_score.append(a_score[0] + a_score[1] + a_score[2])
    a_score.append(a_score[3] /3)
    total += int(a_score[0] + a_score[1] + a_score[2])
    b_score = []
    b_score.append(float(b_sungjuk[0]))
    b_score.append(float(b_sungjuk[1]))
    b_score.append(float(b_sungjuk[2]))
    b_score.append(b_score[0] + b_score[1] + b_score[2])
    b_score.append(b_score[3] /3)
    total += int(b_score[0] + b_score[1] + b_score[2])
    c_score = []
    c_score.append(float(c_sungjuk[0]))
    c_score.append(float(c_sungjuk[1]))
    c_score.append(float(c_sungjuk[2]))
    c_score.append(c_sungjuk[0] + c_sungjuk[1] + c_sungjuk[2])
    c_score.append(c_score[3] /3)
    total += int(b_score[0] + b_score[1] + b_score[2])
    average = total // 9.0
    print(a_score, b_score, c_score)
    print('전체 총점은 {1}, 전체 평균{0}입니다.'.format(average, total))
    return