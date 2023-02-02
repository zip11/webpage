
package hsh.anzh.jb;

import android.app.Activity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.*;

public class rg_n4588 extends AndroidViewGroup {

    public rg_n4588 ()  { }

    public rg_n4588 (android.content.Context context, FrameLayout view, Object objInitData) { super (context, view, objInitData); }
    public rg_n4588 (android.content.Context context, FrameLayout view) { this (context, view, null); }
    public FrameLayout GetFrameLayout () { return (FrameLayout)GetView (); }
    public static rg_n4588 sNewInstance (android.content.Context context) {
        return sNewInstanceAndAttachView (context, new FrameLayout (context), null);
    }
    public static rg_n4588 sNewInstance (android.content.Context context, Object objInitData) {
        return sNewInstanceAndAttachView (context, new FrameLayout (context), objInitData);
    }
    public static rg_n4588 sNewInstanceAndAttachView (android.content.Context context, FrameLayout viewAttach) {
        return sNewInstanceAndAttachView (context, viewAttach, null);
    }
    public static rg_n4588 sNewInstanceAndAttachView (android.content.Context context, FrameLayout viewAttach, Object objInitData) {
        rg_n4588 objControl = new rg_n4588 (context, viewAttach, objInitData);
        objControl.onInitControlContent (context, objInitData);
        return objControl;
    }
    private AndroidLayout m_objLayout;
    public AndroidLayout SetLayoutContent (AndroidLayout objLayout, boolean blListenWindowAttachState, Object objUserData1, Object objUserData2) {
        m_objLayout = objLayout.initAndAddIntoViewGroup (this, blListenWindowAttachState, null, objUserData1, objUserData2, true);
        return m_objLayout;
    }
}
