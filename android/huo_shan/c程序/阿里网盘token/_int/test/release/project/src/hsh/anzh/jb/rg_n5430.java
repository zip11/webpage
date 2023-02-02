
package hsh.anzh.jb;

import android.app.Activity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.*;

public class rg_n5430 extends AndroidView {

    public rg_n5430 ()  { }

    public rg_n5430 (android.content.Context context, TextView view, Object objInitData) { super (context, view, objInitData); }
    public rg_n5430 (android.content.Context context, TextView view) { this (context, view, null); }
    public TextView GetTextView () { return (TextView)GetView (); }
    public static rg_n5430 sNewInstance (android.content.Context context) {
        return sNewInstanceAndAttachView (context, new TextView (context), null);
    }
    public static rg_n5430 sNewInstance (android.content.Context context, Object objInitData) {
        return sNewInstanceAndAttachView (context, new TextView (context), objInitData);
    }
    public static rg_n5430 sNewInstanceAndAttachView (android.content.Context context, TextView viewAttach) {
        return sNewInstanceAndAttachView (context, viewAttach, null);
    }
    public static rg_n5430 sNewInstanceAndAttachView (android.content.Context context, TextView viewAttach, Object objInitData) {
        rg_n5430 objControl = new rg_n5430 (context, viewAttach, objInitData);
        objControl.onInitControlContent (context, objInitData);
        return objControl;
    }
    protected int rg_n5488 = 0;
    protected int rg_n5489 = 0;
    android.text.TextWatcher m_objTextWatcher;

    public void rg_n5450 (final String rg_n5451) {
        if (rg_n581.sIsUiThread ()) {
            try {
                GetTextView ().setText (rg_n5451);
            } catch (Exception e) { }
        } else {
            rg_n581.sRunOnUiThread (new Runnable () {
                @Override public void run () {
                    try {
                        GetTextView ().setText (rg_n5451);
                    } catch (Exception e) { }
                } } );
        }
    }

    public void rg_n5570 (final String rg_n5571) {
        if (rg_n581.sIsUiThread ()) {
            try {
                GetTextView ().append (rg_n5571);
            } catch (Exception e) { }
        } else {
            rg_n581.sRunOnUiThread (new Runnable () {
                @Override public void run () {
                    try {
                        GetTextView ().append (rg_n5571);
                    } catch (Exception e) { }
                } } );
        }
    }
}
