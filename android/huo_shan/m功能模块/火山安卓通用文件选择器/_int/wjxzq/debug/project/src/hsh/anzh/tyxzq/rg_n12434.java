
package hsh.anzh.tyxzq;

public class rg_n12434 extends hsh.Java.jb.rg_n15841 implements android.content.DialogInterface.OnDismissListener,cn.qqtheme.framework.picker.FilePicker.OnFilePickListener {

    public rg_n12434 ()  { }

    protected cn.qqtheme.framework.picker.FilePicker filePicker;
    private rg_n12434 (android.app.Activity activity, int mode) {
        init (activity, mode);
    }
    void init (android.app.Activity activity, int mode) {
        this.filePicker = new cn.qqtheme.framework.picker.FilePicker(activity, mode);
        this.filePicker.setOnDismissListener(this);
        this.filePicker.setOnFilePickListener(this);
    }
    @Override
    public void onDismiss(android.content.DialogInterface dialogInterface) {
        rg_n12530();
    }
    @Override
    public void onFilePicked(String s) {
        rg_n12531(s);
    }
    public cn.qqtheme.framework.picker.FilePicker getPicker() {
        return this.filePicker;
    }

    public static rg_n12434 rg_n12437 (android.app.Activity rg_n12438, boolean rg_n12439) {
        return new rg_n12434 (rg_n12438, rg_n12439 ? 1 : 0);
    }

    public void rg_n12440 (String rg_n12441) {
        getPicker().setRootPath(rg_n12441);
    }

    public void rg_n12442 (int rg_n12443) {
        getPicker().getAdapter().setTextColor(rg_n12443);
    }

    public void rg_n12444 (int rg_n12445) {
        getPicker().getPathAdapter().setTextColor(rg_n12445);
    }

    public void rg_n12447 (boolean rg_n12448) {
        getPicker().setShowUpDir(rg_n12448);
    }

    public void rg_n12451 (boolean rg_n12452) {
        getPicker().setShowHideDir(rg_n12452);
    }

    public void rg_n12465 (String rg_n12466) {
        getPicker().setEmptyHint(rg_n12466);
    }

    public static interface re_n12530 { int dispatch (rg_n12434 objSource, int nTagNumber); }
    private re_n12530 rd_n12530;
    private int rd_n12530_tag;
    public void rl_n12434_n12530 (re_n12530 objListener, int nTagNumber) {
        synchronized (this) { rd_n12530 = objListener;  rd_n12530_tag = nTagNumber; }
    }
    public int rg_n12530 () {
        re_n12530 objDispatcher;  int nTagNumber;
        synchronized (this) { objDispatcher = rd_n12530;  nTagNumber = rd_n12530_tag; }
        return (objDispatcher != null ? objDispatcher.dispatch (this, nTagNumber) : 0);
    }

    public static interface re_n12531 { int dispatch (rg_n12434 objSource, int nTagNumber, String rg_n12532); }
    private re_n12531 rd_n12531;
    private int rd_n12531_tag;
    public void rl_n12434_n12531 (re_n12531 objListener, int nTagNumber) {
        synchronized (this) { rd_n12531 = objListener;  rd_n12531_tag = nTagNumber; }
    }
    public int rg_n12531 (String rg_n12532) {
        re_n12531 objDispatcher;  int nTagNumber;
        synchronized (this) { objDispatcher = rd_n12531;  nTagNumber = rd_n12531_tag; }
        return (objDispatcher != null ? objDispatcher.dispatch (this, nTagNumber, rg_n12532) : 0);
    }
}
