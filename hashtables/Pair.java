package hashtables;

class Pair {
	String key;
	String value;
    Pair next;

    public Pair(String key, String value) {
        this.key = key;
        this.value = value;
    }

	public void setKey(String key) {
		this.key = key;
	}
	public void setValue(String value) {
		this.value = value;
	}		
    public void setNext(Pair next) {
        this.next = next;
    }       
	public String getKey() {
		return this.key;
	}		
	public String getValue() {
		return this.value;
	}
    public Pair getNext() {
        return this.next;
    }
}
