import java.util.ArrayList;
import java.util.Arrays;

public class PowersetIterative {
    public static String[] set1;

    public static void main(String[] m) {
        set1 = new String[6];
        set1[0] = "a";
        set1[1] = "b";
        set1[2] = "c";
        set1[3] = "d";
        set1[4] = "e";
        set1[5] = "f";
        ArrayList<String[]> pset = getPowerset(set1);
        System.out.println(pset.size());
        for (String[] arr : pset) {
            System.out.print(Arrays.toString(arr) + " ");
        }
    }

    public static ArrayList<String[]> subsetsM(String[] set, int m, int mPos, int setPos) {
        ArrayList<String[]> setsOfM = new ArrayList<String[]>();
        while (mPos > 0 && setPos <= (set.length - mPos)) {
            ArrayList<String[]> subs = subsetsM(set, m, mPos-1, setPos+1);
            for (String[] s : subs) {
                s[mPos-1] = set[setPos];
                setsOfM.add(s);
            }
            setPos++;
        }
        if (setsOfM.size() == 0) {
            String[] emptySet = new String[m];
            setsOfM.add(emptySet);
        }
        return setsOfM;
    }

    public static ArrayList<String[]> getPowerset(String[] set) {
        ArrayList<String[]> pset = new ArrayList<String[]>();
        int m = 1;
        while (m <= set.length){
            ArrayList<String[]> subsetsLengthM = subsetsM(set, m, m, 0);
            for (String[] s : subsetsLengthM) {
                pset.add(s);
            }
            m++;
        }
        String[] emptySet = {};
        pset.add(emptySet);
        return pset;
    }
}
