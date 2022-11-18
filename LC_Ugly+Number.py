class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:                                  # 왜 여기 <=로 바꾸면 오히려 속도랑 메모리 늘어나는거지 예외처리로 빨리 걸러주면 좋은거 아닌가
            return False
            quit()
        while n != 1:
            if n % 5 == 0:
                n /= 5
            elif n % 3 == 0:
                n /= 3
            elif n % 2 == 0:
                n /= 2
            else:
                return False
                quit()
        return True