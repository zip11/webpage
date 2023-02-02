
package hsh.anzh.jb;

import android.app.Activity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.*;

public class AndComActivity {

    private static final int rg_n2978 = twothree.ceshi.R.string.rg_n2978;
    private static final int rg_n2982 = twothree.ceshi.R.drawable.info_icon;
    private static final int rg_n2983 = twothree.ceshi.R.string.rg_n2983;
    public static final int rg_n3088 = android.R.attr.colorForeground;
    public static final int rg_n3090 = android.R.attr.colorBackground;
    private static final String cs_strActivityLoadParams = "@activity_params";
    public static void sStartNewActivity (final android.content.Context context, final Class clsActivity,
            final android.os.Bundle bundle, final int nRequestCode, final int nAddFlags, final Object... params) {
        if (rg_n581.sIsUiThread ()) {
            try {
                _sStartNewActivity (context, clsActivity, bundle, nRequestCode, nAddFlags,  params);
            } catch (Exception e) { }
        } else {
            rg_n581.sRunOnUiThread (new Runnable () {
                @Override public void run () {
                    try {
                        _sStartNewActivity (context, clsActivity, bundle, nRequestCode, nAddFlags,  params);
                    } catch (Exception e) { }
                } } );
        }
    }
    public static boolean _sStartNewActivity (android.content.Context context, Class clsActivity,
            android.os.Bundle bundle, int nRequestCode, int nAddFlags, Object... params) {
        rg_n648 objCache = rg_n581.sGetGlobalDataCache ();
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

    public static void rg_n2973 (final android.app.Activity rg_n2974, int rg_n2975, final String rg_n2976, final String rg_n2977) {
        final android.graphics.drawable.Drawable objDrawable = rg_n10806.rg_n10831 (rg_n2975);
        if (rg_n581.sIsUiThread ()) {
            try {
                new android.app.AlertDialog.Builder (rg_n2974).
                       setIcon (objDrawable).setPositiveButton (rg_n2978, null).
                       setTitle (rg_n2977).setMessage (rg_n2976).show ();
            } catch (Exception e) { }
        } else {
            rg_n581.sRunOnUiThread (new Runnable () {
                @Override public void run () {
                    try {
                        new android.app.AlertDialog.Builder (rg_n2974).
                                   setIcon (objDrawable).setPositiveButton (rg_n2978, null).
                                   setTitle (rg_n2977).setMessage (rg_n2976).show ();
                    } catch (Exception e) { }
                } } );
        }
    }

    public static void rg_n2979 (final android.app.Activity rg_n2980, final String rg_n2981) {
        AndComActivity.rg_n2973 (rg_n2980, rg_n2982, rg_n2981, rg_n10806.rg_n10828 (rg_n2983, ""));
    }
}
