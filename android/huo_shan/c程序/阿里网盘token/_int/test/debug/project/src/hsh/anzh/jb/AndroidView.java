
package hsh.anzh.jb;

import android.app.Activity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.*;

public class AndroidView extends hsh.Java.jb.rg_n16405 {

    public AndroidView ()  { }

    public static final int rg_n3911 = -1;
    public static final int rg_n3912 = -2;
    protected static final int rg_n4001 = twothree.ceshi.R.id.rg_n4001;
    private View m_view;
    private rg_n4164 m_animator;
    private View.OnAttachStateChangeListener m_stateChangeListener;
    private android.view.ViewTreeObserver.OnDrawListener m_drawListener;
    private android.view.ViewTreeObserver.OnGlobalLayoutListener m_layoutListener;
    public AndroidView (android.content.Context context, View view, Object objInitData) {
        m_view = view;
        m_view.setTag (rg_n4001, this);
    }
    public AndroidView (android.content.Context context, View view) {
        this (context, view, null);
    }
    public void onInitControlContent (android.content.Context context, Object objInitData) {
        OnInitView (context, objInitData);
        rg_n2498 (context, objInitData);
    }
    public View GetView () { return m_view; }
    public static AndroidView sNewInstance (android.content.Context context) {
        return sNewInstanceAndAttachView (context, new View (context), null);
    }
    public static AndroidView sNewInstance (android.content.Context context, Object objInitData) {
        return sNewInstanceAndAttachView (context, new View (context), objInitData);
    }
    public static AndroidView sNewInstanceAndAttachView (android.content.Context context, View viewAttach) {
        return sNewInstanceAndAttachView (context, viewAttach, null);
    }
    public static AndroidView sNewInstanceAndAttachView (android.content.Context context, View viewAttach, Object objInitData) {
        AndroidView objControl = new AndroidView (context, viewAttach, objInitData);
        objControl.onInitControlContent (context, objInitData);
        return objControl;
    }
    public static AndroidView sSafeGetVolView (View view) {
        if (view != null) {
            Object obj = view.getTag (rg_n4001);
            if (obj != null && obj instanceof AndroidView)
                return (AndroidView)obj;
        }
        return null;
    }
    protected void OnInitView (android.content.Context context, Object objInitData) {
    }

    public static interface re_n3624 { int dispatch (AndroidView objSource, int nTagNumber); }
    private re_n3624 rd_n3624;
    private int rd_n3624_tag;
    public void rl_AndroidView_n3624 (re_n3624 objListener, int nTagNumber) {
        synchronized (this) { rd_n3624 = objListener;  rd_n3624_tag = nTagNumber; }
    }
    public int rg_n3624 () {
        re_n3624 objDispatcher;  int nTagNumber;
        synchronized (this) { objDispatcher = rd_n3624;  nTagNumber = rd_n3624_tag; }
        return (objDispatcher != null ? objDispatcher.dispatch (this, nTagNumber) : 0);
    }

    public void rg_n3646 (final boolean rg_n3647) {
        if (rg_n581.sIsUiThread ()) {
            try {
                m_view.setClickable (rg_n3647);
            } catch (Exception e) { }
        } else {
            rg_n581.sRunOnUiThread (new Runnable () {
                @Override public void run () {
                    try {
                        m_view.setClickable (rg_n3647);
                    } catch (Exception e) { }
                } } );
        }
        try {
            if (rg_n3647) {
               m_view.setOnClickListener (new View.OnClickListener () {
                       @Override public void onClick (View v) {
                           rg_n3624 ();
                       } } );
            } else {
                m_view.setOnClickListener (null);
            };
        } catch (Exception e) { }
    }

    protected void rg_n2498 (android.content.Context rg_n4002, java.lang.Object rg_n4003) {
    }
}
