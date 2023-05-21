import br.com.fiap.models.*;


public class App {
    public static void main(String[] args) throws Exception {
        Sistema sb = new Sistema();
        Usuario usuarioLogado = null;
        
        sb.loadData();

        usuarioLogado = Interface.login(sb);



    }
}
