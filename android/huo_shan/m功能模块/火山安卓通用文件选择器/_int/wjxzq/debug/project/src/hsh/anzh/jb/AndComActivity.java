
package hsh.anzh.jb;

import android.app.Activity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.*;

public class AndComActivity {

    private static final int rg_n2414 = hsh.chx.R.string.rg_n2414;
    private static final int rg_n2418 = hsh.chx.R.drawable.info_icon;
    private static final int rg_n2419 = hsh.chx.R.string.rg_n2419;
    public static final int rg_n2524 = android.R.attr.colorForeground;
    public static final int rg_n2526 = android.R.attr.colorBackground;
    private static final String cs_strActivityLoadParams = "@activity_params";
    public static void sStartNewActivity (final android.content.Context context, final Class clsActivity,
            final android.os.Bundle bundle, final int nRequestCode, final int nAddFlags, final Object... params) {
        if (rg_n17.sIsUiThread ()) {
            try {
                _sStartNewActivity (context, clsActivity, bundle, nRequestCode, nAddFlags,  params);
            } catch (Exception e) { }
        } else {
            rg_n17.sRunOnUiThread (new Runnable () {
                @Override public void run () {
                    try {
                        _sStartNewActivity (context, clsActivity, bundle, nRequestCode, nAddFlags,  params);
                    } catch (Exception e) { }
                } } );
        }
    }
    public static boolean _sStartNewActivity (android.content.Context context, Class clsActivity,
            android.os.Bundle bundle, int nRequestCode, int nAddFlags, Object... params) {
        rg_n84 objCache = rg_n17.sGetGlobalDataCache ();
        int nParamDataIdentifier = 0;
        try {
            android.content.Intent objIntent = new android.content.Intent (context, clsActivity);
            if (nAddFlags != 0)
                objIntent.addFlags (nAddFlags);
            if (bundle != null)
                objIntent.putExtras (bundle);
            if (params != null && params.length > 0) {
                nParamDataIdentifier = objCache.Push (params);
                objIntent.putExtra (cs_strActivityLoadParams, nParamDataIdentifier);
            }
            if (nRequestCode != 0 && context instanceof android.app.Activity)
                ((android.app.Activity)context).startActivityForResult (objIntent, nRequestCode);
            else
                context.startActivity (objIntent);
            return true;
        } catch (Exception e) { }
        objCache.Remove (nParamDataIdentifier);
        return false;
    }

    public static void rg_n2409 (final android.app.Activity rg_n2410, int rg_n2411, final String rg_n2412, final String rg_n2413) {
        final android.graphics.drawable.Drawable objDrawable = rg_n10242.rg_n10267 (rg_n2411);
        if (rg_n17.sIsUiThread ()) {
            try {
                new android.app.AlertDialog.Builder (rg_n2410).
                       setIcon (objDrawable).setPositiveButton (rg_n2414, null).
                       setTitle (rg_n2413).setMessage (rg_n2412).show ();
            } catch (Exception e) { }
        } else {
            rg_n17.sRunOnUiThread (new Runnable () {
                @Override public void run () {
                    try {
                        new android.app.AlertDialog.Builder (rg_n2410).
                                   setIcon (objDrawable).setPositiveButton (rg_n2414, null).
                                   setTitle (rg_n2413).setMessage (rg_n2412).show ();
                    } catch (Exception e) { }
                } } );
        }
    }

    public static void rg_n2415 (final android.app.Activity rg_n2416, final String rg_n2417) {
        AndComActivity.rg_n2409 (rg_n2416, rg_n2418, rg_n2417, rg_n10242.rg_n10264 (rg_n2419, ""));
    }
}
