

# 1330
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

# A, B = map(int, input().split())

# if A>B:
    # print(">")
# elif A<B:
    # print("<")
# elif A==B:
    # print("==")

# if와 그 이외의 결과를 출력하는 elif를 사용하는 문제입니다.



# 9498
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 
# 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

# n = int(input())
# if 90<= n <= 100:
    # print("A")
# elif 80<= n <= 89:
    # print("B")
# elif 70<= n <= 79:
    # print("C")
# elif 60<= n <= 69:
    # print("D")
# elif n <60:
    # print("F")

# 숫자 배열을 더 오밀조밀하게 해서 <= 부호를 < 식으로 하는 둥 해서 줄일 순 있는데
# 뭔가 저 배열이 좀더 깔끔해 보여서 선택했습니다.



# 2753
# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.

# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

# 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 
# 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 
# 하지만, 2000년은 400의 배수이기 때문에 윤년이다.

# year = int(input())

# if ((year%4 == 0)and(year%100 !=0) or (year%400 == 0)):
    # print('1')
# else:
    # print('0')

# and와 or을 사용해서 윤년인 경우와 아닌경우는 else를 사용한다.




# 14681

# 흔한 수학 문제 중 하나는 주어진 점이 어느 사분면에 속하는지 알아내는 것이다. 
# 사분면은 아래 그림처럼 1부터 4까지 번호를 갖는다. 
# "Quadrant n"은 "제n사분면"이라는 뜻이다.

# 예를 들어, 좌표가 (12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다. 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.

# 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 
# 작성하시오. 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.


# x = int(input())
# y = int(input())

# if x>0 and y>0:
    # print('1')
# elif x<0 and y>0:
    # print('2')
# elif x<0 and y<0:
    # print('3')
# else:
    # print('4')


# 사분면의 위치를 확인하면 쉬운 문제



# 2884
# 상근이는 매일 아침 알람을 듣고 일어난다. 알람을 듣고 바로 일어나면 다행이겠지만,
# 항상 조금만 더 자려는 마음 때문에 매일 학교를 지각하고 있다.

# 상근이는 모든 방법을 동원해보았지만, 조금만 더 자려는 마음은 그 어떤 것도 
# 없앨 수가 없었다.

# 이런 상근이를 불쌍하게 보던, 창영이는 자신이 사용하는 방법을 추천해 주었다.

# 바로 "45분 일찍 알람 설정하기"이다.

# 이 방법은 단순하다. 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 
# 것이다. 어차피 알람 소리를 들으면, 알람을 끄고 조금 더 잘 것이기 때문이다. 
# 이 방법을 사용하면, 매일 아침 더 잤다는 기분을 느낄 수 있고, 
# 학교도 지각하지 않게 된다.

# 현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면, 
# 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.


# H, M = map(int, input().split())

# if M < 45:
    # if H == 0:
        # H = 23
        # M += 60
    # else:
        # H -= 1
        # M += 60
        
# print(H, M-45)

# 두 정수 H, M의 시간을 입력받기 위해 45분 전 시간을 출력하는 문제로,
# 시간은 하루 24시간, 1시간에 60분 범위에서 간다. 
# M은 양수이기 때문에 M이 45보다 작은 경우라면 음수로 출력되게 되어 정상 시간이
# 될 수 없기 때문에 M이 45분보다 작은 조건식을 만들었다.

# 여기서 H가 0인 경우와 그렇지 않은 경우를 if로 나눠주는 식을 세운다.
# 마지막 출력에서 H, M-45를 출력하는 이유는 조건을 M이 45보다 적은 수를 가정하여 
# 식을 세웠기 때문에 45분을 빼주는 식으로 출력한다.



# 2525

# KOI 전자에서는 건강에 좋고 맛있는 훈제오리구이 요리를 간편하게 만드는 
# 인공지능 오븐을 개발하려고 한다. 인공지능 오븐을 사용하는 방법은 
# 적당한 양의 오리 훈제 재료를 인공지능 오븐에 넣으면 된다. 그러면 
# 인공지능 오븐은 오븐구이가 끝나는 시간을 분 단위로 자동적으로 계산한다. 

# 또한, KOI 전자의 인공지능 오븐 앞면에는 사용자에게 훈제오리구이 요리가 
# 끝나는 시각을 알려 주는 디지털 시계가 있다. 

# 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 
# 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.


# H, M = map(int, input().split())
# timer = int(input())

# H += timer // 60
# M += timer % 60

# if M >= 60:
    # H += 1
    # M -= 60
# if H >= 24:
    # H -= 24

# print(H, M)

# 2884번 문제와 비슷한 생각으로 접근했다.
# H, M 을 입력받고 timer 시간을 통해 먼저 설정해줬다. H는 시간으로 쳐야하기 때문에
# 몫 연산, M은 나머지 연산으로 지정했다.
# if문을 사용해 M이 60이 넘을때와 H가 24를 넘을때 조건을 설정했으며
# 그로인해 출력되는 것으로 출력했다.