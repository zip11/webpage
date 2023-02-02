
package hsh.chx;

import android.app.Activity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.*;

public class rg_n extends hsh.anzh.jb.rg_n12204 {

    public rg_n ()  { }

    protected hsh.anzh.jb.rg_n5087 rg_n1;
    protected hsh.anzh.tyxzq.rg_n12434 rg_n2;

    protected hsh.anzh.jb.rg_n3980 rp_1;
    @Override public hsh.anzh.jb.AndroidViewGroup GetAndroidActivityContainer () {
        return rp_1;
    }

    @Override
    protected boolean onInitAndroidActivity () {
        if (super.onInitAndroidActivity () == false)
            return false;

        setContentView (R.layout.rg_n);
        rp_1 = new hsh.anzh.jb.rg_n3980 (this, (LinearLayout)findViewById (R.id.rg_n));
        rp_1.onInitControlContent (this, null);

        rg_n1 = new hsh.anzh.jb.rg_n5087 (this, (Button)findViewById (R.id.rg_n1));
        rg_n1.onInitControlContent (this, null);
        rg_n1.rl_AndroidView_n3060 (new hsh.anzh.jb.AndroidView.re_n3060 () {
            public int dispatch (hsh.anzh.jb.AndroidView objSource, int nTagNumber) {
                return rg_n14 ((hsh.anzh.jb.rg_n5087)objSource, nTagNumber);
            }
        }, 0);
        return true;
    }

    public void rg_n3 (android.content.Intent rg_n4, java.lang.Object [] rg_n5, int rg_n6) {
        super.rg_n3 (rg_n4, rg_n5, rg_n6);
        rg_n7 ();
    }

    protected void rg_n7 () {
        rg_n2 = hsh.anzh.tyxzq.rg_n12434.rg_n12437 (this, true);
        rg_n2.rl_n12434_n12531 (new hsh.anzh.tyxzq.rg_n12434.re_n12531 () {
            public int dispatch (hsh.anzh.tyxzq.rg_n12434 objSource, int nTagNumber, String rg_n12532) {
                return rg_n8 (objSource, nTagNumber, rg_n12532);
            }
        }, 0);
        rg_n2.rg_n12447 (true);
        rg_n2.rg_n15842 = "文件选择器";
        rg_n2.rg_n12451 (true);
        rg_n2.rg_n12442 (hsh.anzh.jb.rg_n5661.rg_n5662);
        rg_n2.rg_n12444 (hsh.anzh.jb.rg_n5661.rg_n5664);
        rg_n2.rg_n12440 ("sdcard");
        rg_n2.rg_n12465 ("没有文件了！");
    }

    protected int rg_n8 (hsh.anzh.tyxzq.rg_n12434 rg_n9, int rg_n10, String rg_n11) {
        int rg_n12;
        String rg_n13;
        rg_n12 = rg_n11.lastIndexOf ("/") + 1;
        rg_n13 = hsh.Java.jb.rg_n17223.rg_n17371 (rg_n11, rg_n11.length () - rg_n12);
        hsh.anzh.jb.AndComActivity.rg_n2415 (this, rg_n13);
        return (0);
    }

    protected int rg_n14 (hsh.anzh.jb.rg_n5087 rg_n15, int rg_n16) {
        rg_n2.getPicker().show();
        return (0);
    }
}
