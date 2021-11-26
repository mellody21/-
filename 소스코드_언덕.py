mbti = []
print("안녕하세요? 성격유형에 따른 책을 추천해주는 프로그램입니다. 주어지는 질문에 알맞게 대답해주세요! *정확한 성격유형 검사가 아닙니다. 재미로만 즐겨주세요!")
print("당신은 주로 어디서 에너지를 얻나요? 1 또는 2를 입력하세요.")
while True :
    A = int(input("1. 밖에서 사람들과 시간을 보낸다. 2. 집에서 혼자 쉬면서 시간을 보낸다. : "))
    if A == 1:
        mbti.append("E")
        break
    elif A == 2:
        mbti.append("I")
        break
    else :
        print ("다시 입력해주세요")   
print(mbti)

print("'사과'하면 생각나는 것을 1개 고르세요. 숫자만 입력해주세요.")
while True :
    B = int(input(" 1. 빨갛다 2. 스티브 잡스 3. 백설공주 4. 사각사각 5. 둥글다 6. 비타민C : "))
    if B == 1 or B == 4 or B == 5:
        mbti.append("S")
        break
    elif B == 2 or B == 3 or B == 6:
        mbti.append("N")
        break
    else :
        print ("다시 입력해주세요")
print(mbti)

print("다음 중 더 나쁘다고 생각하는 사람은 누구인가요? 1 혹은 2를 입력하세요.")
while True :
    C = int(input(" 1. 내가 필기한 노트에 실수로 물을 쏟은 친구 2. 나 몰래 내가 필기한 노트를 사진 찍어간 친구: "))
    if C == 1:
        mbti.append("T")
        break
    elif C == 2:
        mbti.append("F")
        break
    else :
        print ("다시 입력해주세요")
print(mbti)

print("여행을 갈 때 당신의 모습은 무엇인가요? 1 혹은 2를 입력하세요.")
while True :
    D = int(input(" 1. 세세히 계획을 세운다 2. 세세한 계획 없이 즉흥적으로 여행을 떠난다: "))
    if D == 1:
        mbti.append("J")
        break
    elif D== 2:
        mbti.append("P")
        break
    else :
        print ("다시 입력해주세요")
print(mbti)

print("성격유형 테스트가 끝났습니다. 책 추천을 시작합니다.")
if mbti == ['I', 'N', 'T', 'J']:
    print("공감의 언어, 정용실")
if mbti == ['E', 'S', 'F', 'J']:
    print("빌 캠벨, 실리콘 밸리의 위대한 코치, 에릭 슈미트 외")
if mbti == ['I', 'S', 'T', 'J']:
    print("오베라는 남자, 프레드릭 배크만")
if mbti == ['E', 'N', 'F', 'J']:
    print("타인의 고통, 수전 손택")
if mbti == ['I', 'S', 'F', 'J']:
    print("꽃을 보듯 너를 본다, 나태주")
if mbti == ['I', 'N', 'F', 'P']:
    print("상처 받지 않는 영혼, 마이크 싱어")
if mbti == ['I', 'S', 'T', 'P']:
    print("도구와 기계의 원리, 데이비드 맥컬레이")
if mbti == ['E', 'S', 'T', 'J']:
    print("이정현의 집밥 레스토랑, 이정현")
if mbti == ['E', 'N', 'T', 'J']:
    print("디즈니만이 하는 것, 로버트 이야기")
if mbti == ['E', 'S', 'F', 'P']:
    print("유쾌함의 기술, 앤서니 T")
if mbti == ['E', 'S', 'T', 'P']:
    print("노인과 바다, 어니스트 헤밍웨이")
if mbti == ['I', 'N', 'F', 'J']:
    print("언어의 온도, 이기주")
if mbti == ['I', 'S', 'F', 'P']:
    print("뉴욕규림일기, 김규림")
if mbti == ['E', 'N', 'F', 'P']:
    print("지적 대화를 위한 넓고 얕은 지식 제로, 채사장")
if mbti == ['I', 'N', 'T', 'P']:
    print("떨림과 울림, 김상욱")
if mbti == ['E', 'N', 'T', 'P']:
    print("말투를바꿨더니 관계가 찾아왔습니다, 김범준")
print ("프로그램이 종료되었습니다. 이용해주셔서 감사합니다.")

input()
