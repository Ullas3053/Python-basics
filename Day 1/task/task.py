# def is_prime(num):
#     if num <2:
#         return False
#     for i in range (2,num):
#         if num % i ==0:
#             return False
#     return True
#
# def sum_of_primes(n):
#     total_sum = 0
#     for num in range(2,n):
#         if is_prime(num):
#             total_sum += num
#     return total_sum
# n =2
# print(sum_of_primes(n))

# def reverse_array(arr):
#     s = 0
#     e =len(arr)-1
#     while s < e:
#         arr[s],arr[e] = arr[e], arr[s]
#         s+=1
#         e-=1
#     return arr
# def sum_reverse_array(arr):
#     reverse_array(arr)
#     even_sum = 0
#     for i in range(0,len(arr)):
#         if i%2 == 0:
#             even_sum+=arr[i]
#     return even_sum
#
# print(sum_reverse_array([10,20,30,40,50,60]))
# def  shift_zeroes_to_end(arr):
#     j=0
#     n=len(arr)
#     for i in range(n):
#         if arr[i] != 0:
#             arr[j] = arr[i]
#             j+=1
#     while j<n:
#         arr[j]= 0
#         j+=1
#     return arr
# arr = [0, 1, 0, 3, 12]
# print(shift_zeroes_to_end(arr))

