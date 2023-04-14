package br.com.fiap.model;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.awt.Desktop;
import java.net.URI;

public class RoyalBard {
    List<Author> authors = new ArrayList<>();
    List<Song> songs = new ArrayList<>();

    public void addAuthor(String name) {
        this.authors.add(new Author(name));
    }

    public void addAuthor(Author author) {
        this.authors.add(author);
    }

    public void removeAuthor(String name) {
        for (Author author : this.authors) {
            if (author.getName().equals(name)) {
                this.authors.remove(author);
            }
        }
    }

    public Author getAuthor(String name) {
        for (Author author : this.authors) {
            if (author.getName().equals(name)) {
                return author;
            }
        }
        throw new RuntimeException("Author not found");
    }

    public void showAuthors() {
        for (Author author : this.authors) {
            System.out.println(author.getName());
        }
    }

    public void addSong(String authorName, String title, String youtubePath) {
        Author author = getAuthor(authorName);
        Song song = new Song(author, title, youtubePath);
        author.addSong(song);
        this.songs.add(song);
    }

    public void addSong(String authorName, String title, String genre, int year, int duration, String youtubePath) {
        Author author = getAuthor(authorName);
        Song song = new Song(author, title, genre, year, duration, youtubePath);
        author.addSong(song);
        this.songs.add(song);
    }

    public void addSong(Song song) {
        this.songs.add(song);
    }

    public Song getSong(String title) {
        for (Song song : this.songs) {
            if (song.getTitle().equals(title)) {
                return song;
            }
        }
        throw new RuntimeException("Song not found");
    }

    public void getSong(String title, String authorName) {
        for (Song song : getAuthor(authorName).getSongs()) {
            if (song.getTitle().equals(title)) {
                System.out.println(song);
            }
        }
    }

    public void showSongs() {
        for (Author author : this.authors) {
            author.showSongs();
        }
    }

    public void play(String title) {
        for (Author author : this.authors) {
            for (Song song : author.getSongs()) {
                if (song.getTitle().equals(title)) {
                    System.out.println("Tocando \"" + song.getTitle() + "\" de " + song.getAuthor().getName());
                    String url = song.getYoutubePath();
                    Desktop desktop = Desktop.getDesktop();
                    try {
                        desktop.browse(new URI(url));
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                    return;
                }
            }
        }
        System.out.println("Música nao encontrada");
    }

    public void play(String title, String authorName) {
        for (Song song : getAuthor(authorName).getSongs()) {
            if (song.getTitle().equals(title)) {
                System.out.println("Tocando \"" + song.getTitle() + "\" de " + song.getAuthor().getName());
                String url = song.getYoutubePath();
                Desktop desktop = Desktop.getDesktop();
                try {
                    desktop.browse(new URI(url));
                } catch (Exception e) {
                    e.printStackTrace();
                }
                return;
            }
        }
        System.out.println("Música nao encontrada");
    }

    public void playRandom() {
        Random rand = new Random();
        System.out.println("Possiveis musicas:");
        System.out.println(songs);
        Song song = songs.get(rand.nextInt(songs.size()));
        String url = song.getYoutubePath();
        Desktop desktop = Desktop.getDesktop();
        try {
            desktop.browse(new URI(url));
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

}
