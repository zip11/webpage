
package hsh.anzh.tyxzq;

public class rg_n12998 extends hsh.Java.jb.rg_n16405 implements android.content.DialogInterface.OnDismissListener,cn.qqtheme.framework.picker.FilePicker.OnFilePickListener {

    public rg_n12998 ()  { }

    protected cn.qqtheme.framework.picker.FilePicker filePicker;
    private rg_n12998 (android.app.Activity activity, int mode) {
        init (activity, mode);
    }
    void init (android.app.Activity activity, int mode) {
        this.filePicker = new cn.qqtheme.framework.picker.FilePicker(activity, mode);
        this.filePicker.setOnDismissListener(this);
        this.filePicker.setOnFilePickListener(this);
    }
    @Override
    public void onDismiss(android.content.DialogInterface dialogInterface) {
        rg_n13094();
    }
    @Override
    public void onFilePicked(String s) {
        rg_n13095(s);
    }
    public cn.qqtheme.framework.picker.FilePicker getPicker() {
        return this.filePicker;
    }

    public static rg_n12998 rg_n13001 (android.app.Activity rg_n13002, boolean rg_n13003) {
        return new rg_n12998 (rg_n13002, rg_n13003 ? 1 : 0);
    }

    public void rg_n13004 (String rg_n13005) {
        getPicker().setRootPath(rg_n13005);
    }

    public void rg_n13006 (int rg_n13007) {
        getPicker().getAdapter().setTextColor(rg_n13007);
    }

    public void rg_n13008 (int rg_n13009) {
        getPicker().getPathAdapter().setTextColor(rg_n13009);
    }

    public void rg_n13011 (boolean rg_n13012) {
        getPicker().setShowUpDir(rg_n13012);
    }

    public void rg_n13015 (boolean rg_n13016) {
        getPicker().setShowHideDir(rg_n13016);
    }

    public void rg_n13029 (String rg_n13030) {
        getPicker().setEmptyHint(rg_n13030);
    }

    public static interface re_n13094 { int dispatch (rg_n12998 objSource, int nTagNumber); }
    private re_n13094 rd_n13094;
    private int rd_n13094_tag;
    public void rl_n12998_n13094 (re_n13094 objListener, int nTagNumber) {
        synchronized (this) { rd_n13094 = objListener;  rd_n13094_tag = nTagNumber; }
    }
    public int rg_n13094 () {
        re_n13094 objDispatcher;  int nTagNumber;
        synchronized (this) { objDispatcher = rd_n13094;  nTagNumber = rd_n13094_tag; }
        return (objDispatcher != null ? objDispatcher.dispatch (this, nTagNumber) : 0);
    }

    public static interface re_n13095 { int dispatch (rg_n12998 objSource, int nTagNumber, String rg_n13096); }
    private re_n13095 rd_n13095;
    private int rd_n13095_tag;
    public void rl_n12998_n13095 (re_n13095 objListener, int nTagNumber) {
        synchronized (this) { rd_n13095 = objListener;  rd_n13095_tag = nTagNumber; }
    }
    public int rg_n13095 (String rg_n13096) {
        re_n13095 objDispatcher;  int nTagNumber;
        synchronized (this) { objDispatcher = rd_n13095;  nTagNumber = rd_n13095_tag; }
        return (objDispatcher != null ? objDispatcher.dispatch (this, nTagNumber, rg_n13096) : 0);
    }
}
