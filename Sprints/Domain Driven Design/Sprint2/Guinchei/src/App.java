import br.com.fiap.models.*;

public class App {
    static boolean debugApp = false;

    public static void main(String[] args) throws Exception {
        Sistema sb = new Sistema();
        Usuario usuarioLogado = null;

        sb.loadData();
        for (Caso caso : sb.getCasos()) {
            System.out.println(caso.getAcidente());
            System.out.println(caso.getLocal());
            System.out.println(caso.getDataHora());
            System.out.println(caso.getTipo());
            System.out.println(caso.getStatus());
            System.out.println(caso.getUsuario().getEmail());
        }

        if (debugApp) {
            usuarioLogado = sb.buscarUsuario("augustobb@live.com");
        } else {
            usuarioLogado = Interface.login(sb);
        }

        while (true) {
            int opcao = Interface.menu(usuarioLogado);
            switch (opcao) {
                case -1:
                    System.exit(0);
                    break;
                case 0:
                    sb.saveData();
                    System.exit(0);
                    break;
                case 1:
                    Interface.solicitarGuincho(usuarioLogado, sb);
                    break;
                case 2:
                    Interface.listarGuinchos();
                    break;
                case 3:
                    Interface.contato();
                    break;
                case 4:
                    Interface.verMeusDados(usuarioLogado);
                    break;
                case 5:
                    usuarioLogado = Interface.login(sb);
                    break;
                default:
                    System.exit(0);
                    break;

            }
        }

    }
}
