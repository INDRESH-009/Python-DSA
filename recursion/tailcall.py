def fun(n):
    if n<=0:
        return
    print(n,end=" ")
    fun(n-1)
fun(3)

# TAIL CALL ELIMINATION OR TAIL CALL OPTIMISATION 
# tail recursive functions are optimised by the mordern compilers 
# there is no point in keeping fun(3) fun(2) and fun(1) in the recursion call stack during the exection of this recursve function because there is nothing to do after this recursive call 
# TCE is not present in python , as a programmer u have to write optimised code 

