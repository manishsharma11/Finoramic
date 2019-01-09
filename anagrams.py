class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def check(self, A, B):
        chlist = [0]*26
        k=0
        while(k<len(A) and k<len(B)):
            chlist[ord(A[k])-97] = chlist[ord(A[k])-97]+1
            chlist[ord(B[k])-97] = chlist[ord(B[k])-97]-1
            k=k+1
        if len(A)!=len(B):
            return False
        for l in range(0, 26):
            if(chlist[l]!=0):
                return False
        return True
    def anagrams(self, A):
        out = []
        tk = []
        for i in range(0, len(A)):
            if i not in tk:
                out.append([i+1])
            j=i+1
            while(j<len(A)):
                if j not in tk:
                    if self.check(A[i], A[j]):
                        tk.append(j)
                        for z in range(0, len(out)):
                            if out[z][0]==i+1:
                                out[z].append(j+1)
                                break
                j=j+1
        return out

