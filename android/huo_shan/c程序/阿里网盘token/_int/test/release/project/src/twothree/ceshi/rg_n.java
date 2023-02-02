
package twothree.ceshi;

import android.app.Activity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.*;

public class rg_n extends hsh.anzh.jb.rg_n12840 {

    public rg_n ()  { }

    protected hsh.anzh.jb.rg_n5651 rg_n1;
    protected hsh.anzh.jb.rg_n5651 rg_n2;
    protected hsh.anzh.jb.rg_n5637 rg_n3;
    protected hsh.anzh.jb.rg_n5637 rg_n4;
    protected hsh.anzh.jb.rg_n5430 rg_n5;
    protected hsh.anzh.jb.rg_n5637 rg_n6;
    protected String rg_n7 = "";
    protected hsh.anzh.tyxzq.rg_n12998 rg_n8;

    protected hsh.anzh.jb.rg_n4544 rp_1;
    @Override public hsh.anzh.jb.AndroidViewGroup GetAndroidActivityContainer () {
        return rp_1;
    }

    @Override
    protected boolean onInitAndroidActivity () {
        if (super.onInitAndroidActivity () == false)
            return false;

        setContentView (R.layout.rg_n);
        rp_1 = new hsh.anzh.jb.rg_n4544 (this, (LinearLayout)findViewById (R.id.rg_n));
        rp_1.onInitControlContent (this, null);

        rg_n1 = new hsh.anzh.jb.rg_n5651 (this, (Button)findViewById (R.id.rg_n1));
        rg_n1.onInitControlContent (this, null);
        rg_n1.rl_AndroidView_n3624 (new hsh.anzh.jb.AndroidView.re_n3624 () {
            public int dispatch (hsh.anzh.jb.AndroidView objSource, int nTagNumber) {
                return rg_n9 ((hsh.anzh.jb.rg_n5651)objSource, nTagNumber);
            }
        }, 0);
        rg_n2 = new hsh.anzh.jb.rg_n5651 (this, (Button)findViewById (R.id.rg_n2));
        rg_n2.onInitControlContent (this, null);
        rg_n2.rl_AndroidView_n3624 (new hsh.anzh.jb.AndroidView.re_n3624 () {
            public int dispatch (hsh.anzh.jb.AndroidView objSource, int nTagNumber) {
                return rg_n9 ((hsh.anzh.jb.rg_n5651)objSource, nTagNumber);
            }
        }, 0);
        rg_n3 = new hsh.anzh.jb.rg_n5637 (this, (EditText)findViewById (R.id.rg_n3));
        rg_n3.onInitControlContent (this, null);
        rg_n4 = new hsh.anzh.jb.rg_n5637 (this, (EditText)findViewById (R.id.rg_n4));
        rg_n4.onInitControlContent (this, null);
        rg_n5 = new hsh.anzh.jb.rg_n5430 (this, (TextView)findViewById (R.id.rg_n5));
        rg_n5.onInitControlContent (this, null);
        rg_n6 = new hsh.anzh.jb.rg_n5637 (this, (EditText)findViewById (R.id.rg_n6));
        rg_n6.onInitControlContent (this, null);
        return true;
    }

    protected int rg_n9 (hsh.anzh.jb.rg_n5651 rg_n10, int rg_n11) {
        if (rg_n10 == rg_n1)
        {
            rg_n8.getPicker().show();
        }
        if (rg_n10 == rg_n2)
        {
            hsh.anzh.jb.rg_n12401.dbg_log (("log file:" + rg_n7), "");
            String rg_n12;
            java.util.ArrayList<String> rg_n13 = new java.util.ArrayList<String> ();
            rg_n12 = rg_n7;
            hsh.anzh.jb.rg_n12401.dbg_log (("sd path:" + rg_n12), "");
            rg_n13 = hsh.Java.jb.rg_n15639.rg_n15658 (rg_n12, hsh.Java.jb.rg_n17741.rg_n17742);
            hsh.anzh.jb.rg_n12401.dbg_log (("txt content:" + String.valueOf (rg_n13)), "");
            int rg_n14 = 0;
            String rg_n15;
            hsh.anzh.jb.rg_n12401.dbg_log (("txtc.取成员数" + String.valueOf (rg_n13.size ())), "");
            for (rg_n14 = rg_n13.size (); rg_n14 > 0; rg_n14--)
            {
                rg_n15 = rg_n13.get (rg_n14 - 1);
                if (rg_n15.contains ("refreshToken"))
                {
                    hsh.anzh.jb.rg_n12401.dbg_log ("token find ok", "");
                    rg_n6.rg_n5570 (rg_n15 + "\n");
                    String rg_n17;
                    rg_n17 = rg_n18 (rg_n15, "refreshToken");
                    rg_n4.rg_n5450 ("");
                    rg_n4.rg_n5450 (rg_n17);
                    hsh.anzh.jb.rg_n2628.rg_n2641 (rg_n17, null);
                    break;
                }
                else
                {
                    hsh.anzh.jb.rg_n12401.dbg_log ("find token  text error", "");
                }
            }
        }
        return (0);
    }

    public String rg_n18 (String rg_n19, String rg_n20) {
        int rg_n21;
        String rg_n22;
        rg_n21 = rg_n19.lastIndexOf (rg_n20);
        hsh.anzh.jb.rg_n12401.dbg_log (("token text num:" + String.valueOf (rg_n21)), "");
        rg_n22 = hsh.Java.jb.rg_n17787.rg_n17924 (rg_n19, rg_n21 + 15, 32);
        hsh.anzh.jb.rg_n12401.dbg_log (("token text：" + rg_n22), "");
        return (rg_n22);
    }

    public void rg_n29 (android.content.Intent rg_n30, java.lang.Object [] rg_n31, int rg_n32) {
        super.rg_n29 (rg_n30, rg_n31, rg_n32);
        rg_n34 ();
        if (this.checkSelfPermission(hsh.anzh.jb.rg_n11585.rg_n11590) == -1)
        {
            String [] rg_n33 = new String [1];
            rg_n33 [0] = hsh.anzh.jb.rg_n11585.rg_n11590;
            rg_n12844 (rg_n33, 111);
        }
        else
        {
            hsh.anzh.jb.AndComActivity.rg_n2979 (this, "read sd quan xian  ok");
        }
    }

    protected void rg_n34 () {
        rg_n8 = hsh.anzh.tyxzq.rg_n12998.rg_n13001 (this, true);
        rg_n8.rl_n12998_n13095 (new hsh.anzh.tyxzq.rg_n12998.re_n13095 () {
            public int dispatch (hsh.anzh.tyxzq.rg_n12998 objSource, int nTagNumber, String rg_n13096) {
                return rg_n35 (objSource, nTagNumber, rg_n13096);
            }
        }, 0);
        rg_n8.rg_n13011 (true);
        rg_n8.rg_n16406 = "文件选择器";
        rg_n8.rg_n13015 (true);
        rg_n8.rg_n13006 (hsh.anzh.jb.rg_n6225.rg_n6226);
        rg_n8.rg_n13008 (hsh.anzh.jb.rg_n6225.rg_n6228);
        rg_n8.rg_n13004 ("sdcard");
        rg_n8.rg_n13029 ("没有文件了！");
    }

    protected int rg_n35 (hsh.anzh.tyxzq.rg_n12998 rg_n36, int rg_n37, String rg_n38) {
        if (rg_n36 == rg_n8)
        {
            rg_n7 = rg_n38;
            hsh.anzh.jb.rg_n12401.dbg_log (rg_n7, "");
            rg_n3.rg_n5450 (rg_n7);
        }
        return (0);
    }
}
