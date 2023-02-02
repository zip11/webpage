
package hsh.anzh.jb;

import android.app.Activity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.*;

public class rg_n12768 extends android.app.Activity {

    private static final String cs_strActivityLoadParams = "@activity_params";
    protected boolean onInitAndroidActivity () {
        if (rg_n581.sCheckRestart (this) == false)
            return false;
        rg_n12781 ();
        return true;
    }
    protected void onStart ()    {  super.onStart ();  m_blCleanupMethodCalled = false;  rg_n12772 ();  }
    protected void onRestart ()  {  super.onRestart ();  rg_n12773 ();  }
    protected void onResume ()   {  super.onResume ();  rg_n12776 ();  }
    protected void onPause ()    {  super.onPause ();  rg_n12777 ();  }
    protected void onNewIntent(android.content.Intent intent) { super.onNewIntent(intent); rg_n12774 (intent);  }
    protected void onStop () {
        super.onStop ();
        rg_n12779 ();
        if (isChangingConfigurations ())
            rg_n581.sForceRestart  ();
        if (isFinishing ())
            SendCleanupNotify ();
    }
    protected void onDestroy () {
        super.onDestroy ();
        SendCleanupNotify ();
        rg_n12780 ();
    }
    private boolean m_blCleanupMethodCalled;
    void SendCleanupNotify () {
        if (m_blCleanupMethodCalled == false) {
            m_blCleanupMethodCalled = true;
            rg_n12778 ();
        }
    }
    @Override protected void onCreate (android.os.Bundle savedInstanceState) {
        super.onCreate (savedInstanceState);
        rg_n581.sPermitDiskAndNetworkOperInsideUIThread ();
        if (getClass ().equals (twothree.ceshi.rg_n.class))
            rg_n581.sOnStartupClassEnter ();
        android.content.Intent objIntent = getIntent ();
        final int nParamDataIdentifier = objIntent.getIntExtra (cs_strActivityLoadParams, 0);
        Object[] aryParams = rg_n581.sGetGlobalDataCache ().Pop (nParamDataIdentifier);
        if (nParamDataIdentifier != 0 && aryParams == null)
            rg_n581.sForceRestart ();
        if (onInitAndroidActivity () == false) {
            finish ();
            return;
        }
        rg_n29 (objIntent, aryParams, (aryParams == null ? 0 : aryParams.length));
    }
    @Override public boolean onCreateOptionsMenu (android.view.Menu menu) {
        final boolean blDisplay = rg_n12782 (menu);
        return (super.onCreateOptionsMenu (menu) && blDisplay);
    }
    @Override public boolean onPrepareOptionsMenu (android.view.Menu menu) {
        final boolean blDisplay = rg_n12784 (menu);
        return (super.onPrepareOptionsMenu (menu) && blDisplay);
    }
    @Override public boolean onOptionsItemSelected (android.view.MenuItem item) {
        if (rg_n12789 (item, false))
            return true;
        return super.onOptionsItemSelected (item);
    }
    @Override public void onOptionsMenuClosed (android.view.Menu menu) {
        rg_n12792 (menu, false);
         super.onOptionsMenuClosed (menu);
    }
    @Override public boolean onContextItemSelected (android.view.MenuItem item) {
        if (rg_n12789 (item, true))
            return true;
        return super.onContextItemSelected (item);
    }
    @Override public void onContextMenuClosed (android.view.Menu menu) {
        rg_n12792 (menu, true);
        super.onContextMenuClosed (menu);
    }
    @Override public void onCreateContextMenu (android.view.ContextMenu menu, View v, android.view.ContextMenu.ContextMenuInfo menuInfo) {
        AndroidView volView = AndroidView.sSafeGetVolView (v);
        if (volView != null)
            rg_n12786 (volView, menu);
        super.onCreateContextMenu (menu, v, menuInfo);
    }
    protected void onActivityResult (int requestCode, int resultCode, android.content.Intent data) {
        super.onActivityResult (requestCode, resultCode, data);
        rg_n12795 (requestCode, resultCode, data);
    }
    @Override public boolean dispatchKeyEvent (android.view.KeyEvent event) {
        if (rg_n12803 (event))
            return true;
        return super.dispatchKeyEvent (event);
    }
    @Override public boolean dispatchKeyShortcutEvent (android.view.KeyEvent event) {
        if (rg_n12805 (event))
            return true;
        return super.dispatchKeyShortcutEvent (event);
    }
    @Override public boolean dispatchTouchEvent (android.view.MotionEvent event) {
        if (rg_n12811 (event))
            return true;
        return super.dispatchTouchEvent (event);
    }
    @Override public boolean dispatchTrackballEvent (android.view.MotionEvent event) {
        if (rg_n12815 (event))
            return true;
        return super.dispatchTrackballEvent (event);
    }
    @Override public boolean dispatchGenericMotionEvent (android.view.MotionEvent event) {
        if (rg_n12799 (event))
            return true;
        return super.dispatchGenericMotionEvent (event);
    }
    @Override public boolean onTouchEvent (android.view.MotionEvent event) {
        if (rg_n12813 (event))
            return true;
        return super.onTouchEvent (event);
    }
    @Override public boolean onGenericMotionEvent (android.view.MotionEvent event) {
        if (rg_n12801 (event))
            return true;
        return super.onGenericMotionEvent (event);
    }
    @Override public boolean onTrackballEvent (android.view.MotionEvent event) {
        if (rg_n12817 (event))
            return true;
        return super.onTrackballEvent (event);
    }
    @Override public boolean onKeyDown (int keyCode, android.view.KeyEvent event) {
        if (rg_n12807 (rg_n12730.rg_n12731, keyCode, event))
            return true;
        return super.onKeyDown (keyCode, event);
    }
    @Override public boolean onKeyLongPress (int keyCode, android.view.KeyEvent event) {
        if (rg_n12807 (rg_n12730.rg_n12733, keyCode, event))
            return true;
        return super.onKeyLongPress (keyCode, event);
    }
    @Override public boolean onKeyMultiple (int keyCode, int repeatCount, android.view.KeyEvent event) {
        if (rg_n12807 (rg_n12730.rg_n12734, keyCode, event))
            return true;
        return super.onKeyMultiple (keyCode, repeatCount, event);
    }
    @Override public boolean onKeyShortcut (int keyCode, android.view.KeyEvent event) {
        if (rg_n12807 (rg_n12730.rg_n12735, keyCode, event))
            return true;
        return super.onKeyShortcut (keyCode, event);
    }
    @Override public boolean onKeyUp (int keyCode, android.view.KeyEvent event) {
        if (rg_n12807 (rg_n12730.rg_n12732, keyCode, event))
            return true;
        return super.onKeyUp (keyCode, event);
    }
    @Override public void onBackPressed () {
        if (rg_n12819 ())
            return;
        super.onBackPressed ();
    }
    @Override public void onUserInteraction () {
        super.onUserInteraction ();
        rg_n12821 ();
    }
    @Override public void onUserLeaveHint () {
        rg_n12822 ();
        super.onUserLeaveHint ();
    }
    @Override public void onWindowFocusChanged (boolean hasFocus) {
        super.onWindowFocusChanged (hasFocus);
        rg_n12823 (hasFocus);
    }
    @Override public CharSequence onCreateDescription () {
        final String strDesc = rg_n12820 ();
        return (strDesc != null ? strDesc : super.onCreateDescription ());
    }

    public AndroidViewGroup GetAndroidActivityContainer () {
        return (null);
    }

    public void rg_n29 (android.content.Intent rg_n12769, java.lang.Object [] rg_n12770, int rg_n12771) {
    }

    public void rg_n12772 () {
    }

    public void rg_n12773 () {
    }

    public void rg_n12774 (android.content.Intent rg_n12775) {
    }

    public void rg_n12776 () {
    }

    public void rg_n12777 () {
    }

    public void rg_n12778 () {
    }

    public void rg_n12779 () {
    }

    public void rg_n12780 () {
    }

    public void rg_n12781 () {
    }

    public boolean rg_n12782 (android.view.Menu rg_n12783) {
        return (true);
    }

    public boolean rg_n12784 (android.view.Menu rg_n12785) {
        return (true);
    }

    public void rg_n12786 (AndroidView rg_n12787, android.view.ContextMenu rg_n12788) {
    }

    public boolean rg_n12789 (android.view.MenuItem rg_n12790, boolean rg_n12791) {
        return (false);
    }

    public void rg_n12792 (android.view.Menu rg_n12793, boolean rg_n12794) {
    }

    public void rg_n12795 (int rg_n12796, int rg_n12797, android.content.Intent rg_n12798) {
    }

    public boolean rg_n12799 (android.view.MotionEvent rg_n12800) {
        return (false);
    }

    public boolean rg_n12801 (android.view.MotionEvent rg_n12802) {
        return (false);
    }

    public boolean rg_n12803 (android.view.KeyEvent rg_n12804) {
        return (false);
    }

    public boolean rg_n12805 (android.view.KeyEvent rg_n12806) {
        return (false);
    }

    public boolean rg_n12807 (int rg_n12808, int rg_n12809, android.view.KeyEvent rg_n12810) {
        return (false);
    }

    public boolean rg_n12811 (android.view.MotionEvent rg_n12812) {
        return (false);
    }

    public boolean rg_n12813 (android.view.MotionEvent rg_n12814) {
        return (false);
    }

    public boolean rg_n12815 (android.view.MotionEvent rg_n12816) {
        return (false);
    }

    public boolean rg_n12817 (android.view.MotionEvent rg_n12818) {
        return (false);
    }

    public boolean rg_n12819 () {
        return (false);
    }

    public String rg_n12820 () {
        return (null);
    }

    public void rg_n12821 () {
    }

    public void rg_n12822 () {
    }

    public void rg_n12823 (boolean rg_n12824) {
    }
}
