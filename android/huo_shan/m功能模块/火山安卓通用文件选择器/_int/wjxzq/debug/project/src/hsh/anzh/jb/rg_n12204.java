
package hsh.anzh.jb;

import android.app.Activity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.*;

public class rg_n12204 extends android.app.Activity {

    private static final String cs_strActivityLoadParams = "@activity_params";
    protected boolean onInitAndroidActivity () {
        if (rg_n17.sCheckRestart (this) == false)
            return false;
        rg_n12217 ();
        return true;
    }
    protected void onStart ()    {  super.onStart ();  m_blCleanupMethodCalled = false;  rg_n12208 ();  }
    protected void onRestart ()  {  super.onRestart ();  rg_n12209 ();  }
    protected void onResume ()   {  super.onResume ();  rg_n12212 ();  }
    protected void onPause ()    {  super.onPause ();  rg_n12213 ();  }
    protected void onNewIntent(android.content.Intent intent) { super.onNewIntent(intent); rg_n12210 (intent);  }
    protected void onStop () {
        super.onStop ();
        rg_n12215 ();
        if (isChangingConfigurations ())
            rg_n17.sForceRestart  ();
        if (isFinishing ())
            SendCleanupNotify ();
    }
    protected void onDestroy () {
        super.onDestroy ();
        SendCleanupNotify ();
        rg_n12216 ();
    }
    private boolean m_blCleanupMethodCalled;
    void SendCleanupNotify () {
        if (m_blCleanupMethodCalled == false) {
            m_blCleanupMethodCalled = true;
            rg_n12214 ();
        }
    }
    @Override protected void onCreate (android.os.Bundle savedInstanceState) {
        super.onCreate (savedInstanceState);
        rg_n17.sPermitDiskAndNetworkOperInsideUIThread ();
        if (getClass ().equals (hsh.chx.rg_n.class))
            rg_n17.sOnStartupClassEnter ();
        android.content.Intent objIntent = getIntent ();
        final int nParamDataIdentifier = objIntent.getIntExtra (cs_strActivityLoadParams, 0);
        Object[] aryParams = rg_n17.sGetGlobalDataCache ().Pop (nParamDataIdentifier);
        if (nParamDataIdentifier != 0 && aryParams == null)
            rg_n17.sForceRestart ();
        if (onInitAndroidActivity () == false) {
            finish ();
            return;
        }
        rg_n3 (objIntent, aryParams, (aryParams == null ? 0 : aryParams.length));
    }
    @Override public boolean onCreateOptionsMenu (android.view.Menu menu) {
        final boolean blDisplay = rg_n12218 (menu);
        return (super.onCreateOptionsMenu (menu) && blDisplay);
    }
    @Override public boolean onPrepareOptionsMenu (android.view.Menu menu) {
        final boolean blDisplay = rg_n12220 (menu);
        return (super.onPrepareOptionsMenu (menu) && blDisplay);
    }
    @Override public boolean onOptionsItemSelected (android.view.MenuItem item) {
        if (rg_n12225 (item, false))
            return true;
        return super.onOptionsItemSelected (item);
    }
    @Override public void onOptionsMenuClosed (android.view.Menu menu) {
        rg_n12228 (menu, false);
         super.onOptionsMenuClosed (menu);
    }
    @Override public boolean onContextItemSelected (android.view.MenuItem item) {
        if (rg_n12225 (item, true))
            return true;
        return super.onContextItemSelected (item);
    }
    @Override public void onContextMenuClosed (android.view.Menu menu) {
        rg_n12228 (menu, true);
        super.onContextMenuClosed (menu);
    }
    @Override public void onCreateContextMenu (android.view.ContextMenu menu, View v, android.view.ContextMenu.ContextMenuInfo menuInfo) {
        AndroidView volView = AndroidView.sSafeGetVolView (v);
        if (volView != null)
            rg_n12222 (volView, menu);
        super.onCreateContextMenu (menu, v, menuInfo);
    }
    protected void onActivityResult (int requestCode, int resultCode, android.content.Intent data) {
        super.onActivityResult (requestCode, resultCode, data);
        rg_n12231 (requestCode, resultCode, data);
    }
    @Override public boolean dispatchKeyEvent (android.view.KeyEvent event) {
        if (rg_n12239 (event))
            return true;
        return super.dispatchKeyEvent (event);
    }
    @Override public boolean dispatchKeyShortcutEvent (android.view.KeyEvent event) {
        if (rg_n12241 (event))
            return true;
        return super.dispatchKeyShortcutEvent (event);
    }
    @Override public boolean dispatchTouchEvent (android.view.MotionEvent event) {
        if (rg_n12247 (event))
            return true;
        return super.dispatchTouchEvent (event);
    }
    @Override public boolean dispatchTrackballEvent (android.view.MotionEvent event) {
        if (rg_n12251 (event))
            return true;
        return super.dispatchTrackballEvent (event);
    }
    @Override public boolean dispatchGenericMotionEvent (android.view.MotionEvent event) {
        if (rg_n12235 (event))
            return true;
        return super.dispatchGenericMotionEvent (event);
    }
    @Override public boolean onTouchEvent (android.view.MotionEvent event) {
        if (rg_n12249 (event))
            return true;
        return super.onTouchEvent (event);
    }
    @Override public boolean onGenericMotionEvent (android.view.MotionEvent event) {
        if (rg_n12237 (event))
            return true;
        return super.onGenericMotionEvent (event);
    }
    @Override public boolean onTrackballEvent (android.view.MotionEvent event) {
        if (rg_n12253 (event))
            return true;
        return super.onTrackballEvent (event);
    }
    @Override public boolean onKeyDown (int keyCode, android.view.KeyEvent event) {
        if (rg_n12243 (rg_n12166.rg_n12167, keyCode, event))
            return true;
        return super.onKeyDown (keyCode, event);
    }
    @Override public boolean onKeyLongPress (int keyCode, android.view.KeyEvent event) {
        if (rg_n12243 (rg_n12166.rg_n12169, keyCode, event))
            return true;
        return super.onKeyLongPress (keyCode, event);
    }
    @Override public boolean onKeyMultiple (int keyCode, int repeatCount, android.view.KeyEvent event) {
        if (rg_n12243 (rg_n12166.rg_n12170, keyCode, event))
            return true;
        return super.onKeyMultiple (keyCode, repeatCount, event);
    }
    @Override public boolean onKeyShortcut (int keyCode, android.view.KeyEvent event) {
        if (rg_n12243 (rg_n12166.rg_n12171, keyCode, event))
            return true;
        return super.onKeyShortcut (keyCode, event);
    }
    @Override public boolean onKeyUp (int keyCode, android.view.KeyEvent event) {
        if (rg_n12243 (rg_n12166.rg_n12168, keyCode, event))
            return true;
        return super.onKeyUp (keyCode, event);
    }
    @Override public void onBackPressed () {
        if (rg_n12255 ())
            return;
        super.onBackPressed ();
    }
    @Override public void onUserInteraction () {
        super.onUserInteraction ();
        rg_n12257 ();
    }
    @Override public void onUserLeaveHint () {
        rg_n12258 ();
        super.onUserLeaveHint ();
    }
    @Override public void onWindowFocusChanged (boolean hasFocus) {
        super.onWindowFocusChanged (hasFocus);
        rg_n12259 (hasFocus);
    }
    @Override public CharSequence onCreateDescription () {
        final String strDesc = rg_n12256 ();
        return (strDesc != null ? strDesc : super.onCreateDescription ());
    }

    public AndroidViewGroup GetAndroidActivityContainer () {
        return (null);
    }

    public void rg_n3 (android.content.Intent rg_n12205, java.lang.Object [] rg_n12206, int rg_n12207) {
    }

    public void rg_n12208 () {
    }

    public void rg_n12209 () {
    }

    public void rg_n12210 (android.content.Intent rg_n12211) {
    }

    public void rg_n12212 () {
    }

    public void rg_n12213 () {
    }

    public void rg_n12214 () {
    }

    public void rg_n12215 () {
    }

    public void rg_n12216 () {
    }

    public void rg_n12217 () {
    }

    public boolean rg_n12218 (android.view.Menu rg_n12219) {
        return (true);
    }

    public boolean rg_n12220 (android.view.Menu rg_n12221) {
        return (true);
    }

    public void rg_n12222 (AndroidView rg_n12223, android.view.ContextMenu rg_n12224) {
    }

    public boolean rg_n12225 (android.view.MenuItem rg_n12226, boolean rg_n12227) {
        return (false);
    }

    public void rg_n12228 (android.view.Menu rg_n12229, boolean rg_n12230) {
    }

    public void rg_n12231 (int rg_n12232, int rg_n12233, android.content.Intent rg_n12234) {
    }

    public boolean rg_n12235 (android.view.MotionEvent rg_n12236) {
        return (false);
    }

    public boolean rg_n12237 (android.view.MotionEvent rg_n12238) {
        return (false);
    }

    public boolean rg_n12239 (android.view.KeyEvent rg_n12240) {
        return (false);
    }

    public boolean rg_n12241 (android.view.KeyEvent rg_n12242) {
        return (false);
    }

    public boolean rg_n12243 (int rg_n12244, int rg_n12245, android.view.KeyEvent rg_n12246) {
        return (false);
    }

    public boolean rg_n12247 (android.view.MotionEvent rg_n12248) {
        return (false);
    }

    public boolean rg_n12249 (android.view.MotionEvent rg_n12250) {
        return (false);
    }

    public boolean rg_n12251 (android.view.MotionEvent rg_n12252) {
        return (false);
    }

    public boolean rg_n12253 (android.view.MotionEvent rg_n12254) {
        return (false);
    }

    public boolean rg_n12255 () {
        return (false);
    }

    public String rg_n12256 () {
        return (null);
    }

    public void rg_n12257 () {
    }

    public void rg_n12258 () {
    }

    public void rg_n12259 (boolean rg_n12260) {
    }
}
