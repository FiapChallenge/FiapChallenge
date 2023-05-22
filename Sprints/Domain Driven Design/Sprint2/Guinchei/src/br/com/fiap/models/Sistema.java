package br.com.fiap.models;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Sistema {
    Categoria categoria;
    List<Caso> casos = new ArrayList<Caso>();
    private List<Usuario> usuarios = new ArrayList<Usuario>();

    public Sistema() {
        this.categoria = new Categoria();
    }

    public List<Caso> getCasos() {
        return casos;
    }

    public void addCaso(Caso caso) {
        casos.add(caso);
    }

    public void saveData() {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter("data.txt"))) {
            for (Usuario usuario : usuarios) {
                String row = usuario.getNome() + ";" + usuario.getEmail() + ";" + usuario.getSenha() + ";"
                        + usuario.getFotopath();
                bw.write(row);
                bw.newLine();
            }
        } catch (IOException e) {
            System.out.println("Erro ao salvar arquivo");
        }
        try (BufferedWriter bw = new BufferedWriter(new FileWriter("casos.txt"))) {
            for (Caso caso : casos) {
                String row = caso.getAcidente() + ";" + caso.getLocal() + ";" + caso.getDataHora() + ";"
                        + caso.getTipo() + ";" + caso.getStatus() + ";" + caso.getUsuario().getEmail();
                bw.write(row);
                bw.newLine();
            }
        } catch (IOException e) {
            System.out.println("Erro ao salvar arquivo");
        }
    }

    public void loadData() {
        List<List<String>> data = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader("data.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] values = line.split(";");
                data.add(Arrays.asList(values));
            }
        } catch (Exception e) {
            System.out.println("Erro ao ler arquivo");
        }
        for (List<String> row : data) {
            Usuario usuario = new Usuario(row.get(0), row.get(1), row.get(2), row.get(3));
            usuarios.add(usuario);
        }
        List<List<String>> dataCasos = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader("casos.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] values = line.split(";");
                dataCasos.add(Arrays.asList(values));
            }
        } catch (Exception e) {
            System.out.println("Erro ao ler arquivo");
        }
        for (List<String> row : dataCasos) {
            Usuario usuario = buscarUsuario(row.get(5));
            Caso caso = new Caso(row.get(0), row.get(1), row.get(2), row.get(3), row.get(4), usuario);
            casos.add(caso);
        }
    }

    public void addUsuario(String nome, String email, String senha) {
        Usuario usuario = new Usuario(nome, email, senha);
        usuarios.add(usuario);
    }

    public void addUsuario(Usuario usuario) {
        usuarios.add(usuario);
    }

    public Usuario buscarUsuario(String email) {
        for (Usuario usuario : usuarios) {
            if (usuario.getEmail().equals(email)) {
                return usuario;
            }
        }
        return null;
    }

    public Categoria getCategoria() {
        return categoria;
    }
}
