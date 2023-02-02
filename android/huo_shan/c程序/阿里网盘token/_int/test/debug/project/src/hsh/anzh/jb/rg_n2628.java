
package hsh.anzh.jb;

public class rg_n2628 {

    public rg_n2628 ()  { }

    android.content.ClipboardManager.OnPrimaryClipChangedListener m_listener;

    public static void rg_n2641 (String rg_n2642, String rg_n2643) {
        android.content.ClipboardManager mgrClip = (android.content.ClipboardManager)rg_n581.sGetApp ().getSystemService (android.content.Context.CLIPBOARD_SERVICE);
        mgrClip.setPrimaryClip (android.content.ClipData.newPlainText (rg_n2643, rg_n2642));
    }
}
