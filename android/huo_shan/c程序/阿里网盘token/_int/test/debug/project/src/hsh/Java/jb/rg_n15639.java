
package hsh.Java.jb;

public class rg_n15639 {

    public rg_n15639 ()  { }

    public static java.util.ArrayList<String> rg_n15658 (String rg_n15659, String rg_n15660) {
        java.io.BufferedReader reader = null;
        try {
            java.io.File file = new java.io.File (rg_n15659);
            if (file.isFile () == false || file.exists () == false)
                return null;
            java.util.ArrayList<String> res = new java.util.ArrayList<String> ();
            reader = new java.io.BufferedReader (new java.io.InputStreamReader (new java.io.FileInputStream (file), rg_n15660));
            String str;
            while ((str = reader.readLine ()) != null)
                res.add (str);
            return res;
        } catch (Exception e) { }
        finally {
            if (reader != null)
                try {
                    reader.close ();
                } catch (Exception e) { }
        }
        return null;
    }
}
