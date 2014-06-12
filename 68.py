import time
start = time.time()

array = [1,2,3,4,5,6,7,8,9,10]
result = []
def swap(i,j):
    flag=array[i]; array[i]=array[j]; array[j]=flag

def permute(i,n):
    if i==n:
        print array
        if array[0]+array[5]+array[6] == array[1]+array[6]+array[7] == array[2]+array[7]+array[8] == array[3]+array[8]+array[9] == array[4]+array[9]+array[5]:
            result.append(array)
    else:
        for j in xrange(i,n+1):
            swap(i,j); permute(i+1,n); swap(i,j)

permute(0,len(array)-1)

print time.time() - start
for each in result:
    print each
