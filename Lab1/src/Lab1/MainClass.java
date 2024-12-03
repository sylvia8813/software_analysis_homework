package Lab1;

class Book{
	public String bname;
	public int price;
	public String isbn;
	
	public Book(String bname, String isbn, int price){
		this.bname=bname;
		this.isbn=isbn;
		this.price=price;
	}
	
	public String get_bname() {
		return bname;
	}
	
	public int get_price(){
		return price;
	}
	
	public String get_isbn() {
		return isbn;
	}
	
	public int get_shipping() {
		return (price > 100) ? 50 : 20;
	}

}

public class MainClass {
	public static void main(String[] args) {
		Book w1 = new Book("BOOK1", "ISBN1", 85);
		Book w2 = new Book("BOOK2", "ISBN2", 135);
		String str1 = w1.get_bname() + "," + w1.get_isbn();
		str1 += "," + (w1.get_price() + w1.get_shipping());
		String str2 = w2.get_bname() + "," + w2.get_isbn();
		str2 += "," + (w2.get_price() + w2.get_shipping());
		System.out.println(str1 + "," + str2);
	}

}


