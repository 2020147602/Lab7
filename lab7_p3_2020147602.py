class not2DError(Exception):
    # Error for 1D list
    def __str__(self):
        return '[ERROR]: list is not 2D.'


class unevenListError(Exception):
    # Error for uneven list
    def __str__(self):
        return '[ERROR]: inner lists are not same in length.'


class improperMatrixError(Exception):
    # Error for incompatible matmul pair
    def __str__(self):
        return '[ERROR]: [a][b]*[c][d] not b==c.'


def mul1d(arr1, arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return  1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum += arr1[i] * arr2[i]
    return sum


class list_D2(list):
    def __init__(self, arr):
        ### YOUR CODE HERE ###
        self.arr=arr
        self.bool=[]
        self.list_len=[]
        self.list_mul=[]


        for item in self.arr:
            # 리스트 분해할 때 바로 정수 요소 있으면 not 2d error 발생
            if isinstance((item),int):
                raise not2DError()
            #그게 아닐 경우, 길이 반환
            self.list_len.append(len(item))
            for integer in item:
                if (isinstance(integer,int)):
                    self.bool.append('True')
        # self.bool에 false 있으면 2d가 아니라는 것
        if 'False' in self.bool:
            raise not2DError()

        # 1이 아니면 다른 숫자의 요소가 있다는것
        if len(set(self.list_len)) == 1:
            self.arr=arr
        else:
            raise unevenListError()

        ######

        self.extend(arr)

    def __str__(self):
        ### YOUR CODE HERE ###

        #행열 구하기
        row = len(self.arr)
        col = len(self.arr[0]) if row > 0 else 0

        return f'list_2D:{row}*{col}'

        ######

    def transpose(self):
        ### YOUR CODE HERE ###
        row = len(self.arr)
        col = len(self.arr[0]) if row > 0 else 0

        #전치된 행렬 초기화
        transpose_arr = [[0 for _ in range(row)] for _ in range(col)]

        for i in range(row):
            for j in range(col):
                transpose_arr[j][i] = self.arr[i][j]

        return list_D2(transpose_arr)


    def __matmul__(self, others):
        ### YOUR CODE HERE ###

        #행렬 곱이 연산가능한지 판단
        if len(self.arr[0]) != len(others.arr):
            raise improperMatrixError()

        #빈 배열 생성
        multiply = []
        for i in range(len(self.arr)):
            row = []
            for j in range(len(others.arr[0])):
                sum = 0
                for k in range(len(others.arr)):
                    sum += self.arr[i][k] * others.arr[k][j]
                row.append(sum)
            multiply.append(row)



        # raise improperMatrixError()
        return list_D2(multiply)

        ######

    def avg(self):
        ### YOUR CODE HERE ###

        #총합과 총 요소수
        total_sum =0
        total_element_num =0
        #순회화면서 더하기
        for row in self.arr:
            for integer in row:
                total_sum +=integer
                total_element_num +=1

        total_avg = total_sum/total_element_num

        return total_avg

        ######

