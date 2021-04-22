
import numpy as np

list1 = [[1,2,3],[4,5,6]] #리스트 생성
list2 = [[10,20,30],[40,50,60]] # 리스트 생성
list3 = [[100,200,300],[400,500,600]] # 리스트 생성

a = np.array(list1)     #생성한 리스트를 a,b,c에 numpy패키지의 array함수를 이용하여 넣어줌. -> a,b,c라는 numpy 객체 생성
b = np.array(list2)
c = np.array(list3)

print("방법1 \n")

print('a 형태:', a.shape, '\n', a)
print('다차원 객체 1차원 변환 방법1. \n revel( ) 을 이용')
print('a =',np.ravel(a))  # 다차원의 모든 객체를 1차원 벡터로 반

print("방법2 \n")

print('b 형태:', b.shape, '\n', b)
print('다차원 객체 1차원 변환 방법2. \n flatten( ) 을 이용')
print('b =',b.flatten())   # 다차원 ndarray 객체를 1차원 백터로 변환 해줌.

print("방법3 \n")

print('c 형태:', c.shape, '\n', c)
print('다차원 객체 1차원 변환 방법3. \n reshape( ) 을 이용')
print('c =',c.reshape(-1))   # reshoap() 함수를 이용하여 1차원 벡터로 변환. 이때 -1 은 자동 정렬을 해줌.

