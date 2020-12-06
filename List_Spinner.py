# Buatlah sebuah return function dengan 1 argumen yang dapat memutar list angka (Putaran 1X counter-clockwise) seperti keterangan di bawah ini .

# List Awal

# [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]
# Function

# # Function Initialization
#  def counterClockwise(...):
#      .....
     
# # Use the Function
# print(counterClockwise(List_awal))
# List Output

# [[3, 6, 9],
# [2, 5, 8],
# [1, 4, 7]]

list_awal = [[1,2,3], [4,5,6], [7,8,9]]

def counterClockwise(list_awal):
    list_akhir = list(map(list, zip(*list_awal)))[::-1]
    print(*list_akhir, sep=',')

counterClockwise(list_awal)
