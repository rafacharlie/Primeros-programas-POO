package primerosProgramasPoo;

public class Fraccion {
	int numerador;
	int denominador;
	
	//constructor
	public Fraccion(int num, int denom) {
		numerador=num;
		denominador=denom;
	}
	/**metodo para obtener la fraccion.
	 * 
	 * @return String
	 * 
	 * @author Rafael Infante
	 * */
	
	public String obtenerFraccion() {
		return "La fraccion obtenida es: " + this.numerador + "/" + this.denominador;
	}
	/**metodo que modifica el numerador y denominador de la fraccion.
	 * 
	 * @param: int numerador
	 * @param: int denominador
	 * 
	 * @author Rafael Infante
	 * */
	
	public void modificarFraccion(int num, int den) {
		if(den==0) {
			System.out.println("No se puede dividir el denominador es igual a 0");
		}else {
			this.numerador=num;
			this.denominador=den;
		}
		
	}
	/**metodo que en el que obtienes el resultado de dividir numerador y 
	 * denominador de la fraccion.
	 * 
	 * @return int
	 * 
	 * @author Rafael Infante
	 * */
	
	public int resultadoFraccion() {
		return this.numerador/this.denominador;
	}
	/**metodo que multiplica la fraccion por un numero.
	 * 
	 * @param: int numero
	 * 
	 * @author Rafael Infante
	 * */
	
	public void multiplicaFraccionPorUnnumero(int num) {
		this.numerador *= num;
	}
	/**metodo que resta fracciones.
	 * 
	 * @param: int numerador
	 * @param: int denominador
	 * 
	 * @author Rafael Infante
	 * */
	
	public void restarFracciones(int num,int den) {
		//multiplicamos los denominadores
		int var3=this.denominador*den;
		//calculamos el resultado del primer numerador
		int var1=var3/this.denominador;
		var1*=this.numerador;
		//calculamos el resultado del segundo numerador
		int var2=var3/den;
		var2*=num;
		//restamos los numeradores
		this.numerador=var1-var2;
		this.denominador=var3;
	}
	/**metodo que suma fracciones.
	 * 
	 * @param: int numerador
	 * @param: int denominador
	 * 
	 * @author Rafael Infante
	 * */
	
	public void sumarFracciones(int num,int den) {
		//multiplicamos los denominadores
		int var3=this.denominador*den;
		//calculamos el resultado del primer numerador
		int var1=var3/this.denominador;
		var1*=this.numerador;
		//calculamos el resultado del segundo numerador
		int var2=var3/den;
		var2*=num;
		//sumamos los numeradores
		this.numerador=var1+var2;
		this.denominador=var3;
	}
	/**metodo que multiplica fracciones.
	 * 
	 * @param: int numerador
	 * @param: int denominador
	 * 
	 * @author Rafael Infante
	 * */
	
	public void multiplicaFracciones(int num, int den) {
		this.numerador *= num;
		this.denominador*=den;
	}
	
	public int hallarMcd() {
		int dividendo;
		int divisor;
		dividendo=this.numerador;
		divisor=this.denominador;
		while(dividendo%divisor!=0) {
			int resto = dividendo%divisor;
			dividendo=divisor;
			divisor=resto;
		}
		
		return divisor;
	}
	
	public void simplificarFraccion() {
		int mcd=hallarMcd();
		this.numerador/=mcd;
		this.denominador/=mcd;

	}
	
	
}


