def can_seat_audiences(N, gates, audiences, max_distance):

    available_seats = [0] * (N + 1)
    for i in range(1, N + 1):
        available_seats[i] = 1

    for gate, audience in zip(gates, audiences):
        left = max(1, gate - max_distance)
        right = min(N, gate + max_distance)


        for seat in range(left, right + 1):
            if audience == 0:
                break
            if available_seats[seat] == 1:
                available_seats[seat] = 0
                audience -= 1

        if audience > 0:
            return False

    return True

# def min_max_distance(N, K, gates, audiences):
# left, right = 0, N
# answer = -1

#     while left <= right:
#         mid = (left + right) // 2
#         if can_seat_audiences(N, gates, audiences, mid):
#             answer = mid
#             right = mid - 1
#         else:
#             left = mid + 1
#     return answer

# def main():
# import sys
# input = sys.stdin.read
# data = input().splitlines()

#     index = 0
#     T = int(data[index])
#     index += 1
#     results = []

#     for _ in range(T):
#         N, K = map(int, data[index].split())
#         index += 1
#         gates = list(map(int, data[index].split()))
#         index += 1
#         audiences = list(map(int, data[index].split()))
#         index += 1

#         result = min_max_distance(N, K, gates, audiences)
#         results.append(result)

#     for res in results:
#         print(res)

# if **name** == '**main**':
# main()
