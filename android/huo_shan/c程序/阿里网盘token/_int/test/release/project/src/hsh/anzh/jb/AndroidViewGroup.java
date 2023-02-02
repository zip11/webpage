
package hsh.anzh.jb;

import android.app.Activity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.*;

public class AndroidViewGroup extends AndroidView {

    public AndroidViewGroup ()  { }

    public AndroidViewGroup (android.content.Context context, ViewGroup view, Object objInitData) { super (context, view, objInitData); }
    public AndroidViewGroup (android.content.Context context, ViewGroup view) { this (context, view, null); }
    public ViewGroup GetViewGroup () { return (ViewGroup)GetView (); }
    public static AndroidViewGroup sNewInstance (android.content.Context context) {
        return null;
    }
    public static AndroidViewGroup sNewInstance (android.content.Context context, Object objInitData) {
        return null;
    }
}
