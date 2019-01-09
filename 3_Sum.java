public class Solution {
    public int threeSumClosest(ArrayList<Integer> A, int B) {
        Collections.sort(A);
        int l, r;
        int ls = Integer.MIN_VALUE;
        int rs = Integer.MAX_VALUE;
        int out;
        
        for (int i = 0; i < A.size() - 2; i++) { 
            l = i + 1; 
            r = A.size() - 1;
            while (l < r) { 
                if(A.get(i) + A.get(l) + A.get(r)==B){
                    out = A.get(i) + A.get(l) + A.get(r);
                    return out;
                }
                if (A.get(i) + A.get(l) + A.get(r) < B){
                    if(ls<A.get(i) + A.get(l) + A.get(r))
                        ls=A.get(i) + A.get(l) + A.get(r);
                    l++;
                }
                else{
                    if(rs>A.get(i) + A.get(l) + A.get(r))
                        rs=A.get(i) + A.get(l) + A.get(r);
                    r--;
                }
            } 
        }
        if(Math.abs(B-ls)<=Math.abs(B-rs))
            return ls;
        return rs;
    }
}
