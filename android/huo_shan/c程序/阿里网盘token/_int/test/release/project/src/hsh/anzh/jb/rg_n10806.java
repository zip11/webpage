
package hsh.anzh.jb;

public class rg_n10806 {

    public static double LP2DP (final int nUnitType, final double dbLPSize) {
        android.util.DisplayMetrics metrics = rg_n581.rg_n631 ().getDisplayMetrics ();
        switch (nUnitType) {
            case rg_n10799.rg_n10800:
                return dbLPSize;
            case rg_n10799.rg_n10801:
                return dbLPSize * metrics.density;
            case rg_n10799.rg_n10802:
                return dbLPSize * metrics.scaledDensity;
            case rg_n10799.rg_n10803:
                return dbLPSize * metrics.xdpi * (1.0 / 72);
            case rg_n10799.rg_n10804:
                return dbLPSize * metrics.xdpi;
            case rg_n10799.rg_n10805:
                return dbLPSize * metrics.xdpi * (1.0 / 25.4);
            }
        return 0;
    }
    public static double DP2LP (final int nUnitType, final double dbDPSize) {
        android.util.DisplayMetrics metrics = rg_n581.rg_n631 ().getDisplayMetrics ();
        switch (nUnitType) {
            case rg_n10799.rg_n10800:
                return dbDPSize;
            case rg_n10799.rg_n10801:
                return dbDPSize / metrics.density;
            case rg_n10799.rg_n10802:
                return dbDPSize / metrics.scaledDensity;
            case rg_n10799.rg_n10803:
                return dbDPSize * 72 / metrics.xdpi;
            case rg_n10799.rg_n10804:
                return dbDPSize / metrics.xdpi;
            case rg_n10799.rg_n10805:
                return dbDPSize * 25.4 / metrics.xdpi;
            }
        return 0;
    }

    public static String rg_n10828 (int rg_n10829, String rg_n10830) {
        if (rg_n10829 == (int)0)
            return rg_n10830;
        try {
            return rg_n581.rg_n631 ().getString (rg_n10829);
        } catch (Exception e) {
            return rg_n10830;
        }
    }

    public static android.graphics.drawable.Drawable rg_n10831 (int rg_n10832) {
        if (rg_n10832 == (int)0)
            return null;
        try {
            return rg_n581.rg_n631 ().getDrawable (rg_n10832);
        } catch (Exception e) {
            return null;
        }
    }
}
