
package hsh.anzh.jb;

import android.app.Activity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.*;

public class AndroidView extends hsh.Java.jb.rg_n15841 {

    public AndroidView ()  { }

    public static final int rg_n3347 = -1;
    public static final int rg_n3348 = -2;
    protected static final int rg_n3437 = hsh.chx.R.id.rg_n3437;
    private View m_view;
    private rg_n3600 m_animator;
    private View.OnAttachStateChangeListener m_stateChangeListener;
    private android.view.ViewTreeObserver.OnDrawListener m_drawListener;
    private android.view.ViewTreeObserver.OnGlobalLayoutListener m_layoutListener;
    public AndroidView (android.content.Context context, View view, Object objInitData) {
        m_view = view;
        m_view.setTag (rg_n3437, this);
    }
    public AndroidView (android.content.Context context, View view) {
        this (context, view, null);
    }
    public void onInitControlContent (android.content.Context context, Object objInitData) {
        OnInitView (context, objInitData);
        rg_n1934 (context, objInitData);
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
            Object obj = view.getTag (rg_n3437);
            if (obj != null && obj instanceof AndroidView)
                return (AndroidView)obj;
        }
        return null;
    }
    protected void OnInitView (android.content.Context context, Object objInitData) {
    }

    public static interface re_n3060 { int dispatch (AndroidView objSource, int nTagNumber); }
    private re_n3060 rd_n3060;
    private int rd_n3060_tag;
    public void rl_AndroidView_n3060 (re_n3060 objListener, int nTagNumber) {
        synchronized (this) { rd_n3060 = objListener;  rd_n3060_tag = nTagNumber; }
    }
    public int rg_n3060 () {
        re_n3060 objDispatcher;  int nTagNumber;
        synchronized (this) { objDispatcher = rd_n3060;  nTagNumber = rd_n3060_tag; }
        return (objDispatcher != null ? objDispatcher.dispatch (this, nTagNumber) : 0);
    }

    public void rg_n3082 (final boolean rg_n3083) {
        if (rg_n17.sIsUiThread ()) {
            try {
                m_view.setClickable (rg_n3083);
            } catch (Exception e) { }
        } else {
            rg_n17.sRunOnUiThread (new Runnable () {
                @Override public void run () {
                    try {
                        m_view.setClickable (rg_n3083);
                    } catch (Exception e) { }
                } } );
        }
        try {
            if (rg_n3083) {
               m_view.setOnClickListener (new View.OnClickListener () {
                       @Override public void onClick (View v) {
                           rg_n3060 ();
                       } } );
            } else {
                m_view.setOnClickListener (null);
            };
        } catch (Exception e) { }
    }

    protected void rg_n1934 (android.content.Context rg_n3438, java.lang.Object rg_n3439) {
    }
}
