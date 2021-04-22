import numpy as np
list = np.random.randint(50,size=(500))  #리스트 생성
check_List = np.zeros(50,int)            #값의 갯수를 파악하기 위한 배열 생성

print("500개의 인덱스를 가진 배열 생성\n", list)



for i in list: # 카운트 중복 되는 값을 카운트 해줌. list[i]의 해당하는 값이 3이라 check_list의 3인덱스에  + 1 을 해줌.
      check_List[list[i]] = check_List[list[i]] + 1

print("check_List를 이용해 값의 갯수를 카운트한 배열 출력 \n" ,check_List)

for i in range(0,3):
    print(i+1,"번째로 가장 많은 값은 = ", np.where(check_List.max() == check_List)[0][0], " 갯수 = ", check_List.max());
    #check_list는 넘파이 객체이므로 Index 함수가 아니기 때문에, where 함수를 사용해야한다.
    # 이때 where 함수는 np.where('찾으려는 원소' == array이름) 형태로 사용한다.
    # where의 return 값은 2차원 배열 형태로 반환이 되기 때문에 [0][0]인덱스로 접근 하여 출력을 하면 된다.
    check_List[np.where(check_List.max() == check_List)[0][0]]  = 0
    #다음번째로 큰 값을 출력하기 위해 max번째의 인덱스에 해당 하는 값을 0으로 바꿔준다.

