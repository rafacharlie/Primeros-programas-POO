/**2. Crea la clase “Circulo” en Java que responda al siguiente comportamiento:

    -Un círculo puede crecer. Aumenta su radio.
    -Un círculo puede menguar. Decrementa su radio.
    -Un círculo me devuelve su área si se la pido.
    -Un círculo me dice su estado, por ejemplo “Soy un círculo de radio 0.5 metros.
     Ocupo un área de 0.7853981633974483 metros cuadrados” (método toString())

@author Rafael Infante
 * */
package primerosProgramasPoo;

import javax.swing.JOptionPane;

public class Circulo {
	
	//Los atributos se declaran fuera del constructor importante
	double a;
	double r;
	double pi;
	
	//constructor. Se inicializan aqui importante
	public Circulo() {
		a=0; //area
		r=0; //radio
		pi=3.141592;
	}
	
	/**metodo que aumenta el area del circulo pasandole una variable
	 * como parametro que multiplica el radio y devuelve el area.
	 * 
	 * @param radio
	 * @return area
	 * 
	 * @author Rafael Infante
	 * */
	public double aumentaCirculo(double numero){
		this.r*=numero;
		this.a=this.pi*Math.pow(this.r, 2);
		return this.a;
	}
	
	/**metodo que decrementa el area del circulo pasandole una variable
	 * como parametro que divide el radio y devuelve el area.
	 * 
	 * @param radio
	 * @return area
	 * 
	 * @author Rafael Infante
	 * */
	public double decrementaCirculo(double numero){
		this.r/=numero;
		this.a=this.pi*Math.pow(this.r, 2);
		return this.a;
	}
	
	/**metodo que calcula el area del circulo.
	 * 
	 * @param radio
	 * @return area
	 *
	 * @author Rafael Infante
	 * */
	public double calculaAreaCirculo(double radio){
		this.r=radio;
		this.a=this.pi*Math.pow(this.r, 2);
		return this.a;
	}
	
	/**metodo que devuelve el estado del circulo en una cadena String.
	 * 4. Modifica la clase Círculo para que cuando el radio se convierta a 0 el
	 *  círculo reaccione y diga con una caja de texto gráfica “Soy un mísero punto 
	 *  sin área” usando la clase JOptionPane del paquete javax.swing. Podéis ver
	 *   este vídeo: https://youtu.be/F_48qh3BcDs
	 * 
	 * @param radio
	 * @return String
	 * 
	 * @author Rafael Infante
	 * */
	public String estadoCirculo() {
		if(this.r==0) {
			return JOptionPane.showInputDialog("Soy un misero punto sin area.");
		}else {
			return "Soy un círculo de radio " + this.r + " metros."
				+ " Ocupo un área de " + this.a + " metros cuadrados.";
		}
	}
}
