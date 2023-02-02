
package hsh.anzh.jb;

import android.app.Activity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.*;

public class rg_n3980 extends AndroidViewGroup {

    public rg_n3980 ()  { }

    public rg_n3980 (android.content.Context context, LinearLayout view, Object objInitData) { super (context, view, objInitData); }
    public rg_n3980 (android.content.Context context, LinearLayout view) { this (context, view, null); }
    public LinearLayout GetLinearLayout () { return (LinearLayout)GetView (); }
    public static rg_n3980 sNewInstance (android.content.Context context) {
        return sNewInstanceAndAttachView (context, new LinearLayout (context), null);
    }
    public static rg_n3980 sNewInstance (android.content.Context context, Object objInitData) {
        return sNewInstanceAndAttachView (context, new LinearLayout (context), objInitData);
    }
    public static rg_n3980 sNewInstanceAndAttachView (android.content.Context context, LinearLayout viewAttach) {
        return sNewInstanceAndAttachView (context, viewAttach, null);
    }
    public static rg_n3980 sNewInstanceAndAttachView (android.content.Context context, LinearLayout viewAttach, Object objInitData) {
        rg_n3980 objControl = new rg_n3980 (context, viewAttach, objInitData);
        objControl.onInitControlContent (context, objInitData);
        return objControl;
    }
}
