public class while1 {
	public static void main(String[] args) {

		int sum = 0;
        int m = 1;
		int n = 4;
		
        // 使用do while计算M+...+N:
		do {
            
            sum = sum + m;
            m = m + 1;

        } while (m <= n);
		
        System.out.println(sum);
	}
}
