
package hsh.anzh.jb;

import android.app.Activity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.*;

public class rg_n5087 extends rg_n4866 {

    public rg_n5087 ()  { }

    public rg_n5087 (android.content.Context context, Button view, Object objInitData) { super (context, view, objInitData); }
    public rg_n5087 (android.content.Context context, Button view) { this (context, view, null); }
    public Button GetButton () { return (Button)GetView (); }
    public static rg_n5087 sNewInstance (android.content.Context context) {
        return sNewInstanceAndAttachView (context, new Button (context), null);
    }
    public static rg_n5087 sNewInstance (android.content.Context context, Object objInitData) {
        return sNewInstanceAndAttachView (context, new Button (context), objInitData);
    }
    public static rg_n5087 sNewInstanceAndAttachView (android.content.Context context, Button viewAttach) {
        return sNewInstanceAndAttachView (context, viewAttach, null);
    }
    public static rg_n5087 sNewInstanceAndAttachView (android.content.Context context, Button viewAttach, Object objInitData) {
        rg_n5087 objControl = new rg_n5087 (context, viewAttach, objInitData);
        objControl.onInitControlContent (context, objInitData);
        return objControl;
    }
    protected void OnInitView (android.content.Context context, Object objInitData) {
        super.OnInitView (context, objInitData);
        rg_n3082 (true);
    }
}
