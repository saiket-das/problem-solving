# https://www.geeksforgeeks.org/problems/java-if-else-decision-making0924/0?category%255B%255D=Java&difficulty%255B%255D=-2&page=1&query=category%255B%255DJavadifficulty%255B%255D-2page1category%255B%255DJava


def compareNM(n : int, m : int) -> str:
    if (n == m):
        return "equal"
    elif (n < m):
        return "lesser"
    else:
        return "greater"


print(compareNM(6, 5))