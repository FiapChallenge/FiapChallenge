package br.com.fiap.models;

public class Usuario {
    String nome;
    String email;
    String senha;
    String fotopath = "";

    public Usuario(String nome, String email, String senha) {
        this.nome = nome;
        this.email = email;
        this.senha = senha;
    }
    

    public Usuario(String nome, String email, String senha, String fotopath) {
        this.nome = nome;
        this.email = email;
        this.senha = senha;
        this.fotopath = fotopath;
        System.out.println("Usuário criado com sucesso!");
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }
}
