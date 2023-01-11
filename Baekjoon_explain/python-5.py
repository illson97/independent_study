

# 10807

# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

# 첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 
# 둘째 줄에는 정수가 공백으로 구분되어져있다. 
# 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 
# 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.

# 첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.

# n = int(input())

# n_list = list(map(int, input().split()))
# v = int(input())

# print(n_list.count(v))


# 문제에 직관적으로 나타내면 끝인 문제



# 10871

# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)

# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 
# 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. 
# X보다 작은 수는 적어도 하나 존재한다.

# N, X = map(int, input().split())
# A = list(map(int, input().split()))

# for i in range(N):
    # if A[i] < X:
        # print(A[i], end=" ")


# A 안에 있는 i가 X라는 정수보다 낮을 때를 기준으로 구조를 형성한다.
# 끝





# 10818

# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의
# 정수를 공백으로 구분해서 주어진다.
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.


# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.


# cnt = int(input())

# N = list(map(int, input().split()))
# print(min(N), max(N))


# 리스트를 만들어주고 max(), min()함수를 이용한다.



# 2562

# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이
# 몇 번째 수인지를 구하는 프로그램을 작성하시오.

# 예를 들어, 서로 다른 9개의 자연수

# 3, 29, 38, 12, 57, 74, 40, 85, 61이 주어지면, 이들 중 최댓값은 85이고,
# 이 값은 8번째 수이다.

# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다.
# 주어지는 자연수는 100 보다 작다.
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.


# num_list = []

# for i in range(0,9):
    # num_list.append(int(input()))
    
# print(max(num_list))

# print(num_list.index(max(num_list))+1)




# 5597

# X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 
# 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.

# 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 
# 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

# 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 
# 하나씩 주어진다. 출석번호에 중복은 없다.
# 출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 
# 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.


# num = [i for i in range(1,31)]

# for i in range(28):
    # data = int(input())
    # num.remove(data)
# print(min(num))
# print(max(num))

# 나열식으로 문제로부터 생각하면 쉬ㅇ운 문제
# for문 밑에 수를 넣어주고 반복하면서 num에서 삭제해준다.



# 3052

# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 
# 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.


# 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 
# 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.


# num = []
# for i in range(10):
    # a = int(input())
    # num.append(a%42)
# print(len(set(num)))


# set함수로 집합 자료형을 만들어준다. 중복을 제거하기 위한 필터 역할을 해준다.



# 1546


# 세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 
# 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 
# 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.

# 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 
# 50/70*100이 되어 71.43점이 된다.

# 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 
# 프로그램을 작성하시오.
 

# n = int(input())
# test_list = list(map(int, input().split()))
# M = max(test_list)

# new_list = []
# for score in test_list:
    # new_list.append(score/M*100)
# test_avg = sum(new_list)/n
# print(test_avg)


# 사실상 대입문제지만 과정을 보면 앞에서 변수를 만들어주고
# 중간에 리스트를 만들어 for문으로 반복해준다. 이런 과정은 흔하게 일어나기 때문에
# 과정을 잘 기억해두도록 하자



# 8958

# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, 
# X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 
# 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 
# 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 
# 문자열은 O와 X만으로 이루어져 있다.

# 각 테스트 케이스마다 점수를 출력한다.


# n = int(input())
# for i in range(n):
    # b = input()
    # s = list(b)
    # sum = 0
    # c = 1
    # for i in s:
        # if i == "O":
            # sum += c
            # c += 1
        # else:
            # c = 1
    # print(sum) 


# 과정을 보면 입력받은 후 for문 밑에서도 입력받아 리스트 구성후 다시 한번
# for문을 구성해 합을 구해준다. 다시 한번 위에서부터 천천히 보도록 하자.


# 4344

# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 
# 당신은 그들에게 슬픈 진실을 알려줘야 한다.

# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 
# 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 
# 100보다 작거나 같은 정수이다.

# num = int(input())

# for _ in range(num):
    # scores = list(map(int, input().split()))
    # avg = sum(scores[1:])/scores[0]    
    # cnt = 0
    
    # for i in scores[1:]:
        # if i > avg:
            # cnt += 1
    
    # per = cnt/scores[0]*100
    # print(f'{per:.3f}%')


# for_ in range()에서 _언더스코어는 인터프리터에서 마지막 값을 저장할 때,
# 값을 무시하고 싶을 때, 변수나 함수명에 특별한 의미 또는 기능을 부여하고자 할 때
# 국제화, 지역화 함수로 사용할 때, 숫자 리터럴값의 자릴수 구분을 위한 구분자로
# 사용할 때 등이 있다.


