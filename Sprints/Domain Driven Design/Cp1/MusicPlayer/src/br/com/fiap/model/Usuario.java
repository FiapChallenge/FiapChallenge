package br.com.fiap.model;

import java.util.ArrayList;
import java.util.List;

public class Usuario {
    private String username;
    private String password;
    private List<Song> favoriteSongs = new ArrayList<>();

    public Usuario(String user, String password) {
        this.username = user;
        this.password = password;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String user) {
        this.username = user;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public void addFavoriteSong(Song song) {
        this.favoriteSongs.add(song);
    }

    public void showFavoriteSongs() {
        System.out.print("Sons favoritos de " + this.username + ": ");
        boolean last = false;
        for (Song song : this.favoriteSongs) {
            last = this.favoriteSongs.indexOf(song) == this.favoriteSongs.size() - 1;
            if (last) {
                System.out.println(song.getTitle());
            } else {
                System.out.print(song.getTitle());
                System.out.print(", ");
            }
        }
    }
}
