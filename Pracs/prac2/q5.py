def towers(n, src, dest, level):
    if n==1:
        moveDisk(n,src,dest, level)
    else:
        tmp = 6-src-dest
        towers(n-1, src, tmp, level+1)
        moveDisk(n,src, dest, level)
        towers(n-1,tmp,dest, level+1)

def moveDisk(n,src,dest,level):
    print(level*"\t","moving disk from peg ", src, " to peg ", dest)
    print(level*"\t","n=", n, " src=", src, " dest=",dest)
    print(level*"\t", "level = ", level," \n")

towers(3,1,3,1)