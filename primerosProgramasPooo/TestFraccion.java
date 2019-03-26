package primerosProgramasPoo;

public class TestFraccion {

	public static void main(String[] args) {
		
		Fraccion miFraccion=new Fraccion(10,12); //objeto
		
		System.out.println(miFraccion.obtenerFraccion());
		miFraccion.simplificarFraccion();
		System.out.println(miFraccion.obtenerFraccion());
		
	}

}
