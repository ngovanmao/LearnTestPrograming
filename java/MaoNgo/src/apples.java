import java.util.Scanner;
class apples {
	public static void main(String args[]){
		System.out.println("Hello youtube!");
		Scanner mao = new Scanner(System.in);
		System.out.println(mao.nextLine());
		
		double fnum, snum, answer;
		System.out.println("Enter first num:");
		fnum = mao.nextDouble();
		System.out.println("Enter second num:");
		snum = mao.nextDouble();
		answer = fnum + snum;
		System.out.println(answer);
	}
	

}
