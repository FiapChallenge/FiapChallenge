package br.com.fiap.model;

import java.util.Iterator;
import java.util.ArrayList;
import java.util.List;

public class Author {
    private List<Song> songs = new ArrayList<>();
    private String name;
    private List<Album> albums = new ArrayList<>();

    public Author(String name) {
        this.name = name;

    }

    public Author(String name, List<Song> songs) {
        this.name = name;
        this.songs = songs;
    }

    public List<Song> getSongs() {
        return songs;
    }

    public void setSongs(List<Song> songs) {
        this.songs = songs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void addSong(Song song) {
        this.songs.add(song);
    }

    public void removeSong(Song song) {
        this.songs.remove(song);
    }

    public void showSongs() {
        System.out.print("Sons de " + this.songs.get(0).getAuthor().getName() + ": ");
        for (Iterator<Song> it = this.songs.iterator(); it.hasNext();) {
            Song song = it.next();
            if (!it.hasNext()) {
                System.out.println(song.getTitle());
            } else {
                System.out.print(song.getTitle());
                System.out.print(", ");
            }
        }
    }

    public List<Album> getAlbums() {
        return albums;
    }

    public void addAlbum(Album album) {
        this.albums.add(album);
    }

    public void removeAlbum(Album album) {
        this.albums.remove(album);
    }

    public void showAlbuns() {
        System.out.print("Álbuns de " + this.name + ": ");
        for (Iterator<Album> it = this.albums.iterator(); it.hasNext();) {
            Album album = it.next();
            if (!it.hasNext()) {
                System.out.println(album.getName() + " (" + album.getYear() + ")");
            } else {
                System.out.print(album.getName() + " (" + album.getYear() + ")");
                System.out.print(", ");
            }
        }
    }

    @Override
    public String toString() {
        return name;
    }
}
