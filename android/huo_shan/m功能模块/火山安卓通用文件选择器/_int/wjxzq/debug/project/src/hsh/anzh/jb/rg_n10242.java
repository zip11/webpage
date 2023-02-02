
package hsh.anzh.jb;

public class rg_n10242 {

    public static double LP2DP (final int nUnitType, final double dbLPSize) {
        android.util.DisplayMetrics metrics = rg_n17.rg_n67 ().getDisplayMetrics ();
        switch (nUnitType) {
            case rg_n10235.rg_n10236:
                return dbLPSize;
            case rg_n10235.rg_n10237:
                return dbLPSize * metrics.density;
            case rg_n10235.rg_n10238:
                return dbLPSize * metrics.scaledDensity;
            case rg_n10235.rg_n10239:
                return dbLPSize * metrics.xdpi * (1.0 / 72);
            case rg_n10235.rg_n10240:
                return dbLPSize * metrics.xdpi;
            case rg_n10235.rg_n10241:
                return dbLPSize * metrics.xdpi * (1.0 / 25.4);
            }
        return 0;
    }
    public static double DP2LP (final int nUnitType, final double dbDPSize) {
        android.util.DisplayMetrics metrics = rg_n17.rg_n67 ().getDisplayMetrics ();
        switch (nUnitType) {
            case rg_n10235.rg_n10236:
                return dbDPSize;
            case rg_n10235.rg_n10237:
                return dbDPSize / metrics.density;
            case rg_n10235.rg_n10238:
                return dbDPSize / metrics.scaledDensity;
            case rg_n10235.rg_n10239:
                return dbDPSize * 72 / metrics.xdpi;
            case rg_n10235.rg_n10240:
                return dbDPSize / metrics.xdpi;
            case rg_n10235.rg_n10241:
                return dbDPSize * 25.4 / metrics.xdpi;
            }
        return 0;
    }

    public static String rg_n10264 (int rg_n10265, String rg_n10266) {
        if (rg_n10265 == (int)0)
            return rg_n10266;
        try {
            return rg_n17.rg_n67 ().getString (rg_n10265);
        } catch (Exception e) {
            return rg_n10266;
        }
    }

    public static android.graphics.drawable.Drawable rg_n10267 (int rg_n10268) {
        if (rg_n10268 == (int)0)
            return null;
        try {
            return rg_n17.rg_n67 ().getDrawable (rg_n10268);
        } catch (Exception e) {
            return null;
        }
    }
}
