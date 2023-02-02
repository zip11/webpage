
package hsh.anzh.jb;

import android.app.Activity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.*;

public class rg_n4866 extends AndroidView {

    public rg_n4866 ()  { }

    public rg_n4866 (android.content.Context context, TextView view, Object objInitData) { super (context, view, objInitData); }
    public rg_n4866 (android.content.Context context, TextView view) { this (context, view, null); }
    public TextView GetTextView () { return (TextView)GetView (); }
    public static rg_n4866 sNewInstance (android.content.Context context) {
        return sNewInstanceAndAttachView (context, new TextView (context), null);
    }
    public static rg_n4866 sNewInstance (android.content.Context context, Object objInitData) {
        return sNewInstanceAndAttachView (context, new TextView (context), objInitData);
    }
    public static rg_n4866 sNewInstanceAndAttachView (android.content.Context context, TextView viewAttach) {
        return sNewInstanceAndAttachView (context, viewAttach, null);
    }
    public static rg_n4866 sNewInstanceAndAttachView (android.content.Context context, TextView viewAttach, Object objInitData) {
        rg_n4866 objControl = new rg_n4866 (context, viewAttach, objInitData);
        objControl.onInitControlContent (context, objInitData);
        return objControl;
    }
    protected int rg_n4924 = 0;
    protected int rg_n4925 = 0;
    android.text.TextWatcher m_objTextWatcher;
}
