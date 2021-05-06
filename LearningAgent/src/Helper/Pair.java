package Helper;

public class Pair<Type1,Type2> {
	private Type1 element1;
	private Type2 element2;
	
	public Pair(Type1 element1, Type2 element2) {
		this.element1 = element1;
		this.element2 = element2;
	}

	public Type1 getElement1() {
		return element1;
	}

	public void setElement1(Type1 element1) {
		this.element1 = element1;
	}

	public Type2 getElement2() {
		return element2;
	}

	public void setElement2(Type2 element2) {
		this.element2 = element2;
	}
	
	
}
